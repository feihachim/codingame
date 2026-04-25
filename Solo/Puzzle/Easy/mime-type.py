# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
mime_types = {}
n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mime_types[ext.lower()] = mt
for i in range(q):
    fname = input()  # One file name per line.
    separated = fname.split(".")
    if len(separated) == 1:
        print("UNKNOWN")
    else:
        file_type = separated[-1]
        if file_type.lower() in mime_types.keys():
            print(mime_types[file_type.lower()])
        else:
            print("UNKNOWN")
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
# print("UNKNOWN")
