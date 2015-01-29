# FONCTIONS

def NbLignes (M):
    return len(M)

def NbColonnes (M):    
    return len(M[0])

def ecrire_matrice (M):
    for ligne in M:
        print(ligne)

def TesterGenerale (nomTest, fctTest, M1, M2, resAttendu):
    resObtenu = fctTest (M1, M2)
    if resAttendu == resObtenu:
        print ("[OK] ",nomTest," !")
    else:
        print ("[ERREUR] ",nomTest,"... ")
        print("attendu :")
        ecrire_matrice(resAttendu)
        print("obtenu :")
        ecrire_matrice(resObtenu)
        
# Matrice nulle de taille n
def MatriceNulle (n):
    M=[]
    for i in range (0,n):    
        M.append([0] * n)
    return M

def TesterMatriceNulle ():
    n = 3
    resAttendu = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
    resObtenu = MatriceNulle (n)
    if resAttendu == resObtenu:
        print ("[OK] TesterMatriceNulle !")
    else:
        print ("[ERREUR] TesterMatriceNulle... ")

# Matrice identité
def MatriceIdentite (n):
    M=[]
    for i in range (0,n):    
        M.append([0] * n)
        M[i][i] = 1
    return M

def TesterMatriceIdentite ():
    n = 3
    resAttendu = [[1,0,0],
                  [0,1,0],
                  [0,0,1]]
    resObtenu = MatriceIdentite (n)
    if resAttendu == resObtenu:
        print ("[OK] TesterMatriceIdentite !")
    else:
        print ("[ERREUR] TesterMatriceIdentite... ")


# Matrice transposée
def MatriceTransposee (M):
    Mtrans = []    
    
    # recopie des elements de M inversés
    for i in range(0,NbColonnes(M)):
        Mtrans.append ([0] * NbLignes(M));
        for j in range(0,NbLignes(M)):
            Mtrans[i][j] = M[j][i]
    return Mtrans

def TesterMatriceTransposeeDUneMatriceCarree ():
    M = [[1,2,3],
         [4,5,6],
         [7,8,9]]
    
    resAttendu = [[1,4,7],
                  [2,5,8],
                  [3,6,9]]
    
    resObtenu = MatriceTransposee (M)
    if resAttendu == resObtenu:
        print ("[OK] TesterMatriceTransposeeDUneMatriceCarree !")
    else:
        print ("[ERREUR] TesterMatriceTransposeeDUneMatriceCarree... ")
        print("attendu :")
        ecrire_matrice(resAttendu)
        print("obtenu :")
        ecrire_matrice(resObtenu)
        

def TesterMatriceTransposeeDUneMatricePasCarree ():
    M = [[1,2,3],
         [4,5,6],
         [7,8,9],
         [10,11,12]]
    resAttendu = [[1,4, 7, 10],
                  [2,5, 8, 11],
                  [3,6, 9, 12]]
    
    resObtenu = MatriceTransposee (M)
    if resAttendu == resObtenu:
        print ("[OK] TesterMatriceTransposeeDUneMatricePasCarree !")
    else:
        print ("[ERREUR] TesterMatriceTransposeeDUneMatricePasCarree... ")
        print("attendu :")
        ecrire_matrice(resAttendu)
        print("obtenu :")
        ecrire_matrice(resObtenu)

# Somme de deux matrices 
def SommeMatrices (M1, M2):
    if NbLignes(M1) != NbLignes(M2) or NbColonnes(M1) != NbColonnes(M2):
        return []

    Msomme = []
    # recopie des sommes des elements de M1 et M2
    for i in range(0, NbLignes(M1)):
        Msomme.append ([0] * NbColonnes(M1));
        for j in range(0,NbColonnes(M1)):
            Msomme[i][j] = M1[i][j] +  M2[i][j]
    return Msomme

def TesterSommeMatricesDeTaillesDifferentes ():
    M1 = [[1,2,3],
         [4,5,6]]
    M2 = [[1,2],
          [3,4],
          [5,6]]
             
    resAttendu = [] # somme impossible
    TesterGenerale ("TesterSommeMatricesDeTaillesDifferentes", SommeMatrices, M1, M2, resAttendu)
    
def TesterSommeMatricesCarrees ():
    M1 = [[1,2,3],
          [4,5,6],
          [7,8,9]]
    M2 = [[9,8,7],
          [6,5,4],
          [3,2,1]]
            
    resAttendu = [[10,10,10],
                  [10,10,10],
                  [10,10,10]]
    TesterGenerale ("TesterSommeMatricesCarrees", SommeMatrices, M1, M2, resAttendu)
  
def TesterSommeMatricesPasCarrees ():
    M1 = [[1,2,3],
          [4,5,6]]
    M2 = [[9,8,7],
          [6,5,4]]            
    resAttendu = [[10,10,10],
                  [10,10,10]]
    TesterGenerale ("TesterSommeMatricesPasCarrees", SommeMatrices, M1, M2, resAttendu)  

# Somme de deux matrices 
def ProduitMatrices (M1, M2):
    if NbColonnes(M1) != NbLignes(M2):
        return []

    Mproduit = []
    # recopie des sommes des elements de M1 et M2
    for i in range(0, NbLignes(M1)):
        Mproduit.append ([0] * NbColonnes(M2));        
        for j in range(0,NbColonnes(M2)):
            somme=0
            for k in range(0,NbColonnes(M1)):
                somme = somme + M1[i][k] *  M2[k][j]
            Mproduit[i][j] = somme
    return Mproduit

def TesterProduitMatricesDeTaillesDifferentes ():
    M1 = [[1,2,3],
         [4,5,6]]
    M2 = [[1,2],
          [3,4]]            
    resAttendu = [] # somme impossible
    TesterGenerale ("TesterProduitMatricesDeTaillesDifferentes", ProduitMatrices, M1, M2, resAttendu)
  

def TesterProduitMatriceLigneParMatriceColonne ():
    M1 = [[1,2,3]]          
    M2 = [[1],
          [2],
          [3]]            
    resAttendu = [[14]]
    TesterGenerale ("TesterProduitMatriceLigneParMatriceColonne", ProduitMatrices, M1, M2, resAttendu)

def TesterProduitMatriceParMatriceColonne ():
    M1 = [[1,2,3],
          [4,5,6]]          
    M2 = [[1],
          [2],
          [3]]            
    resAttendu = [[14],
                  [32]]    
    TesterGenerale ("TesterProduitMatriceParMatriceColonne", ProduitMatrices, M1, M2, resAttendu)      

def TesterProduitMatriceLigneParMatrice ():
    M1 = [[1,2,3]]          
    M2 = [[1, 2],
          [3, 4],
          [5, 6]]            
    resAttendu = [[22, 28]]
    TesterGenerale ("TesterProduitMatriceLigneParMatrice", ProduitMatrices, M1, M2, resAttendu)   
        
def TesterProduitMatricesCarrees ():
    M1 = [[1,2,3],
          [4,5,6],
          [7,8,9]]
    M2 = [[9,8,7],
          [6,5,4],
          [3,2,1]]             
    resAttendu = [[30,24,18],
                  [84,69,54],
                  [138,114,90]]    
    TesterGenerale ("TesterProduitMatricesCarrees", ProduitMatrices, M1, M2, resAttendu)   
        
def TesterProduitMatricesPasCarrees ():
    M1 = [[1,2,3],
          [4,5,6]]          
    M2 = [[1, 2],
          [3, 4],
          [5, 6]]             
    resAttendu = [[22, 28],
                  [49,64]]
    TesterGenerale ("TesterProduitMatricesPasCarrees", ProduitMatrices, M1, M2, resAttendu)
   
# MAIN
TesterMatriceNulle()
TesterMatriceIdentite()

TesterMatriceTransposeeDUneMatriceCarree ()
TesterMatriceTransposeeDUneMatricePasCarree ()

TesterSommeMatricesDeTaillesDifferentes ()
TesterSommeMatricesCarrees()
TesterSommeMatricesPasCarrees()

TesterProduitMatricesDeTaillesDifferentes()
TesterProduitMatriceLigneParMatriceColonne()
TesterProduitMatriceParMatriceColonne ()
TesterProduitMatriceLigneParMatrice ()
TesterProduitMatricesCarrees()
TesterProduitMatricesPasCarrees()
