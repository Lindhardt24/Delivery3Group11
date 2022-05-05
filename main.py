# *************************************** MAIN.PY******************************************************
# Dette script er lavet for at vise hvordan en rapport kan genereres i en PDF fil.
# Der bruges en random tal generator som stressskalaen og genereringen tager udgangspunkt i denne.
# De random tal står i stedet for egentlig data som ville komme gennem en måling med headbandet.
# ******************************** Install før script køres********************************************

# Encodings importeres for at bruge utf_8 til at få flest mulige tegn/bogstaver med i rapporten herunder æ, ø og å.
# Random importeres for at kunne generere random tal til stresskalaen.
from encodings import utf_8
from fpdf import FPDF
import random

# Variablen n initieres ved at den assignes et random tal mellem 1-10 hver gang scriptet køres.
n = random. randint(1,10) 

# Her indtastes det brugernavn der bruges i Appen. 
user = input("Skriv dit brugernavn her: ")

# Gemmer pdf klassen som en variabel
pdf = FPDF()

# Adder en side til PDF
pdf.add_page()

# Font der skal bruges i PDF´en
pdf.set_font("Arial", size = 12, )

# Her åbnes txt filerne og læses ind. 
f = open("stress1.txt", "r", encoding="utf-8")
f = open("stress2.txt", "r", encoding="utf-8")
f = open("stress3.txt", "r", encoding="utf-8")
f = open("stress4.txt", "r", encoding="utf-8")

# IF statement til at finde den "rigtige" text fil med det rigtige indhold ved at kigge efter n variablen.
def openfile ():
    if n <= 3:
        f = open("stress1.txt", "r"),
    elif n <= 6:
        f = open("stress2.txt", "r"),
    elif n <= 8:
        f = open("stress3.txt", "r"),
    else:   
        f = open("stress4.txt", "r")

# Dette forloop indsætter teksten og sætter reglerne ift formatteringen af teksten
# Ydermere addes rapportens billede, der indsættes oppe i højre hjørne.
for x in f:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'Left', border=0)
    pdf.image('logo1.png',205,35,-30);

# Dette genererer PDFen. User tager brugernavnet og lægger det til rapportens navn. 
pdf.output(user + "srapport.pdf")

# Underliggende print statement fortæller brugeren at der nu vil blive genereret en rapport i en PDF fil.
print("Hej " + user + ". Du scorer " + str(n) + " på stress skalaen. " + 
"Du får nu printet din rapport som en PDF fil")




