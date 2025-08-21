# File Read & Write Challenge 🖋️
# This program asks the user for a filename,
# reads the file, and writes a modified version to a new file.

try:
    # Ask the user for the filename
    filename = input("Enter the filename you want to read: ")

    # Try opening the file in read mode
    with open(filename, "r") as file:
        content = file.read()   # Read everything inside the file

    # Modify the content (for beginners, let's make it uppercase)
    modified_content = content.upper()

    # Write the modified content into a new file
    with open("modified_" + filename, "w") as new_file:
        new_file.write(modified_content)

    print("Success! A new file has been created: modified_" + filename)

# Error handling if file not found or cannot be read
except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename and try again.")
except PermissionError:
    print("Error: You don’t have permission to read this file.")
except Exception as e:
    print("An unexpected error occurred:", e)
