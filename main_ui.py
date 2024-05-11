# import tkinter as tk
# from tkinter import ttk
# import main
# import folder_select

# def submit():
#     input_value = input_field.get()
#     file_name = file_name_field.get()
#     do_not_merge = not_merge_files.get()

#     main.init(input_value, do_not_merge, file_name)

# def open_merge_file_window():
#     second_window_window = tk.Toplevel()
#     folder_select.FolderSelector(second_window_window)

# root = tk.Tk()
# root.title("Form")
# root.configure(padx=10, pady=10) 

# style = ttk.Style()
# style.theme_use('classic')

# not_merge_files = tk.IntVar()

# input_label = ttk.Label(root, text="File Link:", font=("Arial", 11))
# input_label.pack()
# file_name_label = ttk.Label(root, text="File Name:", font=("Arial", 11))
# file_name_label.pack()

# input_field = ttk.Entry(root, width=30)
# input_field.pack(pady=5) 
# file_name_field = ttk.Entry(root, width=30)
# file_name_field.pack(pady=5)


# do_not_merge_checkbox = ttk.Checkbutton(root, text="Do Not Merge Files", variable=not_merge_files)
# do_not_merge_checkbox.pack()

# submit_button = ttk.Button(root, text="Submit", command=submit)
# submit_button.pack()

# merge_files_button = ttk.Button(root, text="Merge Files", command=open_merge_file_window)
# merge_files_button.pack()

# root.mainloop()

import tkinter as tk
from tkinter import ttk
import main
import folder_select
import screeninfo
import customtkinter as ctk

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue") 

def submit():
  input_value = input_field.get()
  file_name = file_name_field.get()
  do_not_merge = not_merge_files.get()
  if input_value:
        # the user entered data in the mandatory entry: proceed to next step
      main.init(input_value, do_not_merge, file_name, root)
      if input_field._border_color == 'red':
          input_field.configure(True, border_color='default')

  else:
      # the mandatory field is empty
      input_field.focus_set()
      input_field.configure(True, border_color='red')

def open_merge_file_window():
  second_window_window = tk.Toplevel()
  folder_select.FolderSelector(second_window_window)

root = ctk.CTk()
root.title("Form")

screen_width = screeninfo.get_monitors()[0].width
screen_height = screeninfo.get_monitors()[0].height
window_width = 500
window_height = 300
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2

# Set window geometry (choose either method)
# Method 1: geometry
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
# Method 2: wm_geometry
# root.wm_geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")


# Set the theme (optional, choose a theme you like)
# root.tk.call('ttk::set_theme', 'classic')  # Example theme
# ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')

ttk.Style().theme_use('vista')
root.configure(padx=10, pady=10)  # Adjust padding as needed

input_label = ctk.CTkLabel(root, text="Enter File Link:", font=("Default", 15))
input_label.pack()
input_field = ctk.CTkEntry(root,width=window_width*.8)
input_field.pack(pady=5)

# Create a label and entry field for file name
file_name_label = ctk.CTkLabel(root, text="Enter File Name:", font=("Default", 15))
file_name_label.pack(pady=5)
file_name_field = ctk.CTkEntry(root,width=window_width*.8)
file_name_field.pack()

# Uncomment and customize dropdown fields if needed (refer to previous code)

# Create the checkbox with a clearer style
not_merge_files = tk.IntVar(value=0)
do_not_merge_checkbox = ctk.CTkCheckBox(root, text="Do Not Merge Files", variable=not_merge_files)
do_not_merge_checkbox.pack(pady=5)

# Create buttons with a different style
submit_button = ctk.CTkButton(root, text="Submit", command=submit)
submit_button.pack(pady=10)

merge_files_button = ctk.CTkButton(root, text="Merge Files", command=open_merge_file_window)
merge_files_button.pack(pady=10)


# progressbar = ctk.CTkProgressBar(root, orientation="horizontal",mode="determinate",width=window_width*.8)
# progressbar = ttk.Progressbar(root, orient="horizontal",mode="determinate",length=window_width*.8)
# progressbar['maximum'] = 100
# progressbar.pack()

# def animate():
#   progressbar.step(.1)
#   root.after(100, animate)

# animate()
root.mainloop()
