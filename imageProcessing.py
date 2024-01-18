import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.morphology import skeletonize

"""
Shading


"""

class shadingProcessing:
    def __init__(self):
        pass
    
    def calculate_diagonal_shading(self, image_path):
# Load the image
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # Quantize the image into 4 bits
        quantized_image = self.quantize_image(image)

        # Separate shading into 4 levels
        shading_levels = self.separate_shading(quantized_image)

        # Convert shaded blocks into diagonal contour lines
        level_contours = self.convert_to_contours(shading_levels)

        filled_image = self.fill_contours_with_lines(level_contours, image.shape)
        
        return filled_image
    
    def calculate_cross_hatching(self, image_path):
        pass

# Function to quantize an image into 4 bits
    def quantize_image(self, image):
        return (image // 64) * 64

    def separate_shading(self, image):
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Define intensity thresholds
        thresholds = [64, 128, 192, 255]
        
        shading_levels = []
        
        # Iterate through thresholds to create shading levels
        for i in range(1, len(thresholds) + 1):
            lower_threshold = thresholds[i - 1]
            upper_threshold = thresholds[i] if i < len(thresholds) else 256  # Use a high upper limit for the last level
            level_mask = cv2.inRange(image, lower_threshold, upper_threshold)
            cv2.imshow('thresh', level_mask)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            shading_levels.append(level_mask)

        return shading_levels

    def convert_to_contours(self, shading_levels):
        level_contours = []
        
        for i, level in enumerate(shading_levels, start=1):
            contour_lines = []
            contours, _ = cv2.findContours(level, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                epsilon = 0.001 * cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, epsilon, True)
                
                # Sorting contour points from top-left
                sorted_points = sorted(approx[:, 0], key=lambda x: x[0] + x[1])
                contour_lines.append((i, sorted_points, approx))
        
            level_contours.append(contour_lines)
        
        return level_contours

# Function to fill contours with diagonal lines
    def fill_contours_with_lines(self, level_contours, image_shape):
        combined_levels = np.zeros(image_shape, dtype=np.uint8) 
        for i in range(len(level_contours)):
            combined_mask = np.zeros(image_shape, dtype=np.uint8)
            for _, _, approx in level_contours[i]:
                mask = np.zeros(image_shape, dtype=np.uint8)
                cv2.drawContours(mask, [approx], -1, 255, thickness=cv2.FILLED)
                combined_mask = cv2.bitwise_or(combined_mask, mask)
            
        
            filled_image = draw_diagonal_lines(combined_mask, (i+1) * 5)
            cv2.imshow(f'filled{i}', filled_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            combined_levels = cv2.bitwise_and(combined_levels, filled_image)

        return filled_image

# Function to draw diagonal lines on a mask
    def draw_diagonal_lines(self, mask, spacing):
        diagonal_lines = np.zeros_like(mask, dtype=np.uint8)

        for i in range(0, diagonal_lines.shape[0] + diagonal_lines.shape[1], spacing):
            cv2.line(diagonal_lines, (0, i), (diagonal_lines.shape[1], i - diagonal_lines.shape[1]), 255, 1)

        inverted_mask = cv2.bitwise_not(mask)
        cv2.imshow('Inverted', inverted_mask)
        cv2.imshow('mask', mask)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return cv2.bitwise_and(diagonal_lines, inverted_mask)



"""Outline"""

def convert_image(img_path):
  img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
  imgColor = cv2.imread(img_path)
  if img is None:
      return -1
  div = 64
  quantized = img // div * div + div // 2
  edges = cv2.Canny(img, 100, 200)
  
  skeleton = skeletonize(edges)
  
  skeleton = skeleton.astype(np.uint8) * 255
  
  contours, _ = cv2.findContours(skeleton, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
  print(contours)
  # Iterate through contours and approximate the polygons
  for contour in contours:
        # Choose an epsilon value based on the accuracy required
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
  return approx


class makeOutline:
    def __init__(self, image_path):
    #convert image to single pixel vectors
        pass
        
    def drawOutline(self, image_path):
        convert_image(image_path)
    
