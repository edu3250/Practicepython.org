import tkinter as tk

def click_boton(valor):
    entrada_actual = entrada.get()
    entrada.set(entrada_actual + str(valor))

def limpiar_entrada():
    entrada.set("")

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.set(str(resultado))
    except Exception as e:
        entrada.set("Error")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora")

# Variable para la entrada
entrada = tk.StringVar()

# Campo de entrada
entrada_texto = tk.Entry(ventana, textvariable=entrada, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify="right")
entrada_texto.grid(row=0, column=0, columnspan=4)

# Botones
botones = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('C',5,0)
]

for (texto, fila, columna) in botones:
    if texto == "=":
        boton = tk.Button(ventana, text=texto, padx=20, pady=20, font=("Arial", 14), command=calcular)
    elif texto == "C":
        boton = tk.Button(ventana, text=texto, padx=20, pady=20, font=("Arial", 14), command=limpiar_entrada)
        boton.grid(row=fila, column=columna, columnspan=4, sticky="we")  # "C" ocupa toda la fila
        continue
    else:
        boton = tk.Button(ventana, text=texto, padx=20, pady=20, font=("Arial", 14), command=lambda t=texto: click_boton(t))
    
    boton.grid(row=fila, column=columna)

# Ejecutar la ventana
ventana.mainloop()
