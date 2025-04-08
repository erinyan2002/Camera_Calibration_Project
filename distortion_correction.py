import cv2
import numpy as np

# 이미지 불러오기
img = cv2.imread('./test_image.jpg')
if img is None:
    raise FileNotFoundError("test_image.jpg 파일이 없습니다!")

# 저장한 파라미터 불러오기
with np.load('camera_params.npz') as X:
    mtx, dist = X['mtx'], X['dist']

# 왜곡 보정
h, w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

# 결과 저장
cv2.imwrite('undistorted_result.jpg', dst)

# 시각화
cv2.imshow('Original', img)
cv2.imshow('Undistorted', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
