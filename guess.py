from ultralytics import YOLO

# 학습된 모델 로드
model = YOLO('./yolov8n.pt')

# 이미지에 대한 추론
results = model('./car.jpg')

# 결과 시각화
for r in results:
    im_array = r.plot()  # 플롯된 이미지를 numpy 배열로 가져옵니다
    
# 결과 저장 또는 표시
import cv2
cv2.imshow("YOLOv8 Inference", im_array)
cv2.waitKey(0)
cv2.destroyAllWindows()