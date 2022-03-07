a = int(input())
b = int(input())
if a < b:
    a, b = b, a

r = a % b
while r != 0:
    a = b
    b = r
    r = a % b
print(f'MDC={b}')
