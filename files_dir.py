import os

# Create an empty dictionary to store file information
file_info = {}

# Get the current working directory
current_directory = os.getcwd()

# List all files and directories in the current directory
files = os.listdir(current_directory)

# Iterate through the list of files
for file in files:
    # Create an absolute path for each file
    file_path = current_directory + '/' + file
    
    # Check if the path is a file
    if os.path.isfile(file_path):
        # Get the size of the file in bytes
        file_size = os.path.getsize(file_path)
        
        # Store the file name and size in the dictionary
        file_info[file] = str(file_size) + ' Bytes'
