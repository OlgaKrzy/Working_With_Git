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
