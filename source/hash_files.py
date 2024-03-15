import os
import hashlib

def hash_file(filename):
    """This function returns the SHA-256 hash of the file passed into it"""

    # Make a hash object
    h = hashlib.sha256()

    # Open file for reading in binary mode
    with open(filename, 'rb') as file:
        # Loop till the end of the file
        chunk = 0
        while chunk != b'':
            # Read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # Return the hex representation of digest
    return h.hexdigest()

def get_unique_filename(base_filename):
    """Generates a unique filename by appending a counter before the file extension if the file already exists."""
    filename, extension = os.path.splitext(base_filename)
    counter = 0
    # While the file exists, increment the counter and generate a new filename
    while os.path.exists(f"{filename}_{counter:02}{extension}"):
        counter += 1
    return f"{filename}_{counter:02}{extension}"

folder_path = 'files'  # Change this to the path of your folder

# Determine a unique filename for the output file
output_filename = get_unique_filename('file_hashes.txt')

# Open the uniquely named text file to write the output
with open(output_filename, 'w') as output_file:
    for subdir, dirs, files in os.walk(folder_path):
        for file in files:
            # Construct absolute path
            file_path = os.path.join(subdir, file)
            # Get the file's SHA-256 hash
            file_hash = hash_file(file_path)
            # Write the file path and its SHA-256 hash to the output file
            output_file.write(f"File: {file_path}\nSHA-256: {file_hash}\n\n")

print(f"Hashes written to {output_filename}")

# Wait for the user to press any key before closing
input("Press any key to exit...")
