
def main():
    # Cream o lista cu toate literele din alfabetul romanesc, pentru a le folosi la joc, vocalele primele
    alfabet = ['A', 'Ă', 'Â', 'E', 'I', 'Î', 'O', 'U', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'Ș', 'T', 'Ț', 'V', 'W', 'X', 'Y', 'Z']
    
    # Deschidem fisierul si luam datele din el. In lista 'jocuri', pe fiecare pozitie va fi un rand din fisierul .txt deschis.
    nume_fisier = "cuvinte_de_verificat.txt"
    with open(nume_fisier, 'r', encoding='utf-8-sig') as fisier:
        jocuri = fisier.readlines()
    
    # Cream variabila incercari in care vom monitoriza cate incercari facem ca sa ghicim toate cuvintele
    incercari = 0
    
    # Cream lista 'pozitii' in care vom salva pozitiile la care apare o litera in cuvant
    pozitii = []
    
    # Iteram printre jocuri
    # Pentru fiecare joc din fisierul .txt, separam cuvintele la ';' ca sa putem folosi separat id-ul jocului, cuvant partial si cuvant intreg
    for joc in jocuri:
        # Pe fiecare pozitie va fi un sir de caractere de forma joc = "1;******RA**;ICONOGRAFĂ\n"
        
        # Scapam de caracterul newline (\n) de la finalul fiecarei linie citite
        new = joc.strip("\n")
        
        # Separam sirul de caractere in functie de caracterul ';'. Astfel vom avea joc = ['1', '******RA**', 'ICONOGRAFĂ']
        joc = new.split(";")
        
        # Deoarece sirurile de caractere nu pot fi modificate, transformam cuvantul partial in lista ca sa il putem modifica. 
        # joc[1]= ['*', '*', '*', '*', '*', '*', 'R', 'A', '*', '*']
        cuvant_nou = list(joc[1])
        
        # Pt fiecare joc, incercam literele pe rand
        for litera in alfabet:
            
            # Daca litera nu e deja in cuvantul partial
            if litera not in joc[1]:
                # Crestem cu 1 numarul de incercari
                incercari = incercari + 1
                
                # Daca litera este buna, ii cautam pozitiile in care apare in cuvantul normal, ca sa stim unde sa completam in cuvantul partial
                if litera in joc[2]:
                    for i in range(len(joc[2])):
                        if joc[2][i] == litera:
                            pozitii.append(i)
                    
                    # Pentru toate pozitiile gasite, completam litera in cuvantul partial. 
                    for i in range(len(joc[1])):
                        if i in pozitii:
                            cuvant_nou[i] = litera
                    
                    # Transformam cuvantul partial din lista inapoi in sir de caractere
                    joc[1] = ''.join(str(caracter) for caracter in cuvant_nou)
                    
                # Verificam daca am completat cuvantul partial de tot. Daca da, nu mai incercam si cu celelalte litere
                if joc[1] == joc[2]:
                    print(joc[1])
                    break
            
            # Golim lista 'pozitii' ca sa fie pregatita pentru cuvantul urmator
            pozitii = []
    
    print(incercari)
    

if __name__ == "__main__":
    main()
    # Rezultat pentru fisierul dat: 2253 incercari