def trojkat(bok_a, bok_b, bok_c, wysokosc_a):
    obwod = bok_a + bok_b + bok_c
    pole = (bok_a * wysokosc_a) / 2
    return obwod, pole


# kwadrat, prostokat dla studenta 1
def kwadrat(bok):
    # TODO
    return 0, 0


def prostokat(bok_a, bok_b):
    # TODO
    return 0, 0

# rownoleglobok i romb dla studenta 2
def rownoleglobok(bok_a, bok_b, wysokosc_a):
    # TODO
    return 0, 0

def romb(bok, wysokosc):
    # TODO
    return 0, 0

# trapez, koło dla studenta 3
def trapez(bok_trapezu1, bok_trapezu2, bok_trapezu3, bok_trapezu4, wysokosc_trap):
    obwod_trap = bok_trapezu1 + bok_trapezu2 + bok_trapezu3 + bok_trapezu4
    pole_trap = ((bok_trapezu1 + bok_trapezu2)*wysokosc_trap)/2
    return obwod_trap,pole_trap




import math
pi=math.pi
def kolo(promien):

obwod=2 * pi * promien
pole= promien * promien * pi
return obwod_kolo, pole_kola


assert trojkat(10, 15, 16, 8) == (41, 40)
assert kwadrat(20) == (80, 400)
assert prostokat(12, 10) == (44, 120)
assert rownoleglobok(6, 5, 2) == (22, 12)
assert romb(10, 5) == (40, 50)
assert trapez(10, 15, 7, 14, 2) == (45, 25)
# TODO na koniec! dopisz 2 testy dla kola i dla kazdej innej figury po jednym dodatkowym tescie
