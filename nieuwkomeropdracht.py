print ("Welkom bij mijn nieuwkomersgame genaamd The Survivor")
naam = input ("typ hier je naam in: ")
print("\nHallo",naam," Ik hoop dat je de goede keuzes maakt;)\n")
print("Dit is wat je moet doen:\n  om te beginnen moet je 'startspel()' intypen als dat is gelukt krijg je altijd meerkeuze vragen die moet je dan met A of B beantwoorden en geen kleine letters a of b maar grote letters\n Als je geen zin meer hebt om te spelen of als je het hebt afgespeeld moet je op opties klikken en daar krijg je dan een meerkeuzevraag of het door wilt gaan of wilt stoppen en het allerbelangrijkste heb veel plezier!;)")
    
  
    

def startspel():
    print("Je wilt weg van je land want er is geen werk, je wilt veel verdienen een ferrari kopen een gezin hebben met minimaal 3 kinderen maar dat kan niet in je land want je kan geen werk vinden. Je wilt naar Nederland je reist…\n")
    print("A.’s nachts")
    print("B.Overdag\n")
    antwoord= input("Maak een keuze, A of B? ")
    if antwoord=="A":
        verhaalstukje2()
    elif antwoord=="B":
        verhaalstukje3()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje1()

def verhaalstukje2():
    print("\n\nonderweg heb je je zaklamp aan maar naarmate je doorgaat gaat je zaklamp steeds leger je gaat\n")
    print("A.Door met lopen")
    print("B.Terug en wachten tot het lichter wordt\n")
    antwoord= input("Maak een keuze, A of B?")
    if antwoord=="A":
        print("je gaat door ook al zie je geen ene …  je loopt verder maar je voelt niks onder je voeten opeens bedenk bij jezelf er is geen grond hier hmm je kijkt naar beneden en je ziet inderdaad dat je naar beneden valt en doodgaat.")
        opties()
    elif antwoord=="B":
        verhaalstukje3()
    else:
        print("Je kunt alleen antwoorden met A of B ")
    verhaalstukje2()
    
def verhaalstukje3():
    print("Het is weer licht buiten je gaat naar buiten en begint je reis  je ziet verderop een bootje en een vliegtuig naast elkaar wat vreemd denk je bij jezelf maar ja welk voertuig kies je? ")
    print("A.Het bootje")
    print("B.Het vliegtuig")
    antwoord= input("Maak een keuze, A of B? ")
    if antwoord=="A":
        verhaalstukje4()
    elif antwoord=="B":
        print("Opeens tijdens de reis bedenk je ik kan helemaal niet vliegen ik heb geen vliegbewijs je stort neer en je  gaat dood.")
        opties()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        verhaalstukje2()
        

def verhaalstukje4():
    print("je hebt het bootje gekozen tijdens je reis voel je dat je kont nat is en ziet dat het bootje lekt wat doe je?")
    print("A.Zwemmen ")
    print("B.Repareren ")
    antwoord= input("Maak een keuze A of B? ")
    if antwoord=="A":
        print("je gaat zwemmen maar voor dat je je boot verlaat kreeg je een snee en je valt in het water je ziet dat je bloed je denkt dat is niks gewoon een wondje ik ga verder\nJe zwemt opeens zie in de verte een haaievin want haaien ruiken bloed en gaan daarnaartoe je probeert weg te zwemmen van de haai. De haai haalt je in en eet eerst je voeten op lekker denkt de haai ik neem nog een hap hij pakt je met zijn tanden en eet je in kleine stukken op")
        from PIL import Image, ImageDraw, ImageFilter
        im1 = Image.open('haai.jpg')
        im1.show()
        opties()
    elif antwoord=="B":
        verhaalstukje5()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        verhaalstukje3()

def verhaalstukje5():
    print("Je repareert je boot met plakband en je hebt nog heel veel uren te gaan totdat je in Nederland komt. Je bent aangekomen op land je vraagt aan iemand waar je bent en ze zeggen in Nederland wil je een lekkere stukje hollandse kaas? Je weet het nu zeker je bent in Nederland.je moet uiteindelijk wel assiel gaan aanvragen wat doe je?")
    print("A.Werken")
    print("B.Assiel aanvragen")
    antwoord= input("Maak een keuze A of B? ")
    if antwoord=="A":
        print("Je denkt ik ben eindelijk in Nederland ik kan niet langer wachten ik ga gelijk werken je werkt al een maand in Nederland maar je wordt opgepakt je hebt geen assiel aangevraagd en je wordt uit het land uitgezet.")
        opties()
    elif antwoord=="B":
        verhaalstukje6()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        verhaalstukje4()

def verhaalstukje6():
    print("Je gaat naar de IND om te vertellen waarom je hier in Nederland bent wat doe je ?")
    print("A.Liegen")
    print("B.Waarheid")
    antwoord= input("Maak een keuze A of B? ")
    if antwoord=="A":
        print("De mensen bij de IND checken of je de waarheid hebt gesproken ze komen erachter dat je niet de waarheid spreekt je wordt alsnog het land uitgezet.")
        opties()
    elif antwoord=="B":
        verhaalstukje7()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        verhaalstukje5()
        
def verhaalstukje7():
    print("De mensen bij de IND checken of je de waardheid hebt gesproken en ze zeggen dat je de waarheid spreekt en voldoende redenen hebt om naar Nederland te komen en geven je een assiel. Je bent natuurlijk superblij en hebt je vrouw verteld dat je assiel hebt gekregen wat ga je doen om het te vieren?")
    print("A.vrienden feest vieren")
    print("B.thuis met vrouw vieren")
    antwoord= input("Maak een keuze A of B? ")
    if antwoord=="A":
        print("Je houdt een house party je gebruikt een pilletje je stikt en valt dood neer")
        opties()
    elif antwoord=="B":
        verhaalstukje8()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        verhaalstukje6()
def verhaalstukje8():
    print("Je hebt een fijne dag met je vrouw achter de rug je wilt nu werk gaan zoeken maar je hebt nog geen opleiding,  ga je een opleiding doen Ja of nee?")
    print("A.ja")
    print("B.nee")
    antwoord= input("Maak een keuze A of B? ")
    if antwoord=="A":
        verhaalstukje9()
    elif antwoord=="B":
        print("Je hebt geen opleiding dus vind je geen baan.Je krijgt een uitkering")
        opties()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        verhaalstukje7()
        
def verhaalstukje9():
    print("Omdat je een opleiding wilt gaan doen kan je meer werk krijgen wat kies je?")
    print("A.leger")
    print("B.programmeur")
    antwoord= input("Maak een keuze A of B? ")
    if antwoord=="A":
        print("Bij je eerste training laat je per ongeluk een granaat vallen hij ontploft en je bent dood.")
        opties()
    elif antwoord=="B":
        verhaalstukje10()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        verhaalstukje8()

def verhaalstukje10():
    print("je gaat een programmeer opleiding doen maar je hebt nog geen school gekozen waar ga je naartoe?")
    print("A.slechte school")
    print("B.Mediacollege")
    antwoord= input("Maak een keuze A of B? ")
    if antwoord=="A":
        print("je bent beland in een van de slechtste scholen van Nederland voor de opleiding ICT je krijgt geen baan en je krijgt een uitkering.")
        opties()
    elif antwoord=="B":
        verhaalstukje11()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        verhaalstukje9()
        
def verhaalstukje11():
    print("Je bent aangekomen op de mediacollege je bent na 4 jaar aan je opleiding aan het werken, afgestudeerd en krijgt je diploma.Je moet nu een baan gaan zoeken en op stage gaan waar ga je stage lopen?")
    print("A.groot bedrijf")
    print("B.klein bedrijf")
    antwoord= input("Maak een keuze A of B? ")
    if antwoord=="A":
        print("Je hebt nog geen ervaring met werk en je hebt heel veel concurrentie in je grote bedrijf je woord na 1 maand werk ontslagen. Je krijgt een uitkering.")
        opties()
    elif antwoord=="B":
        verhaalstukje12()
    else:
        print("Je kunt alleen antwoorden met A of B")
        verhaalstukje10()
        
def opties():
    print("A. ik wil doorgaan.")
    print("B. ik wil stoppen.\n")
    antwoord=input("Maak een keuze, A of B? ")
    if antwoord=="A":
        verhaalstukje1()
    elif antwoord=="B":
        exit()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        doorgaan()
    

