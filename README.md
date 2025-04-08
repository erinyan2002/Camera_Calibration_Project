# 🧮 Homework #3 - Camera Calibration & Lens Distortion Correction

---

## 🌐 목표

이 프로젝트의 목표는 내가 사용하는 카메라의 렌즈 왜곡을 보정하는 것입니다.
체스보드 이미지를 다양한 각도에서 촬영한 동영상을 이용해,
카메라의 내부 파라미터 (초점 거리, 중심 좌표 등)를 계산하고
계산된 결과를 이용해 렌즈 왜곡을 보정한 이미지를 만들어냅니다.

이 과정을 통해 카메라가 실제로 어떻게 세상을 왜곡해서 보는지 이해하고,
그 왜곡을 보정하는 방법을 직접 실습하게 됩니다.

---

## 📜 사용 스크립트 설명

### 1. camera_calibration.py
- 입력: 체스보드 영상 (mp4)
- 출력: camera_params.npz (내부 파라미터 포함)

### 2. check_camera_params.py
- camera_params.npz 로드 후 파라미터 확인 출력

### 3. distortion_correction.py
- 입력 이미지(test_image.jpg)에서 왜곡 제거된 결과 저장

## 📂 폴더 및 파일 구조

📁 Camera_Calibration_Project/
├── 📁 frames/ │
├── corner_0.png │ 
├── corner_1.png │ 
├── corner_2.png │ 
├── corner_3.png │ 
└── corner_4.png 
├── 📄 camera_calibration.py 
├── 📄 camera_params.npz 
├── 📄 check_camera_params.py
├── 📄 chessboard.mp4 
├── 📄 distortion_correction.py 
├── 📄 README.md 
├── 📄 test_image.jpg 
└── 📄 undistorted_result.jpg


---

✅ 작업 정보

## ▶ 1. Chessboard 출력 & 도영상 지정

Chessboard Collection 참고

A4 용지에 체스보드 출력 후 다양한 각도에서 영상 촬영



## 예시 영상: 




https://github.com/user-attachments/assets/a9ed336d-227e-4a51-acb6-fc25a1407cfc



## 실행예시 화면 


![image](https://github.com/user-attachments/assets/aeabde7b-625f-4ba2-beb0-31275c072c6e)



![image](https://github.com/user-attachments/assets/4eb93c7a-7ea1-4bcd-9ceb-b7f1a69ef6f4)






---


## ▶ 2. 카메라 캘리브레이션 수행

사용 스크립트: camera_calibration.py

처리 흐름:

- 동영상에서 프레임 추출

- 각 프레임에서 체스보드 코너 검출 (cv2.findChessboardCorners)

- 검출된 코너 시각화 및 저장 (cv2.drawChessboardCorners)

- cv2.calibrateCamera로 내부 파라미터 계산

- 결과를 camera_params.npz로 저장 (mtx, dist, rvecs, tvecs, error)

출력 이미지 예시 (코너 검출 프레임):



![corner_0](https://github.com/user-attachments/assets/8c34a2b8-303a-4674-904b-19569950df0d)




![corner_4](https://github.com/user-attachments/assets/a180f673-f850-4eca-be38-d8f49fa5f2e0)

...

## 📊 캘리브레이션 결과 요약

| 파라미터 | 값 |
|----------|------------------|
| fx       | 1892.98          |
| fy       | 1894.97          |
| cx       | 992.17           |
| cy       | 502.35           |
| dist     | [0.2322, -1.9172, -0.0022, -0.0020, 5.0933] |
| RMSE     | 2.1978           |


Camera matrix:
[[1.89298384e+03 0.00000000e+00 9.92168086e+02]

 [0.00000000e+00 1.89497962e+03 5.02348455e+02]
 
 [0.00000000e+00 0.00000000e+00 1.00000000e+00]]

Distortion coefficients:
[[ 2.32246521e-01 -1.91728901e+00 -2.20117167e-03 -2.02646111e-03 5.09334929e+00]]

Reprojection error (RMSE): 2.197819866097877


---


## ▶ 3. 카메라 파라미터 확인 (check_camera_params.py)



![image](https://github.com/user-attachments/assets/a2b34d19-ec8b-4b20-9bdf-8150ab27e50e)



---



## ▶ 4. 렌즈 왜곡 보정

사용 스크립트: distortion_correction.py

캘리브레이션 결과 불러오기 (camera_params.npz)

왜곡 보정 수행: cv2.undistort

시각화 및 비교

입력 이미지: Original


![test_image](https://github.com/user-attachments/assets/1951c5dc-cbfe-4911-92d5-38d8ec4e090f)




출력 이미지: Undistorted






![undistorted_result](https://github.com/user-attachments/assets/8bb03446-a68d-46ee-bd01-fe217f2bafdf)



---


## 📚 정리

캘리브레이션 완료 및 파라미터 저장 (fx, fy, cx, cy, dist, rmse)

왜곡 보정 결과 이미지 생성 완료

모든 과정은 OpenCV 기반 Python으로 수행


