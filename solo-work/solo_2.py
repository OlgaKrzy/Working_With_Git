import math


class Trojkat:
    def __init__(self, a, b, c, h_a):
        self.a = a
        self.b = b
        self.c = c
        self.h_a = h_a

    def obwod(self):
        return self.a + self.b + self.c


moj_troj = Trojkat(5, 4, 3, 5.3)
print(moj_troj.obwod())


class Kolo:
    def __init__(self, r):
        self.r = r

    def obwod(self):
        return 2 * self.r * math.pi

    def pole(self):
        return math.pi * self.r**2


moje_kolo = Kolo(10)
print(moje_kolo.pole())
print(moje_kolo.obwod())


class Kwadrat:
    def __init__(self, a):
        self.a = a

    def obwod(self):
        return 4 * self.a

    def pole(self):
        return self.a * self.a


moj_kwadrat = Kwadrat(9)
print("Mój kwadrat ma pole: " + str(moj_kwadrat.pole()) + ", a jego obwod to: " + str(moj_kwadrat.obwod()))


class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pole(self):
        return self.a * self.b

    def obwod(self):
        return 2 * self.a + 2 * self.b


moj_prosto = Prostokat(4, 8)
print("Mój prostokat ma pole: " + str(moj_prosto.pole()) + ", a jego obwod to: " + str(moj_prosto.obwod()))


class Trapez:
    def __init__(self, a, b, c, d, h):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = h

    def pole(self):
        return (self.a * self.h)/2

    def obwod(self):
        return self.a + self.b + self.c + self.d


moj_trapez = Trapez(1, 2, 5, 4, 8)
print("Mój trapez ma pole " + str(moj_trapez.pole()) + ", a jego obwod to " + str(moj_trapez.obwod()))


class Student:
    def __init__(self, imie, nazwisko, index):
        self.imie = imie
        self.nazwisko = nazwisko
        self.index = index
        self.oceny = []

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.index}"

    def __int__(self):
        return 6

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def zwroc_srednia(self):
        return sum(self.oceny)/len(self.oceny)


student_Olga = Student("Olga", "Krzyczkowska", 129141)

# wskaźnik do obiektu w pamięci wirtualnej  -> nie jest to de facto wskaźnik: gdyby to był wskaźnik, to moglibyśmy pracować zarówno na wskaźniku jak i na obiekcie, na który wskazuje (dereferencji wskaźnika)

student_Olga.dodaj_ocene(4)
print(student_Olga)
print(student_Olga.zwroc_srednia())


class Pies:
    def __init__(self, imie, rasa, wiek, plec: bool, waga, BMI, can_make_more_selves: bool, mioty):
        self.imie = imie
        self.rasa = rasa
        self.wiek = wiek
        self.plec = plec
        self.waga = waga
        self.BMI = BMI
        self.can_make_more_selves = can_make_more_selves
        self.mioty = mioty

    def kastracja(self):
        if self.can_make_more_selves:
            self.can_make_more_selves = False
        else:
            print("Eggless already")

    def __int__(self):
        return self.BMI

    def fatness(self):
        if self.BMI > 30:
            print("Kliniczniak")
        elif self.BMI > 25:
            print("Tłustosz")
        elif self.BMI > 18:
            print("Dobra robota, panie Obajtek")
        else:
            print("Chonk that boy up")

    def __str__(self):
        return f"{self.imie} ma {self.wiek} lat/lata."


Fafik = Pies("Fafik", "Komondor", 5, True, 110, 50, True, 13)
print(Fafik.can_make_more_selves)
Fafik.kastracja()
print(Fafik.can_make_more_selves)

Fafika = Pies("Fafika", "Labłador", 14, False, 40, 24, True, 2)

print("Informacje o Fafiku: " + str(Fafik))
Fafik.fatness()

print("Informacje o Fafice: " + str(Fafika))
Fafika.fatness()
