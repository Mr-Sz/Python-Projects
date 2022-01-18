def gen_squares(n):
    for i in range(n):
        yield i**2
for numb in gen_squares(10):
    print(numb)
