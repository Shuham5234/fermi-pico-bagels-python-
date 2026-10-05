original_number = "123"

while True:
    guess_number = input("Enter your guess: ")
    output = []

    if len(original_number) != len(guess_number):
        print("Length of original and guess are not same")
        continue

    if len(original_number) != len(set(guess_number)):
        print("Number is Repeated")
        continue

    if guess_number == original_number:
        print("Fermi " * len(original_number), "!!!")
        break

    for i in range(len(original_number)):
        if guess_number[i] == original_number[i]:
            output.append("Fermi")
        elif guess_number[i] in original_number:
            output.append("Pico")

    output_string = ""

    for i in output:
        output_string += i + " "

    if len(output) == 0:
        print("Bagel")
    else:
        print(output_string)