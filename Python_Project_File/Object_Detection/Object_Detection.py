import pathlib
import cv2
import torch

pathlib.PosixPath = pathlib.WindowsPath

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    result = model(frame, size=640)
    df = result.pandas().xyxy[0]
    for ind in df.index:
        x1, y1 = int(df['xmin'][ind]), int(df['ymin'][ind])
        x2, y2 = int(df['xmax'][ind]), int(df['ymax'][ind])
        label = df['name'][ind]
        conf = df['confidence'][ind]  # Convert to string
        data = label + str(conf.round(decimals=2))

        if float(conf.round(decimals=2)) >= 0.60:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2 .putText(frame, data, (x1, y1 - 5), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

    # Display the frame with bounding boxes
    cv2.imshow('Video', frame)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
