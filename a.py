import datetime


def create_timestamped_file():
    # Get the current timestamp
    current_timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    # File name with the current timestamp
    file_name = f"{current_timestamp}.txt"

    # Write the timestamp as the content
    with open(file_name, 'w') as file:
        file.write(f"File created at: {current_timestamp}")

    print(f"File '{file_name}' has been created with timestamp as its content.")


# Call the function
create_timestamped_file()
