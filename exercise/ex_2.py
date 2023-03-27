# kwadrat
import math
a = 10
obwod = a * 4
pole = a*a

#Obwód kwadratu wynosi 40, a pole 100

print("Obwód kwadratu wynosi: " + str(obwod) +", a pole " + str(pole) + ".")

#prostokąt

b = 10
c =  15
obwod_pr = 2*b + 2*c
pole_pr = b*c
print("Obwód prostokątu wynosi: " + str(obwod_pr) +", a pole " + str(pole_pr) + ".")

#koło
zmienna_pi = math.pi
r = 5
pole_kolo = zmienna_pi*(r^2)
obwod_kolo = 2*zmienna_pi*r
print("Obwód koła wynosi: " + str(obwod_kolo) +", a pole " + str(pole_kolo) + ".")

#trapez

d = 9
e = 4
f = 6
g = 5

pole_trapez = (d * e) / 2
obwod_trapez = d + e + f + g
print("Obwód trapezu wynosi: " + str(obwod_trapez) +", a pole " + str(pole_trapez) + ".")
#romb

h_wys = 5
a = 10

pole_rombu = a*h_wys
obwod_rombu = a*4

print("Obwód rombu wynosi: " + str(obwod_rombu) +", a pole " + str(pole_rombu) + ".")