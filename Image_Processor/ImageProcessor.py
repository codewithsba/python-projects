import cv2

# Corrected image path
image_path = 'D:/Py_Programs_Sba/Python_Project_file/apple.webp'  # Ensure this path is correct
apple = cv2.imread(image_path)

# Adjusted rectangle coordinates for a bigger rectangle
rectangle_coordinates = (50, 50, 335, 335)  # Doubled width and height

# Rectangle color in BGR format (Red, Green, Blue)
rectangle_color = (0, 255, 0)

# Draw the rectangle with a thickness of 2 pixels to outline it
cv2.rectangle(apple, rectangle_coordinates, rectangle_color, 2)

# Display the modified image
cv2.imshow('apple', apple)  # Corrected window name
cv2.waitKey(0)
cv2.destroyAllWindows()
