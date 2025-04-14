import cv2 as cv
import numpy as np

with np.load('camera_params.npz') as X:
    mtx, dist = [X[i] for i in ('mtx', 'dist')]

chessboard_size = (9, 6)
square_size = 0.024

objp = np.zeros((np.prod(chessboard_size), 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)
objp *= square_size

cap = cv.VideoCapture(0)
saved = False  # 저장 여부 flag

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    ret, corners = cv.findChessboardCorners(gray, chessboard_size, None)

    if ret:
        cv.cornerSubPix(gray, corners, (11, 11), (-1, -1),
                        criteria=(cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001))

        success, rvecs, tvecs = cv.solvePnP(objp, corners, mtx, dist)

        # 코너 시각화
        cv.drawChessboardCorners(frame, chessboard_size, corners, ret)

        # 도형 투영
        axis = np.float32([
            [0, 0, 0], [0.05, 0.1, 0], [0.1, 0, 0],
            [0.035, 0.05, 0], [0.065, 0.05, 0]
        ])
        imgpts, _ = cv.projectPoints(axis, rvecs, tvecs, mtx, dist)
        imgpts = imgpts.reshape(-1, 2).astype(int)

        cv.line(frame, tuple(imgpts[0]), tuple(imgpts[1]), (255, 0, 0), 3)
        cv.line(frame, tuple(imgpts[1]), tuple(imgpts[2]), (255, 0, 0), 3)
        cv.line(frame, tuple(imgpts[3]), tuple(imgpts[4]), (0, 0, 255), 2)

        if not saved:
            cv.imwrite('ar_result.jpg', frame)
            print("📸 이미지 저장 완료: ar_result.jpg")
            saved = True

    cv.imshow('AR Pose Estimation', frame)
    if cv.waitKey(1) == 27:  # ESC 키
        break

cap.release()
cv.destroyAllWindows()
