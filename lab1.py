import tkinter as tk
from tkinter import messagebox

def find_min_sum_digit_element(matrix):
    min_sum = float('inf')
    min_sum_index = None

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            element = matrix[i][j]
            digit_sum = sum(int(digit) for digit in str(abs(element))) 
            if digit_sum < min_sum:
                min_sum = digit_sum
                min_sum_index = (i, j)

    return min_sum, min_sum_index

def calculate_product(matrix):
    max_row_sums = [max(row) for row in matrix]
    max_col_sums = [max(col) for col in zip(*matrix)]
    product = max(max_row_sums) * max(max_col_sums)
    return product

def process_matrix():
    try:
        matrix = [[int(entry.get()) for entry in row_entries] for row_entries in entry_matrix]
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста вводите числа во все ячейки .")
        return

    min_sum, min_sum_index = find_min_sum_digit_element(matrix)
    product = calculate_product(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < 11:
                matrix[i][j] = matrix[i][j] ** 2

    result_label.config(text=f"минимальная сумма чисел: {min_sum}, Index: {min_sum_index}\n"
                             f"Результат максимума от сумм: {product}\n"
                             f"Полученная матрица: {matrix}")

root = tk.Tk()
root.title("Матрица")
root.geometry("300x200")

matrix_frame = tk.Frame(root)
matrix_frame.pack()

entry_matrix = []

for i in range(3): 
    row_entries = []
    for j in range(3):
        entry = tk.Entry(matrix_frame, width=5)
        entry.grid(row=i, column=j, padx=5, pady=5)
        row_entries.append(entry)
    entry_matrix.append(row_entries)

calculate_button = tk.Button(root, text="Расчитать", command=process_matrix)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
