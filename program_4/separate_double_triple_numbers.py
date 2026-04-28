import os

current_folder = os.path.dirname(os.path.abspath(__file__))

input_file_path = os.path.join(current_folder, "integers.txt")
double_file_path = os.path.join(current_folder, "double.txt")
triple_file_path = os.path.join(current_folder, "triple.txt")

if not os.path.exists(input_file_path):
    print("integers.txt is missing.")
else:
    with open(input_file_path, "r") as source_file:
        number_list = source_file.read().split()

    print("Numbers found:", number_list)

    with open(double_file_path, "w") as double_file, open(triple_file_path, "w") as triple_file:
        for number_text in number_list:
            number_value = int(number_text)

            if number_value % 2 == 0:
                squared_value = number_value ** 2
                double_file.write(str(squared_value) + "\n")
            else:
                cubed_value = number_value ** 3
                triple_file.write(str(cubed_value) + "\n")

    print("Done. Check double.txt and triple.txt.")