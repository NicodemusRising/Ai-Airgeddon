import tkinter as tk
from platform_support import *

def main():
    # Initialize the main window
    root = tk.Tk()

    # Add a title
    root.title("Airgeddon GUI")

    # Set window size
    root.geometry("500x300")

    # Add a menu
    menu = tk.Menu(root)
    root.config(menu=menu)

    # Add a file menu
    file_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)

    # Add a status bar
    status_bar = tk.Label(root, text="Welcome to Airgeddon GUI", bd=1, relief="sunken", anchor="w")
    status_bar.pack(side="bottom", fill="x")

    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
```

# HackGPT - platform\_support.py

```python
import os

def open_file():
    if is_windows():
        os.startfile("example.txt")
    elif is_macos():
        os.system("open example.txt")
    elif is_linux():
        os.system("xdg-open example.txt")

def save_file():
    if is_windows():
        os.system('echo "Hello, World!" > "example.txt"')
    elif is_macos():
        os.system('echo "Hello, World!" > "example.txt"')
    elif is_linux():
        os.system('echo "Hello, World!" > "example.txt"')

def is_windows():
    return os.name == 'nt'

def is_macos():
    return os.name == 'posix' and sys.platform == 'darwin'

def is_linux():
    return os.name == 'posix' and sys.platform != 'darwin'
```

Project resources: file 1: airgeddon\_gui.py, file 2: platform\_support.py
Select files by their number.
