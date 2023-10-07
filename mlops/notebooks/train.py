from ultralytics import YOLO

# Initialize model
yolo_model = YOLO("yolov8n.pt")

costumdata = "C:/Users/ra78lof/yolov5/Mydataset/customdata.yaml"  # dataset.yaml
# Run Train
yolo_model.train(data="C:/Users/ra78lof/yolov5/data/VisDrone.yaml", epochs=50)

# customdata.yaml

# debug
print(yolo_model)
