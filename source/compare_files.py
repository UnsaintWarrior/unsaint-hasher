import os
import glob


def compare_files(files):
    # Read the contents of the first file to use as a basis for comparison
    with open(files[0], 'r') as file:
        base_lines = file.readlines()

    for file_path in files[1:]:
        with open(file_path, 'r') as file:
            compare_lines = file.readlines()

            # Check if the files have the same number of lines
            if len(base_lines) != len(compare_lines):
                print(f"The files {os.path.basename(files[0])} and {os.path.basename(file_path)} are different: they have a different number of lines.")
                return

            # Compare each line of the files
            for i, (line1, line2) in enumerate(zip(base_lines, compare_lines)):
                if line1 != line2:
                    print(f"The files {os.path.basename(files[0])} and {os.path.basename(file_path)} are different at line {i+1}.")
                    return

    print("All files have identical content.")

# Directory where the files are located
directory = '.'  # Use '.' for current directory or specify the path
pattern = "file_hashes_*.txt"  # Pattern to match the files

# List all files in the directory that match the pattern
files = glob.glob(os.path.join(directory, pattern))

if len(files) < 2:
    print("There are not enough files to compare.")
else:
    compare_files(sorted(files))

# Wait for the user to press any key before closing
input("Press any key to exit...")
