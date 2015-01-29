# Decomposition en facteurs premiers

''' rechercher_premier_diviseur
recherche (à partir de 2) le premier diviseur nombre fourni
si le nombre est prenier, la fonction retournera le nombre lui-même
'''
def rechercher_premier_diviseur(n):
    diviseur = 2
    reste = n % diviseur
    while reste != 0 :
        diviseur = diviseur + 1
        reste = n % diviseur
    return diviseur

''' Fonction de tests générique '''
def TesterRecherchePremierDiviseur(n, resultatAttendu) :
    resultatObtenu = rechercher_premier_diviseur(n)
    if (resultatObtenu == resultatAttendu):
        print ("[OK] ", end="")
    else :
        print ("[ERREUR]", end="")
    print ("Est Ce Que La Recherche De Premier Diviseur De ",n," Fonctionne ?")    
    
''' les deux tests effectués '''
def EstCeQueRecherchePremierDiviseurDe45Fonctionne() :
    TesterRecherchePremierDiviseur(45, 3)

def EstCeQueRecherchePremierDiviseurDe17Fonctionne() :
    TesterRecherchePremierDiviseur(17, 17)


''' decomposer_facteurs_premiers
renvoie la décomposition en facteurs premiers du nombre fourni
pour cela, on utilise en boucle la fonction rechercher_premier_diviseur
'''
def decomposer_facteurs_premiers(n):
    lesDiviseurs = []
    if n < 2 :
        lesDiviseurs = [n]
    else:        
        while n > 1 :
            diviseur = rechercher_premier_diviseur(n)
            n = n // diviseur
            lesDiviseurs.append (diviseur)
    return lesDiviseurs

''' Fonction de test générique '''
def TesterDecompositionEnFacteursPremiers(n, resultatAttendu) :
    resultatObtenu = decomposer_facteurs_premiers(n)
    if (resultatObtenu == resultatAttendu):
        print ("[OK] ", end="")
    else :
        print ("[ERREUR]", end="")
    print ("Est Ce Que La Decomposition En Facteurs Premiers De ",n," Fonctionne ?")

''' les deux tests effectués '''    
def EstCeQueLaDecompositionEnFacteursPremiersDe45Fonctionne() :    
    TesterDecompositionEnFacteursPremiers (45, [3, 3, 5])    

def EstCeQueLaDecompositionEnFacteursPremiersDe17Fonctionne() :    
    TesterDecompositionEnFacteursPremiers (17, [17])


# programme principal
EstCeQueRecherchePremierDiviseurDe45Fonctionne()
EstCeQueLaDecompositionEnFacteursPremiersDe45Fonctionne()
EstCeQueRecherchePremierDiviseurDe17Fonctionne()
EstCeQueLaDecompositionEnFacteursPremiersDe17Fonctionne()

