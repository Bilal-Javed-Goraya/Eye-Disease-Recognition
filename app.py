from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
import os
from PIL import Image
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)

model = load_model('eye_disease_model_200.h5')
# model = load_model('weights.hdf5')
@app.route('/')
def index_view():
    return render_template('index.html')

ALLOWED_EXT = set(['jpg', 'jpeg', 'png'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

def read_image(filename):
    img = Image.open(filename)
    img = img.resize((256, 256))
    x = np.array(img)
    x = x / 255.0  # Normalize the pixel values to the range [0, 1]
    return x

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:RP-20EE-407%%++@localhost/eye_Disease_data1'

# Replace 'username', 'password', 'localhost', and 'database_name' with your MySQL credentials
db = SQLAlchemy(app)

class UserMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    message = db.Column(db.Text)
    timestamp = db.Column(db.String(100))




@app.route('/submit_message', methods=['POST'])
def submit_message():
    if request.method == 'POST':
        # Extract form data from the request
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # Get the current date and time
        current_datetime = datetime.now()

        # Create a new UserMessage instance with the current datetime and save it to the database
        new_message = UserMessage(name=name, email=email, phone=phone, message=message, timestamp=current_datetime)
        db.session.add(new_message)
        db.session.commit()

        # Optionally, you can provide a success message or redirect to a thank-you page
        return "Message submitted successfully"

    # Handle GET requests (e.g., direct access to /submit_message)
    return "Invalid request"


# Create the database tables (if they don't exist)
with app.app_context():
    db.create_all()



@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    
    if file and allowed_file(file.filename):
        filename = file.filename
        file_path = os.path.join('static/prid_images', filename)
        file.save(file_path)
        img = read_image(file_path)
        img = img.reshape((1, 256, 256, 3))  # Reshape the input image to match the model's input shape
        class_prediction = model.predict(img)
        classes_x = np.argmax(class_prediction, axis=1)   
        
        class_names = [
            "Cataract Disease",
            "Diabetic Retinopathy Disease",
            "Glaucoma Disease",
            "Normal Eye",
            "Ocular Disease",
            "Retina Disease"
        ]
        
        predicted_class_name = class_names[classes_x[0]]
        
        class_symptoms = [
            ["Blurred vision", "Double vision", "Sensitivity to light", "Difficulty seeing at night"],
            ["Blurred or distorted central vision", "Blank spots"],
            ["Tunnel vision", "Severe eye pain", "Blurred vision", "Halos around lights"],
            [],
            ['Blurry Vision', 'Eye Pain','Redness','Sensitivity to Light (Photophobia)','Floaters and Flashes'],
            ["Blurry or distorted central vision", "Seeing floaters", "Dark spots"]
        ]
        
        predicted_class_symptoms = class_symptoms[classes_x[0]]
        
        class_descriptions = [
            "Cataract disease is a clouding of the eye's lens that affects vision. It is usually caused by aging and may lead to blurry vision, sensitivity to light, and more. Cataract surgery is the most common treatment, where the cloudy lens is removed and replaced with an artificial one. Consult an ophthalmologist for proper diagnosis and treatment.",
            "Diabetic retinopathy is a diabetes complication that affects the eyes. It can cause blindness if left untreated. Symptoms include blurred or distorted central vision and blank spots. Treatment options may include laser therapy, medication, and surgery. Diabetic patients should maintain good blood sugar control and consult an eye specialist.",
            "Glaucoma is a group of eye diseases that can cause vision loss and blindness. It often has no early symptoms but may lead to tunnel vision, severe eye pain, and blurred vision. Treatment involves reducing intraocular pressure with eye drops, laser treatment, or surgery. Regular eye check-ups are important.",
            "Normal eye without any detected diseases.",
            "Ocular diseases encompass a wide range of medical conditions and disorders that affect the eyes and their various components. These conditions can impact vision and eye health, and they can arise from multiple causes, including genetic factors, infections, injuries, systemic diseases, and aging. Ocular diseases can vary in severity from mild discomfort to severe vision impairment or even blindness.",
            "Retina disease affects the retina, the layer of tissue at the back of the inner eye. It may cause blurry or distorted central vision, seeing floaters, or dark spots. Treatment depends on the specific condition and may include medication, laser therapy, or surgery. Consult an eye specialist."
        ]
        
        predicted_class_description = class_descriptions[classes_x[0]]

        treatment_info = {
            "Cataract Disease": {
                "description": "Cataract surgery is the most common treatment, where the cloudy lens is removed and replaced with an artificial one. Consult an ophthalmologist for proper diagnosis and treatment.",
                "medicines": ["Artificial Tears", "Anti-inflammatory Eye Drops"]
            },
            "Diabetic Retinopathy Disease": {
                "description": "Treatment options may include laser therapy, medication, and surgery. Diabetic patients should maintain good blood sugar control and consult an eye specialist.",
                "medicines": ["Anti-VEGF Injections", "Steroid Injections"]
            },
            "Glaucoma Disease": {
                "description": "Treatment involves reducing intraocular pressure with eye drops, laser treatment, or surgery. Regular eye check-ups are important.",
                "medicines": ["Prostaglandin Analogues", "Beta-Blockers"]
            },
            "Normal Eye": {
                "description": "No specific treatment needed for a normal eye.",
                "medicines": []
            },
            "Ocular Disease": {
                "description": "Treatment varies depending on the specific ocular disease. Consult an eye specialist for proper diagnosis and treatment.",
                "medicines": ["Specific Medications Depending on the Disease"]
            },
            "Retina Disease": {
                "description": "Treatment depends on the specific condition and may include medication, laser therapy, or surgery. Consult an eye specialist.",
                "medicines": ["Anti-VEGF Injections", "Corticosteroids"]
            }
        }

        return render_template('predict.html', 
                               predicted_class_name=predicted_class_name,
                               predicted_class_description=predicted_class_description,
                               predicted_class_symptoms=predicted_class_symptoms,
                               treatment_info=treatment_info,
                               user_image=file_path)
    else:
        return "Unable to read the file. Please check file extension"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=5500)
