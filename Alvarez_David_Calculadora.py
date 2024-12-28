import tkinter as tk     # Importar tkinter para la interfaz gráfica

# Alvarez_David_Tarea_04_Calculadora

# Desarrollar una aplicación que funcione como una calculadora básica, 
# permitiendo realizar operaciones aritméticas simples 
# como suma, resta, multiplicación y división. 
# La aplicación debe tener una interfaz intuitiva y funcional, 
# que permita a los usuarios ingresar números y operar fácilmente.

class Calculadora(tk.Tk):

    def __init__(self):
        super().__init__()  # Inicializar la clase
        self.ventana_calculadora()    # Llamar al método de la ventana
        self.botones()  # Llamar al método de los botones

    def ventana_calculadora(self):  # Configuración de la ventana
        self.title('Calculadora')
        self.configure(bg='gray7')
        self.geometry('310x440')

    def botones(self):      # Crear los botones de la calculadora y asignar sus funcionalidades
        
        # Mostrar la operación solicitada
        self.mostrar_operacion = tk.Label(self, text="", font=('Arial', 16), fg='white', bg='gray7', justify='right', width=20, anchor='e')
        self.mostrar_operacion.grid(row=0, columnspan=4, padx=10, pady=10, sticky='e')

        # Pantalla de operación
        self.entry = tk.Entry(self, width=10, font=('Arial', 40), bd=1, fg='white', bg='gray', justify='right')
        self.entry.grid(row=1, column=0, columnspan=4,
                        padx=5, pady=5)

        # Botones
        buttons = [
            '', 'C', '<', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '+',
            '1', '2', '3', '-',
            '0', '.', '='
        ]

        row_val = 2   # Fila inicial de los botones
        col_val = 0   # Columna inicial de los botones
         
        for button in buttons:    # Ubicar los botones
            
            color_fondo = 'SkyBlue3' if button in ['','=', '*', '/', '-', '+', 'C', '<'] else 'gray'


            if button == '=':
                tk.Button(self, text=button, width=17, height=2, command=lambda button=button: self.click(button), bg=color_fondo, fg='white', relief='flat', pady=5, padx=5).grid(row=row_val, column=col_val, columnspan=2, pady=5)
                col_val += 1
            else:
                tk.Button(self, text=button, width=6, height=2, command=lambda button=button: self.click(button), bg=color_fondo, fg='white', relief='flat', pady=5, padx=5).grid(row=row_val, column=col_val, pady=5)
                col_val += 1

            # Si la columna es mayor que 3, se mueve a la siguiente fila
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click(self, valor):  # Maneja las funcionalidades cuando se presiona un botón
        
        if valor == '=': # Evalúa la expresión ingresada
            try:
                operacion = self.entry.get()                    # Obtener la expresión ingresada por el usuario
                result = eval(operacion)                        # Evaluar la expresión (La función eval() en Python evalúa una cadena de texto como una expresión de Python y devuelve su resultado, permitiendo ejecutar dinámicamente operaciones o código contenido en esa cadena)
                self.entry.delete(0, tk.END)                    # Borrar el contenido de la caja de entrada
                self.entry.insert(tk.END, str(result))          # Insertar el resultado en la caja de entrada
                op_label = operacion + " " + valor              # Mostrar la operación completa en el label
                self.mostrar_operacion.config(text=op_label)    # Actualizar el label con la operación
            
            except Exception:   # Si hay errores                     
                self.entry.delete(0, tk.END)                                 # Borrar la caja de entrada
                self.entry.insert(tk.END, "Error")                           # Mostrar "Error" en la caja de entrada
                self.mostrar_operacion.config(text="")                       # Limpiar label de mostrar operación
                self.after(500, lambda: self.entry.delete(0, tk.END))        # Limpiar Error del entry

        elif valor == 'C':      # Borra la pantalla de entrada
            self.entry.delete(0, tk.END)                        # Limpiar la caja de entrada
            self.mostrar_operacion.config(text="")              # Limpiar label de mostrar operación
        
        elif valor == '<':      # Elimina el último carácter de la entrada.
            op_ingresada = self.entry.get()            # Obtener el texto actual de la caja de entrada
            
            if op_ingresada:                                        # Si hay texto en la caja
                new_op = op_ingresada[:-1]                          # Eliminar el último carácter
                self.entry.delete(0, tk.END)                        # Borrar la caja de entrada
                self.entry.insert(tk.END, new_op)                   # Insertar el texto actualizado
                self.mostrar_operacion.config(text=new_op + " ")    # Actualizar el label de mostrar operación
        
        else:
            op_ingresada = self.entry.get()                      # Obtener el texto actual de la caja de entrada
            self.entry.delete(0, tk.END)                         # Borrar la caja de entrada
            self.entry.insert(tk.END, op_ingresada + valor)      # Agregar el nuevo valor al entry
            
        self.entry.xview_moveto(1)        # Mantener el texto visible sin desplazarlo

# Método principal para iniciar la calculadora
if __name__ == "__main__":
    app = Calculadora()      # Crear una instancia de la clase Calculadora
    app.mainloop()