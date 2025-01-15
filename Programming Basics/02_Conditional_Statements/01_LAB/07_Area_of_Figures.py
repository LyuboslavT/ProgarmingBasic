import math
figure = str(input())
if figure == 'square':
    a = float(input())
    print(f'{a * a:.3f}')
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    print(f'{a * b:.3f}')
elif figure == 'circle':
    r = float(input())
    print(f'{r**2 * math.pi:.3f}')
elif figure == 'triangle':
    b = float(input())
    h = float(input())
    print(f'{b * h / 2:.3f}')
