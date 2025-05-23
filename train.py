import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
from ultralytics import YOLO

# Load a model
# model = YOLO(model="yolov8s.yaml")  # yolov8s
# model = YOLO(model="yolov8s-p2.yaml")  # yolov8s+head
# model = YOLO(model="yolov8s-p2-repvgg.yaml")  # yolov8s+repvgg
model = YOLO(model="yolov8s-drone.yaml")  # yolov8s+repvgg+sf

# model.load('yolov8s.pt')  # 论文未加载预训练权重
# Use the model
model.train(data="VisDrone.yaml", imgsz=640, epochs=300, workers=8, batch=8, cache=True, project='runs/train')
# path = model.export(format="onnx", dynamic=True)  # export the mode l to ONNX format

