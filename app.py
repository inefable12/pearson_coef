import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Diagrama de Calor - Pearson", layout="wide")

# Título de la aplicación
st.title("Diagrama de Calor del Coeficiente de Pearson")

# Descripción
st.write("""
Esta aplicación genera un diagrama de calor que muestra los coeficientes de Pearson entre las columnas de una tabla. 
Por defecto, se utiliza una tabla generada aleatoriamente con 10 atributos.
""")

# Generar datos aleatorios
np.random.seed(42)  # Semilla para reproducibilidad
data = pd.DataFrame(
    np.random.rand(100, 10),  # 100 filas, 10 columnas
    columns=[f"Atributo {i+1}" for i in range(10)]
)

# Mostrar la tabla de datos
st.subheader("Tabla de datos (muestra las primeras 10 filas)")
st.dataframe(data.head(10))

# Calcular la matriz de correlación
correlation_matrix = data.corr()

# Generar el diagrama de calor
st.subheader("Diagrama de Calor del Coeficiente de Pearson")
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
plt.title("Diagrama de Calor del Coeficiente de Pearson")
st.pyplot(fig)

# Nota final
st.info("Sube este archivo a un repositorio de GitHub para ejecutarlo en Streamlit Cloud.")
