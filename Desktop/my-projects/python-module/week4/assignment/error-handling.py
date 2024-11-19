def read_user_file():
    filename = input("Enter the filename: ")

    try:
        # Attempt to open the file for reading
        with open(filename, "r") as file:
            content = file.read()
            print("\n=== File Content ===")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist. Please check the filename.")
    except PermissionError:
        print(f"Error: You don't have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
read_user_file()
