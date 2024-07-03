# Diabetes Prediction Web App

This web application predicts the likelihood of diabetes based on input features using a machine learning model. The model has been trained using data on various health metrics.

---

## Features

- Predicts the probability of diabetes based on user inputs.
- Simple and intuitive interface built with Streamlit.
- Integration with a trained machine learning model.

---

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/diabetes-prediction-app.git
    cd diabetes-prediction-app
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    Ensure all dependencies from `requirements.txt` are installed.

---

## Setup

1. **Download the trained model:**

    Place your trained machine learning model (`trained_model.sav`) in the root directory of the project.

---

## Running the App

1. **Start the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

    This command launches a local web server and opens the app in your default web browser.

2. **Input Patient Details:**

    - Enter values for the following health metrics:
        - Number of Pregnancies
        - Glucose level
        - Blood Pressure value
        - Skin Thickness value
        - Insulin Level
        - BMI value
        - Diabetes Pedigree Function value
        - Age of the Person

3. **Predict Diabetes:**

    - Click on the "Diabetes Test Result" button to see the prediction.

---

## File Structure

- `app.py`: Main application file containing Streamlit interface code.
- `model.py`: Code for loading the trained machine learning model.
- `requirements.txt`: List of Python dependencies.
- `trained_model.sav`: Placeholder for the trained machine learning model file.

---

## Contributing

Contributions are welcome! If you want to contribute to this project, please fork the repository and create a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

