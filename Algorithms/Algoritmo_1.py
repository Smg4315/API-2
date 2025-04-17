import sys
import random

def Algoritmo_1(num_strings):
    if num_strings <= 0:
        print("Please enter a valid integer (positive).")
        return
    
    valid_strings = set()
    invalid_strings = set()

    while len(valid_strings) < num_strings:
        valid_strings.add(generate_valid_string(random.randint(0, 10)))

    while len(invalid_strings) < num_strings:
        invalid_strings.add(generate_invalid_string(random.randint(0, 10)))

    with open("String.txt", "w") as out_file:
        out_file.write("--- Strings: ---\n")
        out_file.writelines("'" + s + "'" + "\n" for s in valid_strings)
        out_file.writelines("'" + s + "'" + "\n" for s in invalid_strings)

def generate_valid_string(n):
    if n == 0:
        return ""
    return "a" + generate_valid_string(n - 1) + "b"

def generate_invalid_string(n):
    chars = ["a", "b"]
    return "".join(random.choices(chars, k=n)) + "a"

if __name__ == "__main__":
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    Algoritmo_1(num)
