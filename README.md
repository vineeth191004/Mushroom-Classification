## Mushroom Classification and Flask Deployment
This project involves predicting whether a given mushroom is edible or poisonous based on various features such as cap shape, cap color, gill size, and habitat. The machine learning model is deployed using Flask, allowing users to interact with the model via a web interface.

# Mushroom Classification
Mushroom classification involves the following steps:

1. **Data Collection**
Gather data containing various attributes of mushrooms, including their edibility.

2. **Data Preprocessing**
Handle missing values, encode categorical variables using techniques like Label Encoding, and normalize/standardize numerical features.

3. **Feature Selection/Reduction**
Use techniques like Principal Component Analysis (PCA) to reduce the dimensionality of the dataset while retaining the most informative features.

4. **Model Training**
Train a machine learning model, such as a RandomForestClassifier, on the preprocessed dataset to learn patterns associated with edible and poisonous mushrooms.

5. **Model Evaluation**
Evaluate the model's performance using metrics like accuracy, precision, and recall on a test set to ensure it generalizes well to unseen data.

6. **Model Saving**
Save the trained model and any preprocessing objects (e.g., PCA) to disk using libraries like pickle for later use.

# Flask Deployment
Flask is a lightweight web framework for Python that can be used to deploy machine learning models as web applications. Here is how you can deploy the mushroom classification model using Flask:

1. **Setup Flask Application**
Create a Flask application with the necessary route(s) to handle user requests.

2. **Load Model and Preprocessing Objects**
Load the saved machine learning model and preprocessing objects (e.g., PCA) when the Flask application starts.

3. **Create HTML Forms**
Develop HTML forms to accept user inputs for the various mushroom attributes.

4. **Handle User Inputs**
Capture the user inputs from the HTML form and preprocess them to match the format expected by the model.

5. **Make Predictions**
Pass the preprocessed inputs to the model to get predictions. Map the prediction output to a human-readable format (e.g., edible or poisonous).

6. **Display Results**
Return the prediction results to the user via an HTML page.

# File Structure

.
├── app.py                     # Flask application file
├── Data_pca.pickle            # Saved PCA object
├── Data_saved.pickle          # Saved machine learning model
├── templates
│   ├── index.html             # HTML form for user input
│   └── result.html            # HTML page for displaying prediction results
└── static
    ├── style.css              # CSS for styling the HTML pages
    ├── edible_mushroom.jpg    # Image displayed for edible mushrooms
    └── poisonous_mushroom.jpg # Image displayed for poisonous mushrooms
