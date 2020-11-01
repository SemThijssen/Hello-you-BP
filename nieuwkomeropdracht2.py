print ("Welkom bij mijn nieuwkomersgame genaamd The Survivor")
naam = input ("typ hier je naam in: ")
print("\nHallo",naam,"Ik hoop dat je de goede keuzes maakt;)\n")
print("Dit is wat je moet doen:\nOm te beginnen moet je 'start'intypen\nals dat is gelukt krijg je altijd meerkeuze vragen die moet je dan met A of B beantwoorden.\nAls je geen zin meer hebt om te spelen of als je het hebt afgespeeld moet je op 'opties' klikken\ndaar krijg je dan een meerkeuzevraag of je door wilt gaan of wilt stoppen.\nEn het allerbelangrijkste heb veel plezier!;)")


def opties():
    print("Je bent in de opties wat wil je gaan doen opnieuw beginnen of stoppen?")
    print("A. ik wil opnieuw")
    print("B. ik wil stoppen.\n")
    antwoord= input("Maak een keuze, A of B? ")
    if antwoord=="A" or antwoord=="a":
        start()
    elif antwoord=="B" or antwoord=="b":
        exit()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        doorgaan()    
  
    

def start():
    print("Je wilt weg van je land want er is geen werk, je wilt veel verdienen een ferrari\nkopen, een gezin hebben met minimaal 3 kinderen\nmaar dat kan niet in je land want je kan geen werk vinden.\nJe wilt naar Nederland je reist…\n")
    print("A.’s nachts")
    print("B.Overdag\n")
    antwoord= input("Maak een keuze, A of B? ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje2()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje3()
    else:
        print("Je kunt alleen antwoorden met A of B.")


def verhaalstukje2():
    print("\n\nonderweg heb je je zaklamp aan maar naarmate je doorgaat gaat je zaklamp steeds leger je gaat\n")
    print("A.Door met lopen")
    print("B.Terug en wachten tot het lichter wordt\n")
    antwoord= input("Maak een keuze, A of B? ")
    if antwoord=="A" or antwoord=="a":
        print("\n\nje gaat door ook al zie je geen ene …  je loopt verder maar je voelt niks onder je voeten opeens bedenk bij jezelf er is geen grond hier\nhmm je kijkt naar beneden en je ziet inderdaad dat je naar beneden valt\nen doodgaat.")
        from PIL import Image, ImageDraw, ImageFilter
        im1 = Image.open('dood.jpg')
        im1.show()
        opties()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje3()
    else:
        print("Je kunt alleen antwoorden met A of B ")
    
    
def verhaalstukje3():
    print("\n\nHet is weer licht buiten je gaat naar buiten en begint je reis  je ziet verderop\neen bootje en een vliegtuig naast elkaar wat vreemd denk je bij jezelf\nmaar ja welk voertuig kies je?\n")
    print("A.Het bootje")
    print("B.Het vliegtuig\n")
    antwoord= input("Maak een keuze, A of B? ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje4()
    elif antwoord=="B" or antwoord=="b":
        print("\n\nOpeens tijdens de reis bedenk je bij jezelf dat je geen rijbewijs\nvoor het vliegen hebt.\nJe stort neer en je  gaat dood.\n")
        from PIL import Image, ImageDraw, ImageFilter
        im2 = Image.open('vliegtuig.jpg')
        im2.show()
        opties()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        
        

def verhaalstukje4():
    print("\n\nje hebt het bootje gekozen tijdens je reis voel je dat je kont nat is\nen ziet dat het bootje lekt wat doe je?\n")
    print("A.Zwemmen ")
    print("B.Repareren\n ")
    antwoord= input("Maak een keuze A of B? ")
    if antwoord=="A" or antwoord=="a":
        print("je gaat zwemmen je ziet verderop een vin en het is een haaievin.\nJe probeert weg te zwemmnen maar hij haalt je in.\nHij pakt je met zijn tanden en eet je in kleine stukken op\n")
        from PIL import Image, ImageDraw, ImageFilter
        im3 = Image.open('haai.jpg')
        im3.show()
        opties()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje5()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        

def verhaalstukje5():
    print("Je repareert je boot met plakband en je hebt nog heel veel uren te gaan totdat je in Nederland komt. Je bent aangekomen op land je vraagt aan iemand waar je bent en ze zeggen in Nederland wil je een lekkere stukje hollandse kaas? Je weet het nu zeker je bent in Nederland.je moet uiteindelijk wel assiel gaan aanvragen wat doe je?\n")
    print("A.Werken")
    print("B.Assiel aanvragen\n")
    antwoord= input("Maak een keuze A of B? ")
    if antwoord=="A" or antwoord=="a":
        print("Je denkt ik ben eindelijk in Nederland ik kan niet langer wachten ik ga gelijk werken je werkt al een maand in Nederland maar je wordt opgepakt je hebt geen assiel aangevraagd en je wordt uit het land uitgezet.\n")
        from PIL import Image, ImageDraw, ImageFilter
        im4 = Image.open('uitzetting.jpg')
        im4.show()
        opties()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje6()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        

def verhaalstukje6():
    print("Je gaat naar de IND om te vertellen waarom je hier in Nederland bent wat doe je ?\n")
    print("A.Liegen")
    print("B.Waarheid\n")
    antwoord= input("Maak een keuze A of B? ")
    if antwoord=="A" or antwoord=="a":
        print("De mensen bij de IND checken of je de waarheid hebt gesproken ze komen erachter dat je niet de waarheid spreekt je wordt alsnog het land uitgezet.\n")
        from PIL import Image, ImageDraw, ImageFilter
        im5 = Image.open('uitzetting.jpg')
        im5.show()
        opties()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje7()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        
        
def verhaalstukje7():
    print("De mensen bij de IND checken of je de waardheid hebt gesproken en ze zeggen dat je de waarheid spreekt en voldoende redenen hebt om naar Nederland te komen en geven je een assiel. Je bent natuurlijk superblij en hebt je vrouw verteld dat je assiel hebt gekregen wat ga je doen om het te vieren?")
    print("A.vrienden feest vieren")
    print("B.thuis met vrouw vieren\n")
    antwoord= input("Maak een keuze A of B? ")
    if antwoord=="A" or antwoord=="a":
        print("Je houdt een house party je gebruikt een pilletje je stikt en valt dood neer")
        from PIL import Image, ImageDraw, ImageFilter
        im6 = Image.open('drugs.jpg')
        im6.show()
        opties()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje8()
    else:
        print("Je kunt alleen antwoorden met A of B ")
    
def verhaalstukje8():
    print("Je hebt een fijne dag met je vrouw achter de rug je wilt nu werk gaan zoeken maar je hebt nog geen opleiding,  ga je een opleiding doen Ja of nee?")
    print("A.ja")
    print("B.nee\n")
    antwoord= input("Maak een keuze A of B? ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje9()
    elif antwoord=="B" or antwoord=="b":
        print("Je hebt geen opleiding dus vind je geen baan.Je krijgt een uitkering")
        from PIL import Image, ImageDraw, ImageFilter
        im7 = Image.open('geld.jpg')
        im7.show()
        opties()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        
        
def verhaalstukje9():
    print("Omdat je een opleiding wilt gaan doen kan je meer werk krijgen wat kies je?")
    print("A.leger")
    print("B.programmeur\n")
    antwoord= input("Maak een keuze A of B? ")
    if antwoord=="A" or antwoord=="a":
        print("Bij je eerste training laat je per ongeluk een granaat vallen hij ontploft en je bent dood.")
        from PIL import Image, ImageDraw, ImageFilter
        im8 = Image.open('ontploffing.jpg')
        im8.show()
        opties()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje10()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        

def verhaalstukje10():
    print("je gaat een programmeer opleiding doen maar je hebt nog geen school gekozen waar ga je naartoe?")
    print("A.slechte school")
    print("B.Mediacollege\n")
    antwoord= input("Maak een keuze A of B? ")
    if antwoord=="A" or antwoord=="a":
        print("je bent beland in een van de slechtste scholen van Nederland voor de opleiding ICT je krijgt geen baan en je krijgt een uitkering.")
        from PIL import Image, ImageDraw, ImageFilter
        im9 = Image.open('geld.jpg')
        im9.show()
        opties()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje11()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        
        
def verhaalstukje11():
    print("Je bent aangekomen op de mediacollege je bent na 4 jaar aan je opleiding aan het werken, afgestudeerd en krijgt je diploma.Je moet nu een baan gaan zoeken en op stage gaan waar ga je stage lopen?")
    print("A.groot bedrijf")
    print("B.klein bedrijf\n")
    antwoord= input("Maak een keuze A of B? ")
    if antwoord=="A" or antwoord=="a":
        print("Je hebt nog geen ervaring met werk en je hebt heel veel concurrentie in je grote bedrijf je woord na 1 maand werk ontslagen. Je krijgt een uitkering.")
        from PIL import Image, ImageDraw, ImageFilter
        im10 = Image.open('geld.jpg')
        im10.show()
        opties()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje12()
    else:
        print("Je kunt alleen antwoorden met A of B")

def verhaalstukje12():
    print("Je bent heel blij bij je nieuwe bedrijf het is klein maar, je hebt geen concurrentie niet teveel werk en je hebt nog een goede salaris ook. Er wacht een heel goede toekomst voor je welke keuzes ga je allemaal daarvoor maken?")
    opties()
        

        

