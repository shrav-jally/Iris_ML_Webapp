# Iris Species Predictor – Streamlit Deployment

## Description
A simple Streamlit web application that predicts the species of an Iris flower based on user-provided measurements. It uses a pre-trained Random Forest model built on the Iris dataset.

## Features
- Interactive sliders for sepal and petal measurements
- Instant prediction display
- Visual representation of the Iris dataset with a scatter plot

## Machine Learning Model
- Dataset: Iris dataset from scikit-learn
- Model: RandomForestClassifier
- Model persistence: Saved using `joblib`

## Requirements
- streamlit  
- scikit-learn  
- pandas  
- seaborn  
- matplotlib  
- joblib  

## How to Run
1. Install dependencies:
pip install -r requirements.txt
jupyter notebook
streamlit run streamlit_app.py

