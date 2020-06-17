def table(x=5):
    for inner in range(1, x+1):
        for outer in range(1, x+1):
            print(f'{inner}*{outer}=', inner * outer)
        print('---------')

table(10)