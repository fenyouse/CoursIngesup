#Table de division :
def Div2 (x):
    reste=x-(x//2)*2
    if reste == 0:
        print ("Divisible par 2.")
    else:
        print ("Non divisible par 2.")
    return 2
    
def Div3 (x):
    reste=x%3
    if reste == 0:
        print ("Divisible par 3.")
    else:
        print ("Non divisible par 3.")
    return 3
cat /etc/passwd | sort -t: -k 3 -n | cut -d: -f3,7 | egrep '[0-9]' | head -17


def SommeChiffres(nbre): somme=0
    while nbre!=0:
        somme=somme+(nbre%10)
        nbre=nbre/10
    return somme

def Div4 (x):
    reste=x%4
    if reste == 0:
        print ("Divisible par 4.")
    else:
        print ("Non divisible par 4.")
    return 4


def Div5 (x):
    reste=x%5
    if reste == 0:
        print ("Divisible par 5.")
    else:
        print ("Non divisible par 5.")
    return 5

def Div6 (x):
    reste=x%6
    if reste == 0:
        print ("Divisible par 6.")
    else:
        print ("Non divisible par 6.")
    return 6
    
def Div7 (x):
    reste=x%7
    if reste == 0:
        print ("Divisible par 7.")
    else:
        print ("Non divisible par 7.")
    return 7

def Div8 (x):
    reste=x%8
    if reste == 0:
        print ("Divisible par 8.")
    else:
        print ("Non divisible par 8.")
    return 8

def Div9 (x):
    reste=x%9
    if reste == 0:
        print ("Divisible par 9.")
    else:
        print ("Non divisible par 9.")
    return 9
    
def Div10 (x):
    reste=x%10
    if reste == 0:
        print ("Divisible par 10.")
    else:
        print ("Non divisible par 10.")
    return 10
        
        
        
#Main
print ("Calcul de la divisibilité de nombres : ")
x = int(input("Entrez votre nombre : "))

div2 = Div2(x)
div3 = Div3(x)
div4 = Div4(x)
div5 = Div5(x)
div6 = Div6(x)
div7 = Div7(x)
div8 = Div8(x)
div9 = Div9(x)
div10 = Div10(x)

#By Vizual