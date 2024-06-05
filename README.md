# Eye Disease Recognition Flask App

## Overview

The Eye Disease Recognition Flask App is a machine learning-powered web application designed to identify various eye diseases from images. This application leverages a deep learning model with an impressive accuracy of 95%. The app can classify eye images into one of the five categories:

- Cataract Disease
- Diabetic Retinopathy Disease
- Glaucoma Disease
- Normal Eye
- Ocular Disease

Additionally, the app includes a feature to collect user messages and store them in an SQL database for further analysis or feedback purposes.

## Features

1. **Disease Classification**: Upload an image of an eye, and the app predicts the disease category.
2. **User Feedback**: Users can submit feedback or queries through a form.
3. **Database Integration**: User messages are stored in a MySQL database.
4. **Detailed Information**: For each prediction, the app provides symptoms, a brief description, and possible treatments.

## Requirements

- Python 3.7 or later
- Flask
- TensorFlow
- NumPy
- PIL (Pillow)
- Werkzeug
- Flask-SQLAlchemy
- MySQL and PyMySQL

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Bilal-Javed-Goraya/Eye-Disease-Recognition.git
    cd Eye-Disease-Recognition
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Setup the database**:
    - Ensure MySQL is installed and running.
    - Create a database named `eye_Disease_data1`.
    - Update the database URI in `app.py`:
      ```python
      app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:yourpassword@localhost/eye_Disease_data1'
      ```
    - Create the database tables by running:
      ```bash
      python
      >>> from app import db
      >>> db.create_all()
      >>> exit()
      ```

4. **Run the app**:
    ```bash
    python app.py
    ```

## Usage

### Home Page

Navigate to `http://localhost:5500/` to access the home page.

### Uploading an Image

1. Click on the "Upload Image" button.
2. Choose an image file with one of the following extensions: `.jpg`, `.jpeg`, `.png`.
3. Click "Submit" to get the prediction results.

### Viewing Prediction Results

After uploading an image, the app will display:

- **Predicted Disease**: The identified eye disease.
- **Description**: A brief description of the disease.
- **Symptoms**: Common symptoms associated with the disease.
- **Treatment Information**: Suggested treatments and medications.

### Submitting a Message

1. Navigate to the "Contact Us" or "Submit Message" section.
2. Fill out the form with your name, email, phone number, and message.
3. Click "Submit" to send your message.

### Example Prediction Result

After a successful prediction, the result page (`predict.html`) will display:

- **Predicted Class**: Diabetic Retinopathy Disease
- **Description**: Diabetic retinopathy is a diabetes complication that affects the eyes. It can cause blindness if left untreated. Symptoms include blurred or distorted central vision and blank spots. Treatment options may include laser therapy, medication, and surgery. Diabetic patients should maintain good blood sugar control and consult an eye specialist.
- **Symptoms**:
  - Blurred or distorted central vision
  - Blank spots
- **Treatment Information**:
  - **Description**: Treatment options may include laser therapy, medication, and surgery. Diabetic patients should maintain good blood sugar control and consult an eye specialist.
  - **Medicines**:
    - Anti-VEGF Injections
    - Steroid Injections
- **Uploaded Image**: The image file uploaded by the user.

## File Structure

- `app.py`: Main Flask application file.
- `eye_disease_model_200.h5`: Pre-trained deep learning model.
- `LICENSE`: License file.
- `README.md`: Readme file.
- `static/`: Static files (CSS, JavaScript, images).
- `templates/`: HTML templates.
- `__pycache__/`: Python cache files.


## Result

### Run the Flask App
![Run App](https://github.com/Bilal-Javed-Goraya/Eye-Disease-Recognition/blob/main/App.JPG)

### Flask App
![Flask App ](https://github.com/Bilal-Javed-Goraya/Eye-Disease-Recognition/blob/main/App1.JPG)

![Flask App ](https://github.com/Bilal-Javed-Goraya/Eye-Disease-Recognition/blob/main/App2.JPG)

![Flask App ](https://github.com/Bilal-Javed-Goraya/Eye-Disease-Recognition/blob/main/App3.JPG)

### Upload Image for Prediction

![Upload Image for Prediction](https://github.com/Bilal-Javed-Goraya/Eye-Disease-Recognition/blob/main/App4.JPG)

### Upload Image from Ocular Disease folder images

![Upload Image from Ocular Disease folder images](https://github.com/Bilal-Javed-Goraya/Eye-Disease-Recognition/blob/main/uploadimage.JPG)
### Prediction
![Prediction](https://github.com/Bilal-Javed-Goraya/Eye-Disease-Recognition/blob/main/pred1.JPG)

![Prediction part 2 Image](https://github.com/Bilal-Javed-Goraya/Eye-Disease-Recognition/blob/main/pred2.JPG)
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any queries or feedback, please contact [2019n10718@gmail.com](mailto:2019n10718@gmail.com).

---

**Thank you for using the Eye Disease Recognition Flask App!**