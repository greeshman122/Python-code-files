import os

# Function to perform file operations
def file_operations():
    try:
        # Specify file name
        file_name = "writing.txt"

        # Check if file exists
        if os.path.exists(file_name):
            print(f"{file_name} exists.")
        else:
            # Create the file if it doesn't exist
            with open(file_name, "w") as file:
                file.write("This is a new file.\nFile operations example.")
            print(f"{file_name} created.")

        # Open the file and perform operations using 'with'
        with open(file_name, "r") as file:
            content = file.read()
            print("Content of the file:")
            print(content)

            # Split content based on spaces
            words = content.split()
            print("Words in the file:")
            print(words)

        # Create a new file
        new_file_name = "new_file.txt"
        with open(new_file_name, "w") as new_file:
            new_file.write("This is the new file created.")
        print(f"{new_file_name} created.")

        # Delete the file
        """if os.path.exists(new_file_name):
            os.remove(new_file_name)
            print(f"{new_file_name} deleted.")"""

        # Create a new folder
        folder_name = "example_folder"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"{folder_name} created.")

        # Delete the folder
        """if os.path.exists(folder_name):
            os.rmdir(folder_name)
            print(f"{folder_name} deleted.")"""

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
file_operations()
