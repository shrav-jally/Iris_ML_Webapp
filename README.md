# Iris Species Predictor - Streamlit Deployment

## 🧾 Description
This Streamlit web app allows users to input flower measurements and predicts the species of an Iris flower using a trained RandomForest model.

## ✅ Features
- User-friendly sliders for input
- Prediction displayed instantly
- Scatter plot of original dataset

## 🧠 ML Model
- Trained using the Iris dataset
- RandomForestClassifier from scikit-learn
- Model saved using `joblib`

## 📦 Requirements
- streamlit
- scikit-learn
- pandas
- seaborn
- matplotlib
- joblib

## 🚀 How to Run
```bash
pip install -r requirements.txt
jupyter notebook     # for training
streamlit run streamlit_app.py
```

## 📂 Files
- `model_training.ipynb`: Notebook to train and save model
- `trained_model.pkl`: Saved model
- `streamlit_app.py`: Streamlit web app