from random import randint

oddelovac = "-" * 30
print ("Hi there!")
print(oddelovac)
print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
print(oddelovac)

def duplicates_check(number): #funkce ktera bude kontrolovat jestli vygenerovany cislo pomoci funkce "generate_number" nema v sobe stejne cisla vicekrat
    split_number = [int(i) for i in str(number)] #rozdeli cislo na jednotliva cisla
    if len(split_number) == len(set(split_number)): #zkontroluje jestli jsou cisla unikatni a neopakuji se
        return True
    else:
        return False
def generate_number(): #vygeneruje nahodne 4 mistne cislo
    while True:
        number = randint(1000,9999)
        if duplicates_check(number):
            return number

def cows_bulls():
    neuhadnuto = True
    number = str(generate_number()) #vezme vygenerovane cislo z funkce generate_number a premeni ho  na string aby type sedel se vstupem
    pocet_pokusu = 0
    while neuhadnuto: #while smycka na hadani cisel uzivatelem
        vstup = input("Enter a 4 digit number: ")
        pocet_pokusu += 1
        print(oddelovac)
        if len(vstup) == 4 and vstup.isdigit(): #zkontroluje jestli vstup od uzivatele obsahuje jen 4 znaky a vsechny jsou cisla
            split_vstup = [int(i) for i in vstup] #rozdeli vstup na jednotliva cisla na pozdeji for cyklus
            split_number = [int(i) for i in number] #rozdeli vygenerovane cislo na jednotliva cisla na pozdejsi for cyklus
            if vstup == number:
                neuhadnuto == False
                return (f"Correct, you have guessed the right number in {pocet_pokusu} guesses.")
            else:
                cows = 0 # cows = pokud uzivatel trefi hadane cislo ale ne primo i na jeho umisteni
                bulls = 0 # bulls = pokud uzivatel trefi hadane cislo a trefi se i na jeho umisteni
                for i in set(split_vstup): #for smycka na pocitani uhodnutych cisel a vypsani kolik cows a bulls uzivatel ma
                    if i in split_number and split_vstup.index(i) == split_number.index(i):
                        bulls += 1
                    elif i in split_number:
                        cows += 1
                if cows == 1 and bulls == 1:
                    print(f"Cow = {cows} and Bull = {bulls}")
                    print(oddelovac)
                elif cows == 1:
                    print(f"Cow = {cows} and Bulls = {bulls}")
                    print(oddelovac)
                elif bulls == 1:
                    print(f"Cows = {cows} and Bull = {bulls}")
                    print(oddelovac)
                else:
                    print(f"Cows = {cows} and Bulls = {bulls}")
                    print(oddelovac)
        else:
            print("Wrong number, try again")
            print(oddelovac)
    print(f"Cows = {cows} and Bulls = {bulls}")
print(cows_bulls())
