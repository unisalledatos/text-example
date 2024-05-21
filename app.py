import streamlit as st
import numpy as np
import pickle
import sklearn

def tokenizer(text):
  return text.split()

st.title("Predict reviews' sentiment")

review = st.text_input("Ingrese la reseña: ")
review_array = np.array([review])

with open("model.pickle", "rb") as f:
    model = pickle.load(f)

if st.button("Predicción"):
    pred = model.predict(review_array)[0]

    if pred == 0:
        st.write("Negativa")
    else:
        st.write("Positiva")


