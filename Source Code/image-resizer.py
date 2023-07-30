import tkinter as tk
from tkinter import filedialog
import cv2

# 'Tk' is a TCL package implemented in C that adds custom commands to create and manipulate GUI widgets.
root = tk.Tk()
# withdraw() removes the window from the screen without destroying it.
root.withdraw()
# askopenfilename() returns the selected file name. (path as string).
file_path = filedialog.askopenfilename()

print(file_path)

src = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
# To read an image in Python using OpenCV, use cv2.imread() function.
# IMREAD_UNCHANGED: It specifies to load an image as such including alpha channel.

# cv2.imshow() method is used to display an image in a window.
cv2.imshow("Preview of your selected image", src)

scale_percent = int(
    input("Define the new size of your image using percentage : "))

# Calculate the percent of original dimensions
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# The cv2. resize() function can be used to upscale or downscale images depending on the desired output size.
output = cv2.resize(src, (new_width, new_height))

# cv2.imwrite() method is used to save an image to any storage device.
cv2.imwrite('newImage.jpg', output)
# waitkey() function of Python OpenCV allows users to display a window for given milliseconds or until any key is pressed.
cv2.waitKey(0)