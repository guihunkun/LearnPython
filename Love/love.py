s = "Happy birthday "
for y in [i/100.0 for i in range(130, -116, -6)]:
    line, index = [], 0
    for x in [i/1000.0 for i in range(-1200, 1225, 25)]:
        if pow((x*x+y*y-1.0), 3) - x*x*y*y*y <= 0.0:
            line.append(s[index % len(s)])
            index = index + 1
        else:
            line.append(" ")
    print("".join(line))
