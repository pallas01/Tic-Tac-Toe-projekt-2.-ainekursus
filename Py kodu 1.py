print ("Hello world!")

name = "Georg" # string andmetüüp Tekst // numnrid SAAB teha tekstiks, aga mitte vastupidi
age = 20 # integer andmetüüp // arv ilma komakohata
weight = 78.7 # float andmetüüp //komakohaga kommentaar (invisible)
student = True # boolean andmetüüp // true or false ls?

#vasakul pool üleval siis MUUTUJAD, ja vasakul VÄÄRTUSED

#hashtagiga on kommentaarid

#1 viis väljastada terminalile teksti, ehk nö printimine

print(name + " on " + str(age) + "-aastane")

#2 viis teksti väljstamiseks:

print(name, "on", age,"-aastane" ) # siin iga elemendi vahel spaced tho

#                                                                   print("2" + "2") # math pole absull enabled
print(2 + 2) # Mata töötab

#ting laused ehk IF

username_database = "ananass123"
password_database = "pesulaud"

input_password = input( "Sisesta parool: ") # tunnis otse parooli juurde, ise lisan vahele usernamei
# input laseb käsitsi terminalis infot sisestada
if password_database == input_password:
 # programm saab aru kui If true:
 # kui salvestatud parool on sama, mis sisestatud
 print("oled sisse logitud, ananass123!")
elif input_password == "pesulaud123!":
 print("ise oled")
 #ehk kui elif on vale siis else järgenbki vastus, et ei tööta
else: 
 print ("vale parool")

# PYTHONI ERIPara ongi ELIF ehk else ja if koos.
# töötab = true

töötab = True
if töötab:
 print("oled ilus")

pangakonto = 900
if pangakonto == 1000:
 print("sul on tonn")
if pangakonto >= 10:
 print("enam ei ole piinlik") 

 pangakonto = 900
if pangakonto == 1000:
 print("sul on tonn")
if pangakonto >= 10:
 print("enam ei ole piinlik") 

 #ta näitas mingit teemat kuidas copytud konto summad on sama ifi taga mis originaali if on vms. kinda got complicated


 XP = input("su xp:")
 lvl = float(XP) / 100
 print("su tase:", lvl ) 

 # sisult saab selle xp juures defineerida nii 62 kui ka 63 real saab defineerida xp numbriks

 #astendamine kaks tärni, jagamine kaldkriips, korrutamine üks tärn