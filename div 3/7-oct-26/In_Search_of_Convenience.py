
def cordinates_finder(x, y, R):
#     for i in range(-10, 10):
#         for j in range(-10, 10):
#             if (x - i)**2 + (y - j)**2 == R**2:
                return (x+R, y)

if __name__ == "__main__":
    n = int(input())
    circles = []
    cordinates = []

    for i in range(n):
        x, y, R = map(int, input().split())
        circles.append((x, y, R))

    for x, y, R in circles:
        cordinates.append(cordinates_finder(x, y, R))

    for x, y in cordinates:
        print(x, y)

# t = int(input())
# for _ in range(t):
#     x0, y0, R = map(int, input().split())
#     print(x0 + R, y0)