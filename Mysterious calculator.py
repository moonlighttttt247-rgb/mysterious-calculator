import tkinter as tk

class MysteriousCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("The Oracle • Calculator")
        self.root.geometry("340x480")
        self.root.config(bg="#050505")
        self.root.resizable(False, False)

        self.equation = ""
        self.display_var = tk.StringVar()

        # Build Interface
        self.create_display()
        self.create_buttons()

    def create_display(self):
        display_frame = tk.Frame(self.root, bg="#050505")
        display_frame.pack(expand=True, fill="both", padx=15, pady=15)

        self.display = tk.Entry(
            display_frame,
            textvariable=self.display_var,
            font=("Courier New", 22, "bold"),
            bg="#0a0a0a",
            fg="#c084fc",  # Soft mystical purple glow
            bd=0,
            justify="right",
            insertbackground="#c084fc"
        )
        self.display.pack(expand=True, fill="both", ipady=15)

    def create_buttons(self):
        btn_frame = tk.Frame(self.root, bg="#050505")
        btn_frame.pack(expand=True, fill="both", padx=15, pady=(0, 15))

        # Button layout grid (Text, Row, Column)
        buttons = [
            ('C', 0, 0), ('(', 0, 1), (')', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('**', 4, 2), ('=', 4, 3)
        ]

        for (text, row, col) in buttons:
            # Mysterious color grading
            if text == '=':
                bg_color = "#3b0764"  # Deep obsidian-violet
                fg_color = "#f3e8ff"
            elif text in ('C', '/', '*', '-', '+', '**'):
                bg_color = "#121212"
                fg_color = "#a855f7"
            else:
                bg_color = "#0c0c0c"
                fg_color = "#d1d5db"

            btn = tk.Button(
                btn_frame,
                text=text,
                font=("Courier New", 14, "bold"),
                bg=bg_color,
                fg=fg_color,
                activebackground="#27272a",
                activeforeground="#ffffff",
                bd=0,
                relief="flat",
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

        # Make the buttons scale evenly inside the grid
        for i in range(5):
            btn_frame.rowconfigure(i, weight=1)
        for j in range(4):
            btn_frame.columnconfigure(j, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.equation = ""
            self.display_var.set("")
        elif char == '=':
            try:
                # Safely evaluate the math string
                result = str(eval(self.equation))
                self.display_var.set(result)
                self.equation = result
            except Exception:
                self.display_var.set("ERR: UNKNOWN FATE")
                self.equation = ""
        else:
            self.equation += str(char)
            self.display_var.set(self.equation)

if __name__ == "__main__":
    root = tk.Tk()
    app = MysteriousCalculator(root)
    root.mainloop()