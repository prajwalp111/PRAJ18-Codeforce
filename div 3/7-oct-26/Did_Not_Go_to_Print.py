t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    stack = []
    printed = [False] * (n + 1)

    for i in range(1, n + 1):
        c = s[i - 1]
        if c == '1':
            stack.append(i)
        elif c == '2':
            if stack:
                printed[stack.pop()] = True
            else:
                printed[i] = True
        else:  # '3'
            printed[i] = True

    result = [i for i in range(1, n + 1) if not printed[i]]
    print(len(result))
    print(*result)