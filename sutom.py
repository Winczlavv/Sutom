def wordfinder(N,W,C):
    # ON PASSE EN INDICE 0 TOUS LES MOTS NE CONTENANT PAS LES LETTRES EXACTES AU BON ENDROIT (dans W)
    for j in range(len(C)):
        if C[j][1] == "2":
            for k in range(len(W)):
                if int(W[k][1])==1:
                    wo = W[k][0]
                    if str(wo[j])!=str(C[j][0]):
                        W[k][1] = 0 
    print("Apres les suppressions des 2 : ",W)
    # ON SUPPRIME LES MOTS NE CONTENANT PAS LES LETTRES EXACTES AU BON ENDROIT (on créé une nvlle liste X à partir de W)
    X = []  
    for u in range(len(W)):
        if W[u][1]=="1":
            X.append([W[u][0],1])
    
    # ON COPIE LA LISTE
    Y = []
    for s in range(len(X)):
        Y.append([X[s][0],X[s][1]])
    # ON CREE UNE NOUVELLE LISTE NE CONTENANT PAS LES LETTRES AU BON ENDROIT (on copie X puis on la modif)
    for j in range(len(C)):
        if C[j][1] == "2":
            for k in range(len(Y)):
                Y[k][0] = Y[k][0][:j] +"_"+Y[k][0][j+1:]

    # ON CREE LA NVLLE MATRICE 
    D = []
    for l in range(len(C)):
        if C[l][1]!="2":
            D.append([C[l][0],C[l][1]])
        else:
            D.append(["_",2])

    for k in range(len(D)):
        numLetterPresence = 0
        LetterPresenceIndication = 0
        # ON CHECK SI LA LETTRE EST UNIQUE
        for l in range(len(D)):
            if D[k][0]!="_":
                if D[k][0] == D[l][0]:
                    numLetterPresence+=1
                    LetterPresenceIndication+=int(D[l][1])
        # SI ELLE EST UNIQUE, ON DELETE TOUS LES MOTS QUI EN CONTIENNENT UNE SI INDICE 0, ON DELETE CEUX QUI NEN CONTIENNENT PAS SI INDICE 1
        if numLetterPresence==1:
            if int(D[k][1]) == 0:
                for m in range(len(Y)):
                    wo = Y[m][0]
                    for n in range(len(wo)):
                        if wo[n]==D[k][0]:
                            X[m][1] = 0  #Tous les mots contenant cette lettre sont supprimés
            if int(D[k][1]) == 1:
                for m in range(len(Y)):
                        if D[k][0] not in Y[m][0]:
                            X[m][1] = 0 #Tous les mots ne contenant pas cette lettre sont supprimés
                        else:
                            wo = Y[m][0]
                            for n in range(len(wo)):
                                if D[k][0] == wo[n]:
                                    if n == k:
                                        X[m][1] = 0 #Tous les mots contenant la lettre au bon endroit exact sont supprimés
        #On cherche maintenant dans le cas où l'indicateur est différent de 1
        if numLetterPresence >1:
            for m in range(len(Y)):
                Indicator = 0
                wo = Y[m][0]
                for n in range(len(wo)):
                    if wo[n] == D[k][0]:
                        Indicator+=1
                if LetterPresenceIndication != Indicator:
                    X[m][1] = 0 #S'il n'y a pas le nombre de lettres qu'il devrait y avoir, on supprime le mot
                if D[k][1] == 1:
                    for p in range(len(wo)):
                        if D[k][0] == wo[p]:
                            if n == k:
                                X[m][1] = 0 #Si l'indice est de 1, si la lettre est au bon endroit, alors on supprime le mot

    Z = []  
    for u in range(len(X)):
        if int(X[u][1])==1:
            Z.append([X[u][0],1])
    return tri(N,Z)


def Chain(N,W):
    letters = str(input("Votre mot : "))
    occurences = str(input("Les numéros correspondant à la présence des lettres : "))
    letters = letters.upper()
    C = []
    L = list(letters)
    O = list(occurences)
    if len(L)!=len(O) or len(L)!=N:
        print("Les informations données ne correspondent pas. Merci de réessayer.\n----------\n")
        ask_question()
    for i in range(len(L)):
        C.append([L[i],O[i]])
    wordfinder(N,W,C)

def questions(N,W):
    print("Donnez nous désormais les résultats donnés par SUTOM. Indiquez d'abord le mot, puis si les lettres sont présentes dans le mot à trouver")
    print("2 : lettre correctement placée / 1 : lettre présente mais mal placée / 0 : lettre absente. Indiquez les lettres DANS L'ORDRE")
    print("Exemple pour le mot 'Flambi' : Si F et M sont bien placés, que A est mal placé, et que L,B et I sont absents :")
    print("Ecrivez d'abord 'Flambi' puis '201200'")
    Chain(N,W)


def ask_question():
    N = int(input("De combien de caractères est composé le mot que tu dois deviner ? "))
    if N<=0:
        print("mauvaise valeur indiquée")
        ask_question()
    else:
        print("Les questions vont commencer. Merci de tester une première fois un mot contenant le plus de lettres différentes.")
        W = []
        f=open('words.txt','r')
        for i in range(149443):
            ligne = f.readline()
            ligne = ligne.rstrip("\n")
            ligne = ligne.split(",")
            if len(ligne[0]) == N:
                W.append(ligne)
        f.close()        
        return questions(N,W)


        
def find_word():
    print("Salut à toi !")
    print("=============")
    return ask_question()

def tri(N,Z):
    for u in range(len(Z)):
        wo = Z[u][0]
        lon = len(wo)-1
        if wo[lon] == "S":
            Z[u][1] = 3

        if wo[lon] == "E" and wo[lon-1] == "E":
            Z[u][1] = 4

        if wo[lon] == "S" and wo[lon-1] == "N" and wo[lon-2] == "O":
            Z[u][1] = 9
        if wo[lon] == "T" and wo[lon-1] == "N" and wo[lon-2] == "E":
            Z[u][1] = 9

        if wo[lon] == "Z" and wo[lon-1] == "E":
            Z[u][1] = 10
        if wo[lon] == "T" and wo[lon-1] == "I" and wo[lon-2] == "A":
            Z[u][1] = 10
        if wo[lon] == "S" and wo[lon-1] == "I" and wo[lon-2] == "A":
            Z[u][1] = 10
        if wo[lon] == "A" and wo[lon-1] == "R" and wo[lon-2] == "E":
            Z[u][1] = 10
        if wo[lon] == "S" and wo[lon-1] == "E" and wo[lon-2] == "E":
            Z[u][1] = 10
        if wo[lon] == "I" and wo[lon-1] == "A" and wo[lon-2] == "R" and wo[lon-3] == "E":
            Z[u][1] = 10
        if wo[lon] == "S" and wo[lon-1] == "I" and wo[lon-2] == "A" and wo[lon-3] == "R" and wo[lon-4] == "E":
            Z[u][1] = 10
        if wo[lon] == "T" and wo[lon-1] == "I" and wo[lon-2] == "A" and wo[lon-3] == "R" and wo[lon-4] == "E":
            Z[u][1] = 10

        if wo[lon] == "S" and wo[lon-1] == "E" and wo[lon-2] == "M" and wo[lon-3] == "A":
            Z[u][1] = 11    
        if wo[lon] == "S" and wo[lon-1] == "E" and wo[lon-2] == "T" and wo[lon-3] == "A":
            Z[u][1] = 11    
        if wo[lon] == "S" and wo[lon-1] == "E" and wo[lon-2] == "T" and wo[lon-3] == "I":
            Z[u][1] = 11   
    Z.sort(key=lambda x:x[1],reverse=False)
    return annonceFin(N,Z)

def annonceFin(N,Z):
    print("\n\n\n\n\n\n\n\n<======================================================================>\n\n\n")
    if len(Z) > 0:
        print("Après un rapide tri, dans l'odre de probabilité, voici les mots possibles :\n\n")
        print("-", Z[0][0])
        for i in range(1,len(Z)):
            if Z[i][1] != Z[i-1][1]:
                print("\n")
            print("-", Z[i][0])
    else:
        print("Il y a peut-être eu une erreur lors du procédé, mais nous n'avons trouvé aucune correspondance.")
        print("Merci de réessayer. \n\n")
        print("Si le problème persiste, merci de contacter un administrateur.")
    print("\n\n\n<======================================================================>")
    print("\n\n\n")
    print("Entrez 0 pour arrêter le processus, 1 pour le continuer, 2 pour le recommencer\n")
    choicerestart(N,Z)
    print("\n\n\n")

def resetValues(N,Z):
    for i in range(0,len(Z)):
        Z[i][1] = "1"
    return Chain(N,Z)
def choicerestart(N,Z): 
    choix = input("Votre choix : ")
    if choix == "0": print("Vous avez choisi d'arrêter le programme."); return
    if choix == "1": print("Vous avez choisi de continuer le programme."); return resetValues(N,Z)
    if choix == "2": print("Vous avez choisi de recommencers le programme."); return find_word()
    else: return choicerestart(N,Z)

find_word()
