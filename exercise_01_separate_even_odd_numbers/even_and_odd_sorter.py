import os

current_folder = os.path.dirname(os.path.abspath(__file__))

numbers_file_path = os.path.join(current_folder, "numbers.txt")
even_file_path = os.path.join(current_folder, "even.txt")
odd_file_path = os.path.join(current_folder, "odd.txt")

if not os.path.exists(numbers_file_path):
    print("numbers.txt is missing.")
else:
    with open(numbers_file_path, "r") as numbers_file:
        number_list = numbers_file.read().split()

    print("Numbers found:", number_list)

    with open(even_file_path, "w") as even_file, open(odd_file_path, "w") as odd_file:
        for number_text in number_list:
            number_value = int(number_text)

            if number_value % 2 == 0:
                even_file.write(str(number_value) + "\n")
            else:
                odd_file.write(str(number_value) + "\n")

    print("Successfully classified numbers into even.txt and odd.txt.")