# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
def letter_to_binary_7(letter):
    ascii_number = ord(letter)
    binary_letter = bin(ascii_number)
    binary_no_overhead_letter = binary_letter[2:]
    length_binary_no_overhead_letter = len(binary_no_overhead_letter)
    if length_binary_no_overhead_letter < 7:
        binary_7_letter = (
            f"{(7 - length_binary_no_overhead_letter) * 0}{binary_no_overhead_letter}"
        )
    else:
        binary_7_letter = binary_no_overhead_letter
    return binary_7_letter


def frequency_binary(numbers):
    result = []
    i = 0
    occurrence = 1
    l_numbers = len(numbers)
    while i + 1 < l_numbers:
        letter = numbers[i]
        if numbers[i + 1] == numbers[i]:
            occurrence += 1
        else:
            item = (letter, occurrence)
            result.append(item)
            letter = numbers[i + 1]
            occurrence = 1
        i += 1
    item = (letter, occurrence)
    result.append(item)
    return result


def unary(word):
    binary_word = ""
    unary_value = {"0": "00", "1": "0"}
    for letter in word:
        binary_word += letter_to_binary_7(letter)
    frequency_binary_letter = frequency_binary(binary_word)
    encoded_message = []
    for item in frequency_binary_letter:
        encoded_item = f"{unary_value[item[0]]} {'0' * item[1]}"
        encoded_message.append(encoded_item)
    result = " ".join(encoded_message)
    return result


print(unary(message))
