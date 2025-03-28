import cv2
from Omkar_model import detect_sign  # Import the detection function from Omkarbagad's repo
from Adi_model import predict       # Import the prediction function from Adi3220's repo
import cv2

cap = cv2.VideoCapture(0)  # Initialize webcam (0 is usually the default)

while cap.isOpened():
    ret, frame = cap.read()  # Capture each frame from the webcam
    if not ret:
        break
    
    # Process the frame here (later we'll add the detection code)
    
    cv2.imshow("Real-Time Sign Language Detection", frame)

    # Break if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
