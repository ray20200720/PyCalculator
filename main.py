import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""

        self.display = tk.Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4)

        # Define Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            self.create_button(button, row, col)
            col += 1
            if col == 4:
                row += 1
                col = 0

        # Clear Button
        clear_button = tk.Button(root, text='C', padx=10, pady=10, font=("Arial", 12), command=self.clear)
        clear_button.grid(row=row, column=col, columnspan=4, sticky="nsew")

    def create_button(self, value, row, col):
        button = tk.Button(self.root, text=value, padx=10, pady=10, font=("Arial", 12), command=lambda: self.on_button_click(value))
        button.grid(row=row, column=col, sticky="nsew")

    def on_button_click(self, value):
        if value == "=":
            try:
                self.expression = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(0, self.expression)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expression = ""
        else:
            self.expression += value
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
