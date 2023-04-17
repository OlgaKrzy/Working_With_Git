# zadanie 1.1

hello = "Hello {}"
student = "Ola"

print(hello.format(student))

# zadanie 1.2

student = input("Wpisz swoje imie")
hello = "Hello {}"
print(hello.format(student))

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]
liczba_studentow = str(len(studenci))
print("Liczba studentow wynosi: " + liczba_studentow)

# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]
for name in studenci:
    print("Hello " + name)

# zadanie 1.5

liczba = 3
potega = 4

wynik = liczba ** potega

print("Wynik wynosi: " + str(wynik))

# zadanie 1.6

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count("(")
print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

# zadanie 1.7

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort()
print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

# zadanie 1.8

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort(key= lambda k: k.split()[-1])
print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

# zadanie 1.9

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
liczba_n = 0
for student in studenci:
    last_name=student.split()[-1]
    if last_name.startswith("N"):
        liczba_n += 1
print("Liczba studentow na N wynosi: " + str(liczba_n))

# zadanie 1.10


def subtract_vectors(list_a, list_b):
    result = []
    for item_a, item_b in zip(list_a, list_b):
        result.append(item_b - item_a)
    return result


def are_vectors_equal(list_a, list_b):
    result = True
    for item_a, item_b in zip(list_a, list_b):
        if item_a != item_b:
            result = False
    return result


wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]


wykres_1_funkcja_liniowa = are_vectors_equal(subtract_vectors(wykres_1[0], wykres_1[1]), subtract_vectors(wykres_1[1], wykres_1[2]))
wykres_2_funkcja_liniowa = are_vectors_equal(subtract_vectors(wykres_2[0], wykres_2[1]), subtract_vectors(wykres_2[1], wykres_2[2]))
wykres_3_funkcja_liniowa = are_vectors_equal(subtract_vectors(wykres_3[0], wykres_3[1]), subtract_vectors(wykres_3[1], wykres_3[2]))

if wykres_1_funkcja_liniowa:
    print("Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_1 nie mozna wyznaczyc funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_2 nie mozna wyznaczyc funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktow w wykres_3 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.")
