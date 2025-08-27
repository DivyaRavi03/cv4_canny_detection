import cv2
import numpy

img_path = "test_img.jpg"

img = cv2.imread(img_path)

if img is None:
	print(f"Error  in image path: {img_path}")
else:
	print("Image loaded")
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,100,200)
	cv2.imshow("Original",img)
	cv2.imshow("Canny",edges)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
