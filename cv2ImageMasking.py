import numpy as np
import cv2

img = cv2.imread('Xc7y3Q_2019111_132047_38_CV2.png', cv2.IMREAD_COLOR)
cv2.rectangle(img, (512,183), (647,215), (0,0,0), -1)
cv2.rectangle(img, (775,396), (860,417), (0,0,0), -1)
cv2.rectangle(img, (360,486), (510,520), (0,0,0), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Verified ID', (45,530), font, 1, (0,0,255), 2)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
