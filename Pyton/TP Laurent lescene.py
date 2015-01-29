

def ChercherPremierDiviseur(nombre):
    
    div = 1
    reste = 1
    
    while reste != 0 :
        div = div+1
        reste = nombre%div
    
    return div   
    

def DecomposerFacteursPremiers(nombre):
    
    compte = []
    
    while nombre > 1 :
        pdiv = ChercherPremierDiviseur(nombre)
        nombre = nombre//pdiv
        compte = compte + [pdiv]
    
    return compte


def EstCeQueCherchePremierDiviseurDe45Fonctionne() :
    
    print ("La recherche du premier diviseur par 45 fonctionne ?", end=" : ")
    
    nombre = 45
    resultatObtenu = ChercherPremierDiviseur(nombre)
    resultatAttendu = 3
    
    if (resultatObtenu == resultatAttendu):
        print ("true")
    
    else :
        print ("false")

def EstCeQueCherchePremierDiviseurDe17Fonctionne() :
    
    print ("La recherche du premier diviseur par 17 fonctionne ?", end=" : ")
    
    nombre = 17
    resultatObtenu = ChercherPremierDiviseur(nombre)
    
    if (resultatObtenu == nombre):
        print ("true")
    
    else :
        print ("false")

def EstCeQueLaDecompositionEnFacteursPremiersDe45Fonctionne() :
    
    print ("La decomposition en facteurs premiers de 45 ", end=" : ")
    
    nombre = 45
    resultatObtenu = DecomposerFacteursPremiers(nombre)
    resultatAttendu = [3, 3, 5]
    
    if (resultatObtenu == resultatAttendu):
        print ("true")
    
    else :
        print ("false")

def EstCeQueLaDecompositionEnFacteursPremiersDe17Fonctionne() :
    
    print ("Decomposition en facteurs premiers de 17 fonctionne ?", end=" : ")
    
    nombre = 17
    resultatObtenu = DecomposerFacteursPremiers(nombre)
    resultatAttendu = [17]
    
    if (resultatObtenu == resultatAttendu):
        print ("true")
    
    else :
        print ("false")


EstCeQueCherchePremierDiviseurDe45Fonctionne()

EstCeQueLaDecompositionEnFacteursPremiersDe45Fonctionne()

EstCeQueCherchePremierDiviseurDe17Fonctionne()

EstCeQueLaDecompositionEnFacteursPremiersDe17Fonctionne()

