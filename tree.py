import os

def print_directory_tree_with_content(start_path, indent=""):
    try:
        for item in sorted(os.listdir(start_path)):
            item_path = os.path.join(start_path, item)
            if os.path.isdir(item_path):
                print(f"{indent}|-- {item}")
                print_directory_tree_with_content(item_path, indent + "    ")
            else:
                print(f"{indent}|-- {item}")
                print(f"{indent}    |-- File Content Start --")
                try:
                    with open(item_path, "r", encoding="utf-8") as file:
                        for line in file:
                            print(f"{indent}    {line.rstrip()}")
                except Exception as e:
                    print(f"{indent}    [Error reading file: {str(e)}]")
                print(f"{indent}    |-- File Content End --")
    except PermissionError:
        print(f"{indent}|-- [Permission Denied]")

# Specify the starting directory here
start_directory = input("Enter the starting directory path: ").strip() or "."
print(f"Directory tree for: {start_directory}\n")
print_directory_tree_with_content(start_directory)
