class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = wynagrodzenie_brutto

    @property
    def wynagrodzenie_netto(self) -> float:
        skladka_emerytalna = round(self.wynagrodzenie_brutto * 0.0976, 2)
        skladka_rentowa = round(self.wynagrodzenie_brutto * 0.015, 2)
        skladka_chorobowa = round(self.wynagrodzenie_brutto * 0.0245, 2)
        podstawa_skladki_zdrowotnej = self.wynagrodzenie_brutto - \
            skladka_emerytalna - skladka_rentowa - skladka_chorobowa
        skladka_zdrowotna = round(podstawa_skladki_zdrowotnej * 0.09, 2)
        kwota_zmiejszajaca_podatek = 300
        podstawa_opodatkowania = self.wynagrodzenie_brutto - \
            skladka_emerytalna - skladka_rentowa - skladka_chorobowa
        zaliczka_na_podatek = round(
            (podstawa_opodatkowania * 0.12) - kwota_zmiejszajaca_podatek, 2)

        return self.wynagrodzenie_brutto - skladka_emerytalna - skladka_rentowa - skladka_chorobowa - skladka_zdrowotna - zaliczka_na_podatek

    @property
    def calkowity_koszt(self) -> float:
        skladka_emerytalna = round(self.wynagrodzenie_brutto * 0.0976)
        skladka_rentowa = round(self.wynagrodzenie_brutto * 0.065)
        skladka_wypadkowa = round(self.wynagrodzenie_brutto * 0.0167)
        fundusz_pracy = round(self.wynagrodzenie_brutto * 0.0245)
        fgsp = round(self.wynagrodzenie_brutto * 0.001)

        return self.wynagrodzenie_brutto + skladka_emerytalna + skladka_rentowa + skladka_wypadkowa + fundusz_pracy + fgsp


with open('pracownicy.csv', 'r', encoding='utf-8') as csv_data_file:
    pracownicy = [Pracownik(line[0], line[1], float(line[2])) for line in [line.split(',') for line in csv_data_file.readlines()[1:]]]
    koszt_pracodawcy = sum([pracownik.calkowity_koszt for pracownik in pracownicy])

print(f'Całkowity koszt pracodawcy: {koszt_pracodawcy}')

for pracownik in pracownicy:
    print(f'Koszt pracownika {pracownik.imie} {pracownik.nazwisko} dla pracodawcy: {pracownik.calkowity_koszt}')

