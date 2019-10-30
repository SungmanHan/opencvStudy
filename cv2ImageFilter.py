import cv2,sys
from matplotlib import pyplot as plt
import numpy as np

def rename(pathArg):
    orgPath = pathArg
    tempSplit = orgPath.split("/")
    orgFileName = tempSplit[-1]
    tempSplit = orgFileName.split(".")
    newFileName = tempSplit[0] +"_CV2."+ tempSplit[1]
    return orgPath.replace(orgFileName,newFileName)

def cv2ImageFilter(pathArg):
    imgPath = pathArg
    rImgPath = rename(imgPath)

    img = cv2.imread(imgPath)
    image_gray = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
    
    b, g, r = cv2.split(img)
    img2 = cv2.merge([r, g, b])
    
    blur = cv2.GaussianBlur(image_gray, ksize=(5,5), sigmaX=4)
    ret, thresh1 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

    edged = cv2.Canny(blur, 10, 200)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
    total = 0

    contours_xy = np.array(contours)
    contours_xy.shape

    # x의 min과 max 찾기
    x_min, x_max = 0, 0
    value = list()
    for i in range(len(contours_xy)):
        for j in range(len(contours_xy[i])):
            value.append(contours_xy[i][j][0][0])  # 네번째 괄호가 0일때 x의 값
            x_min = min(value)
            x_max = max(value)

    # y의 min과 max 찾기
    y_min, y_max = 0, 0
    value = list()
    for i in range(len(contours_xy)):
        for j in range(len(contours_xy[i])):
            value.append(contours_xy[i][j][0][1])  # 네번째 괄호가 0일때 x의 값
            y_min = min(value)
            y_max = max(value)

    # image trim 하기
    x = x_min
    y = y_min
    w = x_max - x_min
    h = y_max - y_min

    img_trim = img[y:y + h, x:x + w]
    cv2.imwrite(rImgPath, img_trim,[int(cv2.IMWRITE_PNG_COMPRESSION), 9])
    
    return rImgPath

print(cv2ImageFilter(sys.argv[1]))