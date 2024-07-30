from ultralytics import YOLO

# 모델 생성
model = YOLO('yolov8n.yaml')  # 'n'은 nano 모델, 다른 크기도 선택 가능

# 학습 시작
if __name__ == '__main__':
    results = model.train(data='./datasets/data.yaml', epochs=100, imgsz=640)