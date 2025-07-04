import tkinter as tk
from ttkbootstrap import Style
from tkinter import messagebox

board = [[0 for _ in range(9)] for _ in range(9)]

def is_valid(board, num, pos):
    row, col = pos
    if num in board[row]: return False
    if num in [board[i][col] for i in range(9)]: return False

    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False
    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0
    return False

def gui_solve():
    try:
        for i in range(9):
            for j in range(9):
                val = entries[i][j].get()
                board[i][j] = int(val) if val else 0
        if solve(board):
            for i in range(9):
                for j in range(9):
                    entries[i][j].delete(0, tk.END)
                    entries[i][j].insert(0, str(board[i][j]))
        else:
            messagebox.showerror("No Solution", "This Sudoku puzzle is unsolvable.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter only digits 1–9.")

# --- GUI Setup ---
root = tk.Tk()
root.title("Sudoku Solver - by Roger")
style = Style(theme='minty')
style.master = root

entries = [[None for _ in range(9)] for _ in range(9)]

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

for i in range(9):
    for j in range(9):
        e = tk.Entry(
            frame,
            width=2,
            font=('Helvetica', 18),
            justify='center',
            relief='solid',
            borderwidth=1,
            highlightthickness=1
        )

        # Bold-style padding to visually separate 3x3 boxes
        pady = (4, 1) if i % 3 == 0 else (1, 4) if i % 3 == 2 else (1, 1)
        padx = (4, 1) if j % 3 == 0 else (1, 4) if j % 3 == 2 else (1, 1)

        e.grid(row=i, column=j, padx=padx, pady=pady)
        entries[i][j] = e

solve_btn = tk.Button(root, text="Solve", font=("Helvetica", 14), command=gui_solve)
solve_btn.pack(pady=10)

root.mainloop()