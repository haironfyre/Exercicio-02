def questao1() :
    print("", 5**2, 9 * 5, 15 / 12, 12 / 15, 15 // 12, 12 // 15, 5 % 2, 9 % 5, 15 % 12, 12 % 15, 6 % 6, 0 % 7)
questao1()

def questao2() :
    print("Daqui a dois dias, as 5 da tarde o alarme irá tocar")
questao2()

def questao3() :
    m = int(input())
    n = int(input())
    x = (m+n)%24
    print("Hora atual: {}".format(m))
    print("Tempo de espera: {}".format(n))
    print("O alarme irá despertar às {} horas".format(x))
questao3()

def questao5() :
    a1 = str("Só")
    a2 = str("trabah1o")
    a3 = str("sem")
    a4 = str("diversao")
    a5 = str("faz")
    a6 = str("de")
    a7 = str("João")
    a8 = str("em")
    a9 = str("chato")
    return print("", a1, a2, a3, a4, a5, a6, a7, a8, a9)
questao5()

def questao11() :
    print("", 6 * (1 - 2))
questao11()

def questao2a() :
    t = int(input())
    js = 10000*((1+(0.08/12))**(12*t))
    return print("", js)
questao2a()

def questao33() :
    print("Digite o raio")
    r = float(input())
    a = (3.14*(r**2))
    return print("", a)
questao33()

def questao44() :
    print("Digite a base e altura")
    b = float(input())
    h = float(input())
    a = b*h
    return print("", a)
questao44()

def questao55() :
    km = int(input())
    lt = float(input())
    con = km/lt
    return print("", con)
questao55()


def questao6() :
    print("Insira a temperatura em C")
    c = int(input())
    print("", (c*1.8)+32)
questao6()

def questao7() :
    print("Insira a temperatura em F")
    f = float(input())
    print("", (f-32)/1.8)
questao7()
