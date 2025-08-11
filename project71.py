import tkinter as tk
from tkinter import messagebox

class StackVisualizer:
    def __init__(self, root):
        self.stack = []
        self.root = root
        self.root.title("Stack Visualizer")
        self.root.geometry("400x500")

        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)

        self.push_btn = tk.Button(self.root, text="Push", command=self.push)
        self.push_btn.pack(side="left", padx=20)

        self.pop_btn = tk.Button(self.root, text="Pop", command=self.pop)
        self.pop_btn.pack(side="right", padx=20)

        self.draw_stack()

    def push(self):
        val = self.entry.get()
        if val == "":
            messagebox.showwarning("Input Error", "Enter a value to push")
            return
        self.stack.append(val)
        self.entry.delete(0, tk.END)
        self.draw_stack()

    def pop(self):
        if not self.stack:
            messagebox.showerror("Stack Underflow", "Stack is empty!")
        else:
            self.stack.pop()
        self.draw_stack()

    def draw_stack(self):
        self.canvas.delete("all")
        width = 200
        height = 40
        x = 100
        y = 350

        for item in reversed(self.stack):
            self.canvas.create_rectangle(x, y, x + width, y - height, fill="skyblue")
            self.canvas.create_text(x + width / 2, y - height / 2, text=item)
            y -= height + 5

# Run the visualizer
if __name__ == "__main__":
    root = tk.Tk()
    app = StackVisualizer(root)
    root.mainloop()