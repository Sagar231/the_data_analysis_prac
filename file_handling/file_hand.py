import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set the file path to be in the same directory as the script
file_path = os.path.join(script_dir, "example.txt")

# # Create and write to the file
with open(file_path, "w") as file:
    file.write("Hello, World!")



