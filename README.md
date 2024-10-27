# CNN Digit Recognizer 🔢

This repository houses an exciting deep learning project employing Convolutional Neural Networks (CNN) to construct a digit recognizer using the MNIST dataset. The MNIST dataset comprises a vast collection of handwritten digit images.

![DigitRecognizer](/analysis/preview.png)

## Dependencies 🛠️

Ensure you have the following packages installed with the specified versions:

- `numpy`
- `matplotlib`
- `tensorflow`
- `keras`
- `pillow` or `opencv-python`

## Usage 🚀

1. **Clone the repository** to your local machine:

   ```bash
   git clone https://github.com/ZephyrusBlaze/DigitRecognizer.git
   ```

2. **Install required packages**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask server**:

   ```bash
   python server.py
   ```

4. **Access the web interface**:

   Visit `http://localhost:5000` in your web browser.

5. **Draw a digit**:

   In the provided interface, draw a digit, and the trained model will predict the corresponding digit.

🌐 **Alternatively, use the pre-trained model**:

   Access the model at [https://thestrange-007.github.io/DigitRecognizer/](https://thestrange-007.github.io/DigitRecognizer/).

## Model Training 🧠

The repository includes code for training the CNN model using the MNIST dataset. The model architecture comprises convolutional layers, pooling layers, dropout layers, and dense layers. Augmentation techniques are applied to generate augmented images for training.

## License 📜

This project is licensed under the [MIT License](LICENSE).
