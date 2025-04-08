# 🧮 Homework #3 - Camera Calibration

---

🌐 목표

내 카메라를 칼리브리언하기

🔧 사용 프로그램

camera_calibration.py

check_camera_params.py

distortion_correction.py

✅ 작업 정보

▶ 1. Chessboard 출력 & 도영상 지정

Chessboard Collection 참고

A4 용지에 체스보드 출력 후 다양한 각도에서 영상 촬영

예시 영상: 




https://github.com/user-attachments/assets/a9ed336d-227e-4a51-acb6-fc25a1407cfc





▶ 2. 카메라 캘리브레이션 수행

사용 스크립트: camera_calibration.py

처리 흐름:

동영상에서 프레임 추출

각 프레임에서 체스보드 코너 검출 (cv2.findChessboardCorners)

검출된 코너 시각화 및 저장 (cv2.drawChessboardCorners)

cv2.calibrateCamera로 내부 파라미터 계산

결과를 camera_params.npz로 저장 (mtx, dist, rvecs, tvecs, error)

출력 이미지 예시 (코너 검출 프레임):

![corner_0](https://github.com/user-attachments/assets/8c34a2b8-303a-4674-904b-19569950df0d)




![corner_4](https://github.com/user-attachments/assets/a180f673-f850-4eca-be38-d8f49fa5f2e0)

...



결과 출력 예시:

Camera matrix:
[[1.89298384e+03 0.00000000e+00 9.92168086e+02]
 [0.00000000e+00 1.89497962e+03 5.02348455e+02]
 [0.00000000e+00 0.00000000e+00 1.00000000e+00]]

Distortion coefficients:
[[ 2.32246521e-01 -1.91728901e+00 -2.20117167e-03 -2.02646111e-03 5.09334929e+00]]

Reprojection error (RMSE): 2.197819866097877

fx: 1892.98

fy: 1894.97

cx: 992.17

cy: 502.35

dist: [0.2322, -1.9172, -0.0022, -0.0020, 5.0933]

rmse: 2.1978

▶ 3. 카메라 파라미터 확인 (check_camera_params.py)

import numpy as np

data = np.load('camera_params.npz')
print("Camera matrix:\n", data['mtx'])
print("Distortion coefficients:\n", data['dist'])
print("Reprojection error (RMSE):", data['error'])

▶ 4. 렌즈 왜곡 보정

사용 스크립트: distortion_correction.py

캘리브레이션 결과 불러오기 (camera_params.npz)

왜곡 보정 수행: cv2.undistort

시각화 및 비교

입력 이미지: Original


![test_image](https://github.com/user-attachments/assets/1951c5dc-cbfe-4911-92d5-38d8ec4e090f)




출력 이미지: Undistorted






![undistorted_result](https://github.com/user-attachments/assets/8bb03446-a68d-46ee-bd01-fe217f2bafdf)






📚 정리
