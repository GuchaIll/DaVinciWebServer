from flask import Flask, render_template, request, redirect, url_for, session
import os
from werkzeug.utils import secure_filename
from imageEdit import modifyImageModel
from imageGen2 import generateImageModel
#loading flask and the models
app = Flask(__name__)
app.secret_key = "key"

ImageEdit_model = modifyImageModel()
ImageGen_model = generateImageModel()
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'
}
app.config['UPLOAD_FOLDER'] = "./static/uploads"
app.config['SUBMISSION_FOLDER'] = "./static/processed"

working_filepath = None

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/generate', methods=['GET', 'POST'])
def generateImage():
  if request.method == 'POST':
    prompt = request.form.get('user_input', '')
    if prompt:
      result = ImageGen_model.generate_image(prompt)
      filename = secure_filename(prompt)
      file_path = os.path.join(app.config['SUBMISSION_FOLDER'], filename)
      result.save(file_path)
      return render_template('generated.html', result = filename)
    return render_template('generate.html')
  return render_template('generate.html')

@app.route('/image', methods=['GET', 'POST'])
def uploadImage():
  if request.method == 'POST':
    user_input = request.form.get('user_input', '')
    if user_input and 'working_filepath' in session:
        print("user input")
        working_filepath = session['working_filepath']
        filename = session['file_name' ] 
        result = ImageEdit_model.modify_image(working_filepath, user_input)
        result_path = secure_filename(filename)
        result_path = os.path.join(app.config['SUBMISSION_FOLDER'], result_path)
        result.save(result_path)
        
        print(result, working_filepath, user_input)
        return render_template('image.html', filename = working_filepath, result = filename)
     
    if 'file' in request.files:
      
      file = request.files['file']
      processing_type = request.form['processing_type']
      if file.filename == '':
        return redirect(request.url)
      
      if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        session['file_name' ] = filename
        session['working_filepath'] = file_path
        #result = process_image(file_path, processing_type)
        return render_template('image.html', filename=filename)
      
  return render_template('image.html')
  
if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug = True)