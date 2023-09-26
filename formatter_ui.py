import tkinter as tk
from tkinter import filedialog, messagebox
import eb_formatter

VERSION_NO = "2.05"

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        selectedfile_label.config(text="Selected File: " + file_path)
        selected_file.set(file_path)

def run_tool():
    file_path = selected_file.get() # Get the selected file path

    arg1 = var_arg1.get()
    arg2 = var_arg2.get()
    arg3 = var_arg3.get()
    arg4 = var_arg4.get()

    company= dropdown_var.get()
   
    try:
        eb_formatter.edit(company, file_path, arg1, arg2, arg3, arg4)
    except Exception as e:
        # Display error
        message = str(e)
        messagebox.showerror("Error", message)
    else:
        # Display message
        message = "Modifications successfully applied!"
        messagebox.showinfo("Formatter :^)", message)

def on_dropdown_change(*args):
    # This function will be called when the dropdown selection changes
    selected_option = dropdown_var.get()
    dropdown_label.config(text=f"Selected company: {selected_option}")

# Create the main window
root = tk.Tk()
root.title(f"Formatter :^) v{VERSION_NO}")

# Set the initial window size
root.geometry("460x260") # Width x Height

## Dropdown menu
# Create a tkinter StringVar to store the selected option
dropdown_var = tk.StringVar(root)

# Create a label to display the selected option
dropdown_label = tk.Label(root, text="Selected company: None")

# Create a list of options for the dropdown
options = ["","TSL", "Eatbook", "MSN", "Zula", "Uchify"]

# Create the dropdown menu
dropdown_menu = tk.OptionMenu(root, dropdown_var, *options, command=on_dropdown_change)
dropdown_menu['menu'].delete(0)

# Set the default selected option
dropdown_var.set(options[0])

# Create variables to hold checkbox states
var_arg1 = tk.BooleanVar()
var_arg2 = tk.BooleanVar()
var_arg3 = tk.BooleanVar()
var_arg4 = tk.BooleanVar()

# Create variable to hold selected file path
selected_file = tk.StringVar()

## Function checkbox
# Create checkboxes
chk_arg1 = tk.Checkbutton(root, text="Edit outbound links", variable=var_arg1)
chk_arg2 = tk.Checkbutton(root, text="Bold all heading3", variable=var_arg2)
chk_arg3 = tk.Checkbutton(root, text="Add horizontal lines to heading3s", variable=var_arg3)
chk_arg4 = tk.Checkbutton(root, text="Add horizontal lines to heading2s", variable=var_arg4)

# Create a file upload button
btn_upload = tk.Button(root, text="Upload File", command=open_file)

# Create a label to display the selected file
selectedfile_label = tk.Label(root, text="Selected file: None")

# Create a run button
btn_run = tk.Button(root, text="Run Tool", command=run_tool)

# Place contents
dropdown_label.pack(anchor="w")
dropdown_menu.pack(anchor="w")

selectedfile_label.pack(pady=(10,0), anchor="nw")
btn_upload.pack(anchor="w")

chk_arg1.pack(pady=(10,0), anchor="nw")
chk_arg2.pack(anchor="w")
chk_arg3.pack(anchor="w")
chk_arg4.pack(anchor="w")

btn_run.pack()

# Start the GUI event loop
root.mainloop()
