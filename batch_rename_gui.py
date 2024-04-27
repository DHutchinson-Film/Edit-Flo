import os
import tkinter as tk
from tkinter import filedialog, messagebox

def batch_rename(directory, prefix, naming_convention="sequential"):
    # Get list of files in the directory
    files = os.listdir(directory)
    
    # Filter files if needed (e.g., by extension)
    # You can customize this filtering logic as per your requirements
    files = [file for file in files if file.endswith(('.mp4', '.mov', '.avi'))]
    
    # Handle case where no files match the criteria
    if not files:
        messagebox.showinfo("No Files Found", "No files found matching the specified criteria.")
        return
    
    # Sort files alphabetically or by modification time
    files.sort()  # You can customize the sorting logic as per your requirements
    
    # Initialize index for sequential numbering
    index = 1
    
    # Iterate through the files
    for file in files:
        # Split the file name and extension
        name, extension = os.path.splitext(file)
        
        # Create the new file name based on the chosen naming convention
        if naming_convention == "sequential":
            new_name = f"{prefix}_{index}{extension}"
            index += 1
        elif naming_convention == "original_with_prefix":
            new_name = f"{prefix}_{name}{extension}"
        else:
            messagebox.showwarning("Invalid Naming Convention", "Invalid naming convention specified. Using sequential numbering.")
            new_name = f"{prefix}_{index}{extension}"
            index += 1
        
        # Construct the full paths
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed {file} to {new_name}")

def browse_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory)

def rename_files():
    directory = directory_entry.get()
    prefix = prefix_entry.get()
    naming_convention = naming_convention_var.get()
    batch_rename(directory, prefix, naming_convention)

# Create main window
window = tk.Tk()
window.title("Batch File Rename")

# Directory selection
directory_label = tk.Label(window, text="Directory:")
directory_label.grid(row=0, column=0, sticky="w")
directory_entry = tk.Entry(window, width=50)
directory_entry.grid(row=0, column=1, padx=5, pady=5)
browse_button = tk.Button(window, text="Browse", command=browse_directory)
browse_button.grid(row=0, column=2, padx=5, pady=5)

# Prefix input
prefix_label = tk.Label(window, text="Prefix:")
prefix_label.grid(row=1, column=0, sticky="w")
prefix_entry = tk.Entry(window, width=50)
prefix_entry.grid(row=1, column=1, padx=5, pady=5)

# Naming convention selection
naming_convention_label = tk.Label(window, text="Naming Convention:")
naming_convention_label.grid(row=2, column=0, sticky="w")
naming_convention_var = tk.StringVar()
naming_convention_var.set("sequential")
sequential_radio = tk.Radiobutton(window, text="Sequential", variable=naming_convention_var, value="sequential")
sequential_radio.grid(row=2, column=1, sticky="w")
original_radio = tk.Radiobutton(window, text="Original with Prefix", variable=naming_convention_var, value="original_with_prefix")
original_radio.grid(row=3, column=1, sticky="w")

# Rename button
rename_button = tk.Button(window, text="Rename Files", command=rename_files)
rename_button.grid(row=4, column=1, padx=5, pady=5)

# Run the main event loop
window.mainloop()