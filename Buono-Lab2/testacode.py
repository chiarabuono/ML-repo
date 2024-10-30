import matplotlib.pyplot as plt

# Dati di esempio
x_points = [1, 2, 3, 4, 5]
y_points = [2, 3, 5, 7, 11]

# Coefficiente angolare e intercetta per la retta (esempio: y = 2x + 1)
m = 2
b = 1
x_line = [0, 6]  # Estensione dell'asse x per la linea
y_line = [m * x + b for x in x_line]  # Calcolo dei valori y per la linea

# Grafico
plt.figure(figsize=(8, 6))

# Traccia i punti
plt.scatter(x_points, y_points, color='blue', label='Punti', s=50)

# Traccia la linea
plt.plot(x_line, y_line, color='red', label='Linea y=2x+1')

# Aggiungi etichette e legenda
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Grafico di una linea e un set di punti')

# Mostra il grafico
plt.show()
