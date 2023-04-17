def trojkat(bok_a, bok_b, bok_c, wysokosc_a):
    obwod = bok_a + bok_b + bok_c
    pole = (bok_a * wysokosc_a) / 2
    return obwod, pole
#do każdego przykładu utworzyłyśmy osobne zmienne - w przypadku osób początkujących (jak my :)) kod będzie bardzo czytelny i ładny

# kwadrat, prostokat dla studenta 1
def kwadrat(bok_kwad):
    obwod_kwad = bok_kwad*4
    pole_kwad = bok_kwad*bok_kwad
    return obwod_kwad, pole_kwad

def prostokat(bok_a_pros, bok_b_pros):
    obwod_pros = bok_a_pros*2 + bok_b_pros*2
    pole_pros = bok_a_pros*bok_b_pros
    return obwod_pros, pole_pros

# rownoleglobok i romb dla studenta 2
def rownoleglobok(bok_a_row, bok_b_row, wysokosc_a_row):
    obwod_row = 2 * bok_a_row + 2 * bok_b_row
    pole_row = bok_a_row * wysokosc_a_row
    return obwod_row, pole_row

def romb(bok_rom, wysokosc_rom):
    obwod_rom = 4 * bok_rom
    pole_rom = bok_rom * wysokosc_rom
    return obwod_rom, pole_rom

# trapez, koło dla studenta 3
def trapez(bok_trapezu1, bok_trapezu2, bok_trapezu3, bok_trapezu4, wysokosc_trap):
    obwod_trap = bok_trapezu1 + bok_trapezu2 + bok_trapezu3 + bok_trapezu4
    pole_trap = ((bok_trapezu1 + bok_trapezu2)*wysokosc_trap)/2
    return obwod_trap,pole_trap




import math
pi=math.pi
def kolo(promien_kola):

    obwod_kolo=2 * pi * promien_kola
    pole_kola= promien_kola * promien_kola * pi
    return obwod_kolo, pole_kola


assert trojkat(10, 15, 16, 8) == (41, 40)
assert kwadrat(20) == (80, 400)
assert prostokat(12, 10) == (44, 120)
assert rownoleglobok(6, 5, 2) == (22, 12)
assert rownoleglobok(10, 8, 7) == (36, 70)
assert romb(10, 5) == (40, 50)
assert romb(2, 3) == (8, 6)
assert trapez(10, 15, 7, 14, 2) == (46, 25)
assert trapez(9, 11, 6, 8, 3) == (34, 30)
# TODO na koniec! dopisz 2 testy dla kola i dla kazdej innej figury po jednym dodatkowym tescie
