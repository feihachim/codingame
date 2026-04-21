# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
temperatures = []
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)

    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    temperatures.append(t)
result = 0

negative_temperatures = [x for x in temperatures if x < 0]
positive_temperatures = [x for x in temperatures if x > 0]
if not temperatures:
    result = 0
elif temperatures == negative_temperatures:
    result = max(negative_temperatures)
elif temperatures == positive_temperatures:
    result = min(positive_temperatures)
else:
    min_positive = min(positive_temperatures)
    max_negative = max(negative_temperatures)

    if abs(min_positive) < abs(max_negative):
        result = min_positive
    elif abs(min_positive) > abs(max_negative):
        result = max_negative
    else:
        result = min_positive
print(result)
