import cv2
import numpy as np
import os

CHECKERBOARD = (9, 6)

objp = np.zeros((CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)

objpoints = []
imgpoints = []

# ✅ 프레임 저장 폴더 생성
os.makedirs('frames', exist_ok=True)

cap = cv2.VideoCapture('chessboard.mp4')

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    found, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, None)

    if found:
        objpoints.append(objp)
        imgpoints.append(corners)
        cv2.drawChessboardCorners(frame, CHECKERBOARD, corners, found)

        # ✅ 프레임 저장
        cv2.imwrite(f'frames/corner_{frame_count}.png', frame)
        frame_count += 1

        # (옵션) 확인용 시각화
        cv2.imshow('Corners', frame)
        cv2.waitKey(100)

cap.release()
cv2.destroyAllWindows()

# 🔍 카메라 캘리브레이션 수행
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print("Camera matrix:\n", mtx)
print("Distortion coefficients:\n", dist)
print("Reprojection error:", ret)

# ✅ 모든 파라미터 저장 (error 포함)
np.savez('camera_params.npz', mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvecs, error=ret)
