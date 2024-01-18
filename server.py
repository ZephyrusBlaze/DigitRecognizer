from flask import Flask, render_template, request
from PIL import Image
import io
import base64
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

model = load_model("analysis/digits_classifier_cnn.h5")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_image', methods=['POST'])
def predict_image():
    # Get the image data from the request
    data = request.get_json()
    canvas_data_url = data["image"]
    canvas_data = base64.b64decode(canvas_data_url.split(',')[1])

    # Use PIL to open the image
    with Image.open(io.BytesIO(canvas_data)) as img:
        img = img.convert('L')
        img = img.resize((28, 28))

        # Save the image (optional)
        img.save("digit.png")

        nparr = np.array(img)

    img = nparr / 255.0

    # Reshape the image to match the input shape of the model
    img = img.reshape(1, 28, 28, 1)

    probabilities = np.round(model.predict(img)[0] * 100)

    return f"{probabilities.tolist()}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
