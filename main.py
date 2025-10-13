import cv2
import flask
from flask_cors import CORS

PORT = 8192

app = flask.Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

camera = cv2.VideoCapture(0)

@app.route("/stream")
def stream():
    def generate_frames():
        while True:
            success, frame = camera.read()
            if not success:
                continue
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    return flask.Response(generate_frames(),
                          mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)