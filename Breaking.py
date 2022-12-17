import requests
x = "abcdefghijklmnoprstuwyzqxv?.<>,!1:234567890_/*-+()'!@#$%^&=;' "
alfabet = ["zxcvbnmasdfghjklqwertyuiop"]
r = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
#print(r)
soup = (r.text)
soup = soup.split('\n')           
soup = soup[0:-1]    #2 słowa mają 1 litere, 396 ma 2, 678 ma 3, 1127 ma 4, 1379 ma 5, 1504 ma 6, 1468 ma7, 1162 ma 8, 909 ma 9...

letters = []
for i in x:
    letters.append(i)
for i in soup:
    if len(i) == 1:
        soup.remove(i)
soup.append('a')
soup.append('i')
PotSen = []

def breaker(A):
    amount = {}
    count = 3
    Key1 = []
    Key2 = []
    Words = []
    KeyLetters1 = {}
    for i in letters:
        amount[i] = A.count(i)    #Dla każdego znaku w haśle zlicza jego ilość
    MaxValue = max(amount.values())  #MaxValue = ilość tej litery
    MostCommon = []
    for i in amount:
        if amount.get(i) == MaxValue:
            MostCommon.append(i)     #litera której jest najwiecej
    for i in MostCommon:
        PotSen.append(A.split(i))    #Potencjalna sentencja wyrazów
    for Sentence in PotSen:          #Jeśli powstanie zdanie mające 0-literowe wyrazy to
        for Word in Sentence:        #sentencja jest odrzucana
            if len(Word) == 0:
                PotSen.remove(Sentence)
                break
    for Sentence in PotSen:                         
        if Sentence[0][0] == str(MostCommon):
            PotSen.remove(Sentence)
            break                               #Jeśli znak uchodzący za spacje jest na końcu lub początku zdania 
    for Sentence in PotSen:                     #To znaczy, że nie może być spacją, a potencjalne zdanie
        if Sentence[-1][-1] == str(MostCommon): #jest odrzucane
            PotSen.remove(Sentence) 
            break               
    Moment = Sentence
    for Sentence in PotSen:
        for Word in Sentence:
            if len(Word) == 1:
                Key1 = Word
                Sentence.remove(Word)
                break
            elif len(Word) == 2:                #Tworzenie hierarchi według której program wybierze najlepsze
                Key1 = Word
                Sentence.remove(Word)
                break                                          #pierwsze słowo do rozpoczęcia łamania 
            elif len(Word) == 4 and len(Word) > len(set(Word)):     #kodu
                Key1 = Word
                Sentence.remove(Word)
                break
            elif len(Word) == 3:
                Key1 = Word
                Sentence.remove(Word)
                break
            elif len(Word) == 5 and len(Word) > len(set(Word)):
                Key1 = Word
                Sentence.remove(Word)
                break
            elif len(Word) == 4:
                Key1 = Word
                Sentence.remove(Word)
                break
            elif len(Word) == 6 and len(Word) > len(set(Word)):
                Key1 = Word
                Sentence.remove(Word)
                break
            elif len(Word) == 5:
                Key1 = Word
                Sentence.remove(Word)
                break       
        for Sentence in PotSen:
            for Word in Sentence:
                for Letter in Word:
                    KeyLetters1[Letter] = Key1.count(Letter)
                if KeyLetters1.get(Letter) > 2:
                    WspolnyZnak = Letter
                    break
                elif KeyLetters1.get(Letter) > 1:
                    WspolnyZnak = Letter
                    break
                elif KeyLetters1.get(Letter) > 0:
                    WspolnyZnak = Letter
                    break
                else:
                    WspolnyZnak = Letter
                    break
    for Sentence in PotSen:
        for Word in Sentence:
            if WspolnyZnak in Word:
                Key2 = Word
                break
    print(f'Najczęstszy znak {MostCommon} występujący {MaxValue} razy to prawdopodobna spacja')
    print(f'Zatem prawdopodobne zdanie ma następujące słowa: {Moment}')
    print(f'"{Key1}" oraz "{Key2}" to potencjalne słowa najbardziej nadające się do rozpoczęcia łamania kodu')
    for letter in Key1:
        for a in alfabet:
            for let in a:
                Key1B = (Key1[0].replace(Key1[0], let))
                if len(Key1) >= 2:
                    for let in a:
                        Key1C = Key1B + (Key1[1].replace(Key1[1], let))
                        if len(Key1) >= 3:
                            for let in a:
                                Key1D = Key1C + (Key1[2].replace(Key1[2], let))
                                if len(Key1) >= 4:
                                    for let in a:
                                        Key1E = Key1D + (Key1[3].replace(Key1[3], let))
                                        if len(Key1) >= 5:
                                            for let in a:
                                                Key1F = Key1E + (Key1[4].replace(Key1[4], let))
                                                
print(breaker("punpd(n=y$n/dcnu)n1y$=s"))



    

