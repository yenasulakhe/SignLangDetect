from flask import Flask, render_template, Response
import cv2
import time

app = Flask(__name__)

# Initialize the webcam
cap = cv2.VideoCapture(0)

@app.route('/')
def home():
    return render_template('index.html')

def gen_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Process frame for sign language detection here
            # Example: detected_sign = detect_sign(frame)
            detected_sign = "No sign detected"  # Placeholder for the result

            # Convert the frame to JPEG to send it to the client
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_sign')
def get_sign():
    # This should return the sign detection result
    # For example, you can send the detected sign through an API or update the front-end dynamically
    return "No sign detected"  # Placeholder

if __name__ == '__main__':
    app.run(debug=True)


