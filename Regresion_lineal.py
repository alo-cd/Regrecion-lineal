import numpy as np
import matplotlib.pyplot as plt

def regresion_lineal(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x_squared = np.sum(x**2)
    sum_xy = np.sum(x*y)
    
    # Calculando los coeficientes de la regresión lineal
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    b = (sum_y - m * sum_x) / n
    # Creando el resultado en texto
    resultado_texto = f"La función de regresión lineal es: y = {m:.2f}x + {b:.2f}"
    
    return m, b, resultado_texto

def main():
    # Pedir al usuario que ingrese los datos
    expresion = input("Ingrese la expresión de la función (usando 'x' como variable independiente): ")
    x_values = np.array(eval(input("Ingrese los valores de x separados por comas: ")))
    y_values = np.array(eval(input("Ingrese los valores de y separados por comas: ")))
    
    # Ajustar la función utilizando regresión lineal
    m, b, resultado_texto = regresion_lineal(x_values, y_values)
    print(resultado_texto)  # Mostrar el resultado en texto
    
    # Generar la línea de regresión
    x_regresion = np.linspace(min(x_values), max(x_values), 100)
    y_regresion = m * x_regresion + b
    
    # Graficar los datos originales y la línea de regresión
    plt.scatter(x_values, y_values, label='Datos originales')
    plt.plot(x_regresion, y_regresion, color='red', label='Línea de regresión')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Regresión Lineal de ' + expresion)
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
