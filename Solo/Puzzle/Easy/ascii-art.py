# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

width = int(input())
h = int(input())
t = input()
letters = "abcdefghijklmnopqrstuvwxyz"
indices = letters + "?"
ascii_lines = []
for i in range(h):
    row = input()
    ascii_lines.append(row)

answer = ""
for i in range(h):
    for letter in t:
        if letter.lower() in letters:
            index_letter = letters.index(letter.lower())
            answer += ascii_lines[i][index_letter * width : (index_letter + 1) * width]
        else:
            answer += ascii_lines[i][26 * width : 27 * width]
    answer += "\n"

# print(ascii_letters[0]['c'],file=sys.stderr,flush=True)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(answer)
