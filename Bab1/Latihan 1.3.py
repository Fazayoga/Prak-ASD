def ucapkanSalam():
    print('Assalamualaikum!')

def sapa(nama):
    ucapkanSalam()
    print('Halo',nama)
    print('Selamat Belajar!')

def kuadratkan(b):
    h = b*b
    return h

ucapkanSalam()
sapa('Faza')
b = kuadratkan(5)
print(b)
k = 9
print('Bilangannya', k, ',kalau dipangkat dua jadinya', kuadratkan(k))