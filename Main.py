import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def create_folders():
    """Create the necessary folders if they don't exist."""
    if not os.path.exists('sc'):
        os.makedirs('sc')
        print('Folder "sc" created.')
    if not os.path.exists('sc-fixed'):
        os.makedirs('sc-fixed')
        print('Folder "sc-fixed" created.')

def remove_block_from_hex(file_path):
    with open(file_path, 'rb') as f:
        hex_data = f.read()

    block = b'\x00\x00\x00\x01'
    index = hex_data.find(block)

    if index != -1:
        new_hex_data = hex_data[:index] + hex_data[index + len(block):]
        return new_hex_data
    else:
        return hex_data

def process_files():
    # Get all .sc files in the 'sc' folder
    sc_files = [f for f in os.listdir('sc') if f.endswith('.sc')]

    for sc_file in sc_files:
        sc_file_path = os.path.join('sc', sc_file)

        # Process the file by removing the block
        new_hex_data = remove_block_from_hex(sc_file_path)

        # Save the modified file in the 'sc-fixed' folder
        new_sc_file_path = os.path.join('sc-fixed', sc_file)
        with open(new_sc_file_path, 'wb') as new_f:
            new_f.write(new_hex_data)

        print(f'Processed and saved: {sc_file}')
    input("\nPress enter to continue")
    clear()
    main()

def main():
    clear()
    print("Press enter to start fixing the .sc files")
    input(">>> ")

if __name__ == "__main__":
    create_folders()
    main()
    process_files()
