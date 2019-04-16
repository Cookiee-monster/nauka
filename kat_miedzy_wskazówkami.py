def input_data(tekst):
    return input(tekst)

def kat_godziny(godzina, minuta):
    return godzina * 30 + minuta * 0.5

def kat_minuty(minuta):
    return  minuta * 6

godzina = int(input_data("Podaj godzinę"))
minuta = int(input_data("Podaj minutę"))

kat_godzinowy = kat_godziny(godzina, minuta)
kat_minutowy = kat_minuty(minuta)

kat = abs(kat_godzinowy - kat_minutowy)

print("Kąt pomiędzy wskazówkami dla godziny {}:{} wynosi {} stopni".format(godzina, minuta, kat))
