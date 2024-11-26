
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Configuración inicial
st.title("Optimización de Funciones")
st.markdown("Este aplicativo muestra los resultados de ejercicios relacionados con optimización de funciones.")

# Función 1: Verifica los mínimos locales y globales
def f1(x):
    return x**2 - 4*x + 5

st.header("1. Verificación de mínimos locales y globales")
x_vals = np.linspace(-1, 4, 500)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_vals, f1(x_vals), label="f(x) = x^2 - 4x + 5")
ax.scatter([2], [f1(2)], color="red", label="Mínimo global en x=2")
ax.scatter([0], [f1(0)], color="blue", label="Valor en x=0")
ax.legend()
ax.grid()
ax.set_title("Función cuadrática y sus puntos críticos")
st.pyplot(fig)

# Función 2: Dibuja la función |x|
def f2(x):
    return np.abs(x)

st.header("2. Gráfica de la función f(x) = |x|")
x_vals = np.linspace(-2, 2, 500)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_vals, f2(x_vals), label="f(x) = |x|")
ax.scatter([0], [f2(0)], color="red", label="Mínimo global en x=0")
ax.legend()
ax.grid()
ax.set_title("Función f(x) = |x|")
st.pyplot(fig)

# Función 3: Teorema de Weierstrass con f(x) = sin(x)
def f3(x):
    return np.sin(x)

st.header("3. Teorema de Weierstrass con f(x) = sin(x) en [0, π]")
x_vals = np.linspace(0, np.pi, 500)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_vals, f3(x_vals), label="f(x) = sin(x)")
ax.scatter([np.pi], [f3(np.pi)], color="red", label="Mínimo global en x=π")
ax.scatter([np.pi/2], [f3(np.pi/2)], color="green", label="Máximo global en x=π/2")
ax.legend()
ax.grid()
ax.set_title("Función f(x) = sin(x) en [0, π]")
st.pyplot(fig)

# Función 4: Función en dos variables
st.header("4. Función f(x, y) = x^2 + y^2")
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
x, y = np.meshgrid(x, y)
z = x**2 + y**2

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8)
ax.scatter(0, 0, 0, color="red", s=50, label="Mínimo global en (0,0)")
ax.set_title("Función f(x, y) = x^2 + y^2")
ax.legend()
st.pyplot(fig)

# Función 5: Ejemplo con múltiples mínimos globales
def f5(x):
    return x**4 - x**2

st.header("5. Ejemplo con múltiples mínimos globales")
x_vals = np.linspace(-2, 2, 500)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_vals, f5(x_vals), label="f(x) = x^4 - x^2")
ax.scatter([0, -1/np.sqrt(2), 1/np.sqrt(2)], [f5(0), f5(-1/np.sqrt(2)), f5(1/np.sqrt(2))], 
           color="red", label="Mínimos globales")
ax.legend()
ax.grid()
ax.set_title("Función f(x) = x^4 - x^2")
st.pyplot(fig)
