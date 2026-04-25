import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = input()
lat = input()
n = int(input())
defibs = []
xlon = float(lon.replace(",", "."))
xlat = float(lat.replace(",", "."))
for i in range(n):
    defib = input()
    defib_item = defib.split(";")
    defib_name = defib_item[1]
    defib_lon = float(defib_item[4].replace(",", "."))
    defib_lat = float(defib_item[5].replace(",", "."))
    x = (xlon - defib_lon) * math.cos((xlat + defib_lat) / 2)
    y = xlat - defib_lat
    d = ((x**2 + y**2) ** 0.5) * 6371
    item = {"name": defib_name, "distance": d}
    defibs.append(item)

d_list = [x["distance"] for x in defibs]
min_d = min(d_list)
the_defib = [x["name"] for x in defibs if x["distance"] == min_d]
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(the_defib[0])
