from ultralytics import YOLO

# 모델 로드
model = YOLO('yolov8n.pt')  # 'n'은 nano 모델을 의미합니다

# 이미지에서 객체 감지 수행
results = model('./car.jpg')

# 결과 시각화
for r in results:
    im_array = r.plot()  # 플롯된 이미지를 numpy 배열로 가져옵니다
    
# 결과 저장 또는 표시
import cv2
cv2.imshow("YOLOv8 Inference", im_array)
cv2.waitKey(0)
cv2.destroyAllWindows()