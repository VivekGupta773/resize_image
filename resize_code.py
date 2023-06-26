import cv2
import os

# Define the directory where the images are located
image_directory = "Narendra_Modi"
image_resized = "image_resized"

# List all the image files in the directory
image_files = os.listdir(image_directory)

# Loop through each image file
for filename in image_files:
    # Check if the file is an image
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        # Load the image
        image_path = os.path.join(image_directory, filename)
        image = cv2.imread(image_path)

        # Determine the new dimensions for the resized image
        new_width = int(image.shape[1] * 0.5)
        new_height = int(image.shape[0] * 0.5)

        # Resize the image
        resized_image = cv2.resize(image, (new_width, new_height))

        # Save the resized image
        output_path = os.path.join(image_resized, "resized_" + filename)
        cv2.imwrite(output_path, resized_image)
  
    