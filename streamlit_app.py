import streamlit as st
import pandas as pd
import joblib
import seaborn as sns
import matplotlib.pyplot as plt

# Load the model
model = joblib.load("trained_model.pkl")

# Title
st.title("🌸 Iris Species Predictor")
st.write("Enter the values to predict the Iris species")

# Sidebar Inputs
sepal_length = st.sidebar.slider("Sepal Length", 4.0, 8.0, 5.4)
sepal_width = st.sidebar.slider("Sepal Width", 2.0, 4.5, 3.4)
petal_length = st.sidebar.slider("Petal Length", 1.0, 7.0, 1.3)
petal_width = st.sidebar.slider("Petal Width", 0.1, 2.5, 0.2)

# Prediction Input
input_df = pd.DataFrame({
    'sepal_length': [sepal_length],
    'sepal_width': [sepal_width],
    'petal_length': [petal_length],
    'petal_width': [petal_width]
})

# Display Input
st.subheader("📥 Input Values")
st.write(input_df)

# Prediction
prediction = model.predict(input_df)
st.subheader("🌼 Predicted Iris Species:")
st.success(prediction[0])

# Visualization
st.subheader("📊 Iris Dataset Overview")
df = sns.load_dataset("iris")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="species", ax=ax)
st.pyplot(fig)