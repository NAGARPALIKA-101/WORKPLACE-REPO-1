from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import filedialog

def compress_image(input_path, output_path, target_size_kb):
    original_image = Image.open(input_path)
    temp_path = "C:/Users/sony/Desktop/LDCE/compress temp/temp.jpg"
    original_image.save(temp_path, quality=85)
    current_size_kb = os.path.getsize(temp_path) / 1024.0
    compression_ratio = target_size_kb / current_size_kb
    
    if compression_ratio >= 1.0:
        original_image.save(output_path)
        os.remove(temp_path)
        return

    compressed_image = Image.open(temp_path)
    compressed_image.save(output_path, quality=int(85 * compression_ratio))

    os.remove(temp_path)

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)

def compress_button_click():
    input_path = entry_path.get()
    output_path = entry_output_path.get()
    target_size_kb = float(entry_target_size.get())

    compress_image(input_path, output_path, target_size_kb)
    result_label.config(text="Image compression complete.")
def exit_button_click():
    root.destroy()

def animate_color_change():
    current_bg_color = button_exit.cget("bg")
    new_bg_color = "grey" if current_bg_color == "red" else "red"
    button_exit.config(bg=new_bg_color)
    root.after(500, animate_color_change) 

root = tk.Tk()
root.title("Image Compressor")
root.configure(bg="light blue")

label_path = tk.Label(root, text="Image Path:", bg="light blue")
label_path.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

entry_path = tk.Entry(root, width=40)
entry_path.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

button_browse = tk.Button(root, text="Browse", command=browse_file)
button_browse.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)

label_output_path = tk.Label(root, text="Output Path:", bg="light blue")
label_output_path.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

entry_output_path = tk.Entry(root, width=40)
entry_output_path.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

label_target_size = tk.Label(root, text="Target Size (KB):", bg="light blue")
label_target_size.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

entry_target_size = tk.Entry(root, width=10)
entry_target_size.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

button_compress = tk.Button(root, text="Compress Image", command=compress_button_click, bg="maroon", fg="white")
button_compress.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", bg="light blue")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

button_exit = tk.Button(root, text="Exit", command=exit_button_click, fg="white")
button_exit.grid(row=3, column=1, columnspan=2, pady=10)
animate_color_change()

root.mainloop()