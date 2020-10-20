
print ("Welkom bij mijn nieuwkomersgame genaamd The Survivor")
naam = input ("typ hier je naam in: ")
print("\nHallo",naam," Ik hoop dat je de goede keuzes maakt;)\n")

#Vraag1
antwoord = input("Je wilt weg van je land want er is geen werk, je wilt veel verdienen een ferrari kopen een gezin hebben met minimaal 3 kinderen maar dat kan niet in je land want je kan geen werk vinden. Je wilt naar Nederland je reist…\nA. 's nachts \nB. overdag \n")
print(" ")
if antwoord == 'A':
    antwoord1 = input("onderweg heb je je zaklamp aan maar naarmate je doorgaat gaat je zaklamp steeds leger je gaat…\nA Door met lopen \nB Terug en wachten tot het weer licht wordt. \n")
elif antwoord == 'B':
    antwoord1 = input("Het is weer licht buiten je gaat naar buiten en begint je reis  je ziet verderop een bootje en een vliegtuig naast elkaar wat vreemd denk je bij jezelf maar ja welk voertuig kies je?\nA.Het bootje \nB Het vliegtuig \n")
    
else:
    print("kies A of B")

#Vraag2
if antwoord1 == 'A':
    print ("je gaat door ook al zie je geen ene …  je loopt verder maar je voelt niks onder je voeten opeens bedenk bij jezelf er is geen grond hier hmm je kijkt naar beneden en je ziet inderdaad dat je naar beneden valt en doodgaat.")
elif antwoord1 == 'B':
    antwoord2 = input("Het is weer licht buiten je gaat naar buiten en begint je reis  je ziet verderop een bootje en een vliegtuig naast elkaar wat vreemd denk je bij jezelf maar ja welk voertuig kies je?\nA.Het bootje \nB Het vliegtuig \n")
else:
    print("Kies A of B")

#Vraag3
if antwoord2 == 'A':
    antwoord3 = input("je hebt het bootje gekozen tijdens je reis voel je dat je kont nat is en ziet dat het bootje lekt wat doe je?\nA Zwemmen \nB repareren \n")
elif antwoord2 == 'B':
    print("Opeens tijdens de reis bedenk je ik kan helemaal niet vliegen ik heb geen vliegbewijs je stort neer en je  gaat dood.")
else:
    print("kies A of B")

#Vraag4
if antwoord3 == 'A':
    print("Je gaat zwemmen.Na een paar minuten zie je een haaievin je draait je om en begint weg te zwemmen maar de haai haalt je in en eet je op.")
elif antwoord3 == 'B':
    antwoord4 = input("Je repareert je boot met plakband en je hebt nog heel veel uren te gaan totdat je in Nederland komt. Je bent aangekomen op land je vraagt aan iemand waar je bent en ze zeggen in Nederland wil je een lekkere stukje hollandse kaas? Je weet het nu zeker je bent in Nederland.je moet uiteindelijk wel assiel gaan aanvragen wat doe je?\nA Werken \nB Assiel aanvragen")
else:
    print("kies A of B")
    
#Vraag5
if antwoord4 == 'A':
    print("Je denkt ik ben eindelijk in Nederland ik kan niet langer wachten ik ga gelijk werken je werkt al een maand in Nederland maar je wordt opgepakt je hebt geen assiel aangevraagd en je wordt uit het land uitgezet.")
elif antwoord4 == 'B':
    antwoord5 = input("Je gaat naar de IND om te vertellen waarom je hier in Nederland bent wat doe je ?\nA Liegen \nB waarheid")
else:
    print("kies A of B")

#Vraag6
if antwoord5 == 'A':
    print("De mensen bij de IND checken of je de waarheid hebt gesproken ze komen erachter dat je niet de waarheid spreekt je wordt alsnog het land uitgezet.")
elif antwoord5 == 'B':
    antwoord6 = input("De mensen bij de IND checken of je de waardheid hebt gesproken en ze zeggen dat je de waarheid spreekt en voldoende redenen hebt om naar Nederland te komen en geven je een assiel. Je bent natuurlijk superblij en hebt je vrouw verteld dat je assiel hebt gekregen wat ga je doen om het te vieren?\nA Met vrienden feest vieren \nB Thuis met vrouw vieren")
else:
    print("kies A of B")
    
#vraag7
if antwoord6 == 'A':
    print("Je gaat met je vrienden een house party doen je krijgt een pilletje aangeboden je neemt pilletje in en je stikt. je valt dood neer.")
elif antwoord6 == 'B':
    antwoord7 = input("Je hebt een fijne dag met je vrouw achter de rug je wilt nu werk gaan zoeken maar je hebt nog geen opleiding,  ga je een opleiding doen Ja of nee?\nA Ja \nB Nee")
else:
    print("kies A of B")

#Vraag8
if antwoord7 == 'A':
    antwoord8 = input("Omdat je een opleiding wilt gaan doen kan je meer werk krijgen wat kies je?\nA leger \nB programmeur")
elif  antwoord7 == 'B':
    print("Je hebt geen opleiding dus vind je geen baan.Je krijgt een uitkering.")

else:
    print("kies A of B")

#Vraag9
if antwoord8 == 'A':
    print("Je zit in het leger en je hebt je laatste training, iemand laat perongeluk een granaat vallen en jij krijgt een ongeluk en gaat dood.")
elif antwoord8 == 'B':
    antwoord9 = input("je gaat een programmeer opleiding doen maar je hebt nog geen school gekozen waar ga je naartoe?\nA Slechte school \nB Mediacollege")
else:
    print("kies A of B")

#Vraag10
if antwoord9 == 'A':
    print("je bent beland in een van de slechtste scholen van Nederland voor de opleiding ICT je krijgt geen baan en je krijgt een uitkering.")
elif antwoord9 == 'B':
    antwoord10 = input("Je bent aangekomen op de mediacollege je bent na 4 jaar aan je opleiding aan het werken, afgestudeerd en krijgt je diploma.Je moet nu een baan gaan zoeken en op stage gaan waar ga je stage lopen?\nA Groot bedrijf \nB klein bedrijf")
else:
    print("kies A of B")

#Vraag11
if antwoord10 == 'A':
    print("Je hebt nog geen ervaring met werk en je hebt heel veel concurrentie in je grote bedrijf je woord na 1 maand werk ontslagen. Je krijgt een uitkering.")
elif antwoord10 == 'B':
    print("Je bent heel blij bij je nieuwe bedrijf het is klein maar, je hebt geen concurrentie niet teveel werk en je hebt nog een goede salaris ook. Er wacht een heel goede toekomst voor je welke keuzes ga je allemaal daarvoor maken?")
else:
    print("Kies A of B")
    
