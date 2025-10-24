x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

if (x1 + y1) % 2 == (x2 + y2) % 2:
    print("YES")
    print("White" if (x1 + y1) % 2 == 0 else "Black")
else:
    print("NO")