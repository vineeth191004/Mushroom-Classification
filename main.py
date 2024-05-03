from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the saved model and PCA object
saved_model = pickle.load(open('Data_saved.pickle', 'rb'))
saved_pca = pickle.load(open('Data_pca.pickle', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def predict():
    # Get form data
    form_data = request.form.to_dict()

    # Convert form data to numpy array
    input_data = np.zeros((1, 22))  # Initialize with the correct number of features
    for key, value in form_data.items():
        # Check if the key is a valid integer
        if not key.isdigit():
            # If not, skip this value
            continue
        
        # Convert the key to integer
        key_int = int(key)

        # Assign the integer value to the input data
        input_data[0, key_int] = int(value)

    # Transform the input data using PCA
    input_data_pca = saved_pca.transform(input_data)

    # Make prediction
    prediction = saved_model.predict(input_data_pca)[0]

    # Map prediction to class label
    class_label = "Poisonous" if prediction == 1 else "Edible"

    return render_template('result.html', prediction=class_label)

if __name__ == '__main__':
    app.run(debug=True)
