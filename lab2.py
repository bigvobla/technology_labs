import tkinter as tk
from tkinter import messagebox

class MatrixHandler:
    def __init__(self):
        self.num_rows = 0
        self.num_cols = 0
        self.matrix = []

    def input_matrix(self, num_rows, num_cols, coefficients):
        if num_rows <= 0 or num_cols <= 0 or len(coefficients) != num_rows * num_cols:
            messagebox.showerror("Input Error", "Invalid input dimensions or coefficients")
            return

        self.num_rows = num_rows
        self.num_cols = num_cols
        self.matrix = [coefficients[i:i+num_cols] for i in range(0, len(coefficients), num_cols)]

    def sort_rows(self):
        self.matrix.sort()

    def sort_cols(self):
        self.matrix = [list(row) for row in zip(*self.matrix)]
        self.matrix.sort()
        self.matrix = [list(row) for row in zip(*self.matrix)]

    def replace_element(self, row, col, new_value):
        if 0 <= row < self.num_rows and 0 <= col < self.num_cols:
            self.matrix[row][col] = new_value
        else:
            messagebox.showerror("Replace Error", "Invalid row or column index")

    def search_element(self, value):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self.matrix[i][j] == value:
                    return (i, j)
        return None

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

class MatrixApp:
    def __init__(self, root):
        self.root = root
        self.matrix_handler = MatrixHandler()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Number of rows:").grid(row=0, column=0)
        self.num_rows_entry = tk.Entry(self.root)
        self.num_rows_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Number of columns:").grid(row=1, column=0)
        self.num_cols_entry = tk.Entry(self.root)
        self.num_cols_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Coefficients (comma-separated):").grid(row=2, column=0)
        self.coefficients_entry = tk.Entry(self.root)
        self.coefficients_entry.grid(row=2, column=1)

        tk.Button(self.root, text="Input Matrix", command=self.input_matrix).grid(row=3, column=0, columnspan=2)
        tk.Button(self.root, text="Sort Rows", command=self.sort_rows).grid(row=4, column=0, columnspan=2)
        tk.Button(self.root, text="Sort Columns", command=self.sort_cols).grid(row=5, column=0, columnspan=2)
        tk.Button(self.root, text="Replace Element", command=self.replace_element).grid(row=6, column=0, columnspan=2)
        tk.Button(self.root, text="Search Element", command=self.search_element).grid(row=7, column=0, columnspan=2)
        tk.Button(self.root, text="Display Matrix", command=self.display_matrix).grid(row=8, column=0, columnspan=2)

    def input_matrix(self):
        num_rows = int(self.num_rows_entry.get())
        num_cols = int(self.num_cols_entry.get())
        coefficients = list(map(int, self.coefficients_entry.get().split(',')))

        self.matrix_handler.input_matrix(num_rows, num_cols, coefficients)

    def sort_rows(self):
        self.matrix_handler.sort_rows()

    def sort_cols(self):
        self.matrix_handler.sort_cols()

    def replace_element(self):
        row = int(input("Enter the row index: "))
        col = int(input("Enter the column index: "))
        new_value = int(input("Enter the new value: "))

        self.matrix_handler.replace_element(row, col, new_value)

    def search_element(self):
        value = int(input("Enter the value to search: "))
        result = self.matrix_handler.search_element(value)

        if result:
            messagebox.showinfo("Search Result", f"Element found at row {result[0]}, column {result[1]}")
        else:
            messagebox.showinfo("Search Result", "Element not found")

    def display_matrix(self):
        messagebox.showinfo("Matrix", str(self.matrix_handler))

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixApp(root)
    root.mainloop()