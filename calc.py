import tkinter as tk

# Function to update the expression in the input field
def click(button_text):
    current_text = str(entry.get())
    if button_text == "=":
        try:
            # Evaluate the expression and update the input field
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        # Append button text to the input field
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an Entry widget for the expression
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="ridge")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Create buttons and place them on the grid
row = 1
col = 0
for button in buttons:
    if button == 'C':
        tk.Button(root, text=button, command=lambda: click(button), width=5, height=2).grid(row=row, column=col, columnspan=2)
        col += 2
    else:
        tk.Button(root, text=button, command=lambda b=button: click(b), width=5, height=2).grid(row=row, column=col)
        col += 1
        if col > 3:
            col = 0
            row += 1

# Run the application
root.mainloop()