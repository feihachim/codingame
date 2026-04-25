# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
horses = [0] * n
for i in range(n):
    pi = int(input())
    horses[i] = pi
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
horses.sort()
differences = [0] * (n - 1)
for i in range(n - 1):
    differences[i] = horses[i + 1] - horses[i]
print(min(differences))
