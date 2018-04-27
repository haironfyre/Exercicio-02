def questao1() :
    return print("", 5**2, 9 * 5, 15 / 12, 12 / 15, 15 // 12, 12 // 15, 5 % 2, 9 % 5, 15 % 12, 12 % 15, 6 % 6, 0 % 7)
questao1()

def questao2() :
    return print("Daqui a dois dias, as 5 da tarde o alarme irá tocar")
questao2()

def questao3() :
    print("Insira a hora atual")
    m = int(input())
    print("Insira o tempo de espera")
    n = int(input())
    x = (m+n)%24
    print("Hora atual: {}".format(m))
    print("Tempo de espera: {}".format(n))
    print("O alarme irá despertar às {} horas".format(x))
questao3()

def questao4(a,f):
    f = f+a
    t = f%30
    res = t%7
    return print("Mês =", t,"Dia da semana =", res)
questao4(2,7)


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
    return print("", 6 * (1 - 2))
questao11()

def questao2a() :
    print("Insira a quantidade de anos")
    t = int(input())
    js = 10000*((1+(0.08/12))**(12*t))
    return print("Valor final de juros após", t, "anos será:", js)
questao2a()

def questao33() :
    print("Digite o raio")
    r = float(input())
    a = (3.14*(r**2))
    return print("a área do círculo é:", a)
questao33()

def questao44() :
    print("Digite a base e altura")
    b = float(input())
    h = float(input())
    a = b*h
    return print("A área do retangulo é:", a)
questao44()

def questao55() :
    print("Insira os quilômetros percorridos:")
    km = int(input())
    print("Insira a quantidade de galosina consumida:")
    lt = float(input())
    con = km/lt
    return print("O consumo de gasolina por quilômetro é igual a:", con)
questao55()


def questao6() :
    print("Insira a temperatura em C")
    c = int(input())
    return print("Temperatura em Fº", (c*1.8)+32)
questao6()

def questao7() :
    print("Insira a temperatura em F")
    f = float(input())
    return print("Temperatura em Cº", (f-32)/1.8)
questao7()
