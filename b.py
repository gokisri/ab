def read_text_file(file_name):
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Read and display the content
            content = file.read()
            print(f"Content of '{file_name}':\n")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_name = input("Enter the name of the text file to read: ")
read_text_file(file_name)
