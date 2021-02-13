import cv2

image = cv2.imread("data/logo.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("OpenCV logo", image)
cv2.imshow("OpenCV logo gray format", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
