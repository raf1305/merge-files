import tkinter as tk
from tkinter import filedialog
import merge_files

class FolderSelector:
    def __init__(self,window=None):
        if window:
            self.root = window
        else:
            self.root = tk.Tk()
        self.root.title("Folder Selector")
        self.folder_path = None
        self.create_widgets()

    def create_widgets(self):
        # create the button to open the file dialog
        self.button = tk.Button(self.root, text="Select Folder", command=self.select_folder)
        self.button.pack(pady=10)

        # create a label to display the selected folder path
        self.label = tk.Label(self.root, text="")
        self.label.pack()

    def select_folder(self):
        # open the file dialog and get the selected folder path
        self.folder_path = filedialog.askdirectory()
        merge_files.merge_files(self.folder_path.split('/')[-1])
        # update the label to display the selected folder path
        self.label.config(text=self.folder_path)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    folder_selector = FolderSelector()
    folder_selector.run()