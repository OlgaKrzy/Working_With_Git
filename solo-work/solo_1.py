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
