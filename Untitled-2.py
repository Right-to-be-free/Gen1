import tkinter as tk
from tkinter import scrolledtext

def send_message():
    message = entry.get()
    if message:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + message + "\n")
        chat_window.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Chat Box")

# Create a scrolled text widget for the chat window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create an entry widget for typing messages
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.X, expand=True)

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10, side=tk.RIGHT)

# Run the application
root.mainloop()