import tkinter as tk
def message_rev():
    root = tk.Tk()
    root.title("Message Reverser")
    root.geometry("400x200")

    def reverse_message():
        message = entry.get()
        reversed_message = message[::-1]
        result_label.config(text=f"Reversed Message: {reversed_message}")

    entry = tk.Entry(root, width=30)
    entry.pack(pady=10)

    reverse_button = tk.Button(root, text="Reverse", command=reverse_message)
    reverse_button.pack(pady=5)

    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    root.mainloop()
message_rev()