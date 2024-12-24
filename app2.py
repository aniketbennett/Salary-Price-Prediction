import streamlit as st
import pickle
import numpy as np

# Load the saved model
model = pickle.load(open(r"C:\Users\gs705\Desktop\Work\Naresh- IT\Data Analytics\Project\Project-5 (Streamlit)\linear_regression_model.pkl", 'rb'))

# Set the title of the Streamlit app
st.set_page_config(page_title="Salary Prediction App", layout="centered")

# Apply custom styling
st.markdown(
    """
    <style>
    body {
        background-color: #f7f9fc;
        color: #333333;
        font-family: Arial, sans-serif;
    }
    .title {
        color: #4A90E2;
        text-align: center;
        font-size: 2.5em;
        margin-top: 20px;
        font-weight: bold;
    }
    .description {
        color: #5D6D7E;
        text-align: center;
        font-size: 1.2em;
        margin-bottom: 30px;
    }
    .input-container {
        margin: 0 auto;
        text-align: center;
        font-size: 1.1em;
    }
    .button {
        text-align: center;
        margin-top: 20px;
    }
    .result {
        text-align: center;
        color: #27AE60;
        font-size: 1.5em;
        margin-top: 20px;
        font-weight: bold;
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        font-size: 0.9em;
        color: #7F8C8D;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='title'>Salary Prediction App</div>", unsafe_allow_html=True)

# Add a brief description
st.markdown("<div class='description'>Predict the salary based on years of experience using a linear regression model.</div>", unsafe_allow_html=True)

# Add input widget for user to enter years of experience
st.markdown("<div class='input-container'>", unsafe_allow_html=True)
years_experience = st.number_input(
    "Enter Years of Experience:", 
    min_value=0.0, 
    max_value=50.0, 
    value=1.0, 
    step=0.5
)
st.markdown("</div>", unsafe_allow_html=True)

# When the button is clicked, make predictions
if st.button("Predict Salary"):
    # Make a prediction using the trained model
    experience_input = np.array([[years_experience]])  # Convert the input to a 2D array for prediction
    prediction = model.predict(experience_input)

    # Display the result
    st.markdown(f"<div class='result'>The predicted salary for {years_experience} years of experience is: ${prediction[0]:,.2f}</div>", unsafe_allow_html=True)

# Display additional information about the model
st.markdown("<div class='footer'>This model was trained using a dataset of salaries and years of experience.<br>Built by Aniket Singh.</div>", unsafe_allow_html=True)
