import tkinter as tk
root=tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")  

label=tk.Label(root, text="Enter length in inch:", fg="white", bg="#3498db", font=("Arial", 14))
label.pack(pady=10)

entry=tk.Entry(root, font=("Arial", 14), bg="#ecf0f1")
entry.pack(pady=10)

def convert():
    inch=float(entry.get())
    cm=inch*2.54
    result_label.config(text=f"{inch} inch = {cm:.2f} cm")

convert_button=tk.Button(root, text="Convert to cm", command=convert, bg="#2ecc71", fg="white", font=("Arial", 12))
convert_button.pack(pady=10)

result_label=tk.Label(root, text="", font=("Arial", 14), bg="#f1c40f")
result_label.pack(pady=10)

root.mainloop()
