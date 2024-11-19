def read_and_write_file(input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, "r") as infile:
            content = infile.read()

        # Modify the content (e.g., add a header)
        modified_content = "=== Modified File ===\n" + content.upper()

        # Open the output file for writing
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"File has been successfully modified and saved to {output_file}.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
read_and_write_file("input.txt", "output.txt")
