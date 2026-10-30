import cv2
image=cv2.imread("Cat.jpg")
resized_image1=cv2.resize(image, (200,200))
resized_image2=cv2.resize(image, (400,400))
resized_image3=cv2.resize(image, (600,600))
cv2.imshow("Resized Image (Small)", resized_image1)
cv2.imshow("Resized Image (Medium)", resized_image2)
cv2.imshow("Resized Image (Large)", resized_image3)
key=cv2.waitKey(0)
if key==ord("s"):
    cv2.imwrite("input_image_small.jpg", resized_image1)
    cv2.imwrite("input_image_medium.jpg", resized_image2)
    cv2.imwrite("input_image_large.jpg", resized_image3)
    print("Images saved as input_image_small.jpg, input_image_medium.jpg and input_image_large.jpg")
else:
    print("Image not saved")
cv2.destroyAllWindows()