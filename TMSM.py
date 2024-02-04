import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import subprocess
import os

def run_c_executable(input_text):
    # Buat file input sementara dan tulis input_text ke dalamnya
    input_filename = "temp_input.txt"
    with open(input_filename, 'w') as file:
        file.write(input_text)

    # Menggunakan subproses untuk menjalankan eksekusi C dan mendapatkan output
    # Menggunakan perintah yang sesuai untuk OS Windows
    command = "TMSM.exe < {}".format(input_filename)
    result = subprocess.check_output(command, shell=True, text=True)

    # Menghapus file input sementara
    os.remove(input_filename)

    return result.strip()

def calculate_result():
    input_text = input_text_widget.get("1.0", tk.END).strip()

    if input_text:
        result = run_c_executable(input_text)
        result_text.delete(1.0, tk.END)  # Menghapus hasil sebelumnya
        result_text.insert(tk.END, result)
    else:
        result_text.delete(1.0, tk.END)  # Menghapus hasil sebelumnya
        result_text.insert(tk.END, "No input provided!")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            input_text = file.read()
        input_text_widget.delete("1.0", tk.END)
        input_text_widget.insert(tk.END, input_text)

def save_result():
    result = result_text.get(1.0, tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(result)

# Membuat jendela utama
root = tk.Tk()
root.title("TMSM Executable C GUI")

# Frame untuk opsi masukan
input_options_frame = ttk.Frame(root)
input_options_frame.grid(row=0, column=0, columnspan=2, pady=10)

# Tombol radio untuk memilih metode input
input_method_var = tk.StringVar(value="text")  # Inisialisasi metode default
file_radio_button = ttk.Radiobutton(input_options_frame, text="Select File", variable=input_method_var, value="file", command=browse_file)
file_radio_button.grid(row=0, column=0, padx=5)

text_radio_button = ttk.Radiobutton(input_options_frame, text="Enter Text", variable=input_method_var, value="text", command=lambda: input_text_widget.focus())
text_radio_button.grid(row=0, column=1, padx=5)

# Widget input teks
input_text_widget = tk.Text(root, height=10, width=120)
input_text_widget.grid(row=1, column=0, columnspan=2, pady=10)

# Tombol run
run_button = ttk.Button(root, text="Run", command=calculate_result)
run_button.grid(row=2, column=0, pady=10)

# Tombol save
save_button = ttk.Button(root, text="Save Result", command=save_result)
save_button.grid(row=2, column=1, pady=10)

# Widget hasil teks
result_text = tk.Text(root, height=20, width=120)
result_text.grid(row=4, column=0, columnspan=2, pady=10)

# Memulai loop event Tkinter
root.mainloop()
