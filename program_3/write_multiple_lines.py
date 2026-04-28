def write_lines_to_file():
    with open("mylife.txt", "w") as life_file:
        while True:
            line_content = input("Enter line: ")
            life_file.write(line_content + "\n")

            user_choice = input("Are there more lines y/n? ")

            if user_choice.lower() == "n":
                break


write_lines_to_file()