import numpy as np

data = np.load('camera_params.npz')

print("✅ Camera matrix:\n", data['mtx'])
print("✅ Distortion coefficients:\n", data['dist'])

# 'error'가 저장된 경우만 출력
if 'error' in data:
    print("✅ Reprojection error (RMSE):", data['error'])
else:
    print("⚠️ 'error' 값이 camera_params.npz에 저장되어 있지 않음!")
