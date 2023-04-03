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
def rownoleglobok(bok_a, bok_b, wysokosc_a):
    # TODO
    return 0, 0

def romb(bok, wysokosc):
    # TODO
    return 0, 0

# trapez i kolo dla studenta 3
def trapez(bok_a, bok_b, bok_c, bok_d, wysokosc_a):
    # TODO
    return 0, 0


def kolo(promien):
    # TODO
    return 0, 0


assert trojkat(10, 15, 16, 8) == (41, 40)
assert kwadrat(20) == (80, 400)
assert prostokat(12, 10) == (44, 120)
assert rownoleglobok(6, 5, 2) == (22, 12)
assert romb(10, 5) == (40, 50)
assert trapez(10, 15, 7, 14, 2) == (45, 25)
# TODO na koniec! dopisz 2 testy dla kola i dla kazdej innej figury po jednym dodatkowym tescie
