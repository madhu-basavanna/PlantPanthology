# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import matplotlib.pyplot as plt

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # Load two images
    img1 = cv2.imread('/home/madhu/Downloads/plant-pathology-2021-fgvc8/test_images/85f8cb619c66b863.jpg')
    img2 = cv2.imread('/home/madhu/timage.jpg')
    height, width, _ = img1.shape
    img2 = cv2.resize(img2, (width, height))
    # I want to put logo on top-left corner, So I create a ROI
    rows, cols, channels = img2.shape
    roi = img1[0:rows, 0:cols]
    # Now create a mask of logo and create its inverse mask also
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
    # Put logo in ROI and modify the main image
    dst = cv2.add(img1_bg, img2_fg)
    dst = cv2.resize(dst, (width, height))
    img1[0:rows, 0:cols] = dst
    cv2.imshow('res', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
