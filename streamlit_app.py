# -*- coding: utf-8 -*-
"""Rol de Género.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O-M_A-o-bYGV9L5Bp0TzTxTTFWn2vrLg
"""

import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Title of the app
st.title("Red Neuronal Artificial [CDMX]| Encuesta Nacional sobre la Dinámica de las Relaciones en los Hogares (ENDIREH) 2021")

st.image("URC.png", caption="UST-URC Universidad Rosario Castellanos", width=200)

# Cargar los datos desde el CSV en GitHub

url = 'https://github.com/Alexramsilva/rol_genero/blob/main/MM.csv'

# Cargar el conjunto de datos
df=pd.read_csv(url, low_memory=False)

# Definir las preguntas y las opciones para los menús desplegables
questions = {
    'P6_1_1': '1. ¿Quién cree usted que debe ser responsable del cuidado de los hijos(as), de las personas enfermas y ancianas?',
    'P6_1_2': '2. ¿Quién cree usted que debe ganar más salario en el trabajo?',
    'P6_1_3': '3. ¿Quién cree usted que debe ser el responsable de las tareas de la casa?',
    'P6_1_4': '4. ¿Quién cree usted que debe ser el responsable de traer dinero para la casa?',
    'P6_1_5': '5. ¿Quién cree usted que tiene mayor capacidad para trabajar y/o estudiar?',
    'P6_2_1': '1. ¿Está usted de acuerdo en que hombres y mujeres tienen el mismo derecho a salir por las noches a divertirse?',
    'P6_2_2': '2. ¿Está usted de acuerdo en que las mujeres que tienen hijos(as) trabajen, aún si no tienen necesidad de hacerlo?'
}

options = {
    'P6_1_1': ['La mujer', 'El hombre', 'Ambos'],
    'P6_1_2': ['La mujer', 'El hombre', 'Deben ganar lo mismo'],
    'P6_1_3': ['La mujer', 'El hombre', 'Ambos'],
    'P6_1_4': ['La mujer', 'El hombre', 'Ambos'],
    'P6_1_5': ['La mujer', 'El hombre', 'Ambos tienen la misma capacidad'],
    'P6_2_1': ['Sí (de acuerdo)', 'No (en desacuerdo)'],
    'P6_2_2': ['Sí (de acuerdo)', 'No (en desacuerdo)']
}

# Interfaz de usuario en Streamlit
st.title('Predicción con Red Neuronal')
st.write('Seleccione sus respuestas a las preguntas para predecir un resultado:')

# Diccionario para almacenar las respuestas seleccionadas
user_responses = {}

for key, question in questions.items():
    user_responses[key] = st.selectbox(question, options[key])

# Convertir las respuestas seleccionadas a un dataframe
response_df = pd.DataFrame([user_responses])


# Preprocesar los datos
X = df[['P6_1_1','P6_1_2','P6_1_3','P6_1_4','P6_1_5','P6_2_1', 'P6_2_2']]  # Reemplaza 'Variable de Predicción' con la columna dependiente
y = df[['Y']]  # Ajusta según tu CSV


# Separar los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalado de características
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Crear el modelo de red neuronal
model = Sequential()
model.add(Dense(16, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))  # Cambia según el tipo de salida (clasificación o regresión)

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, verbose=0)

# Realizar predicción con las respuestas del usuario
user_responses_scaled = scaler.transform(response_df)
prediction = model.predict(user_responses_scaled)

# Mostrar el resultado de la predicción
st.write(f'Predicción: {prediction[0][0]:.2f}')