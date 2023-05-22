# Examensnotenrechner

def bestimmung_der_notenskala(errechneteNote): #nach § 2 urPrNotSkV # Table mit übersicht der Noten

    if 0 <= errechneteNote <= 1.49:
        noteinwort = "ungenügend"
    elif 1.50 <= errechneteNote <= 3.99:
        noteinwort = "mangelhaft"
    elif 4.00 <= errechneteNote <= 6.49:  
        noteinwort = "ausreichend"
    elif 6.50 <= errechneteNote <= 8.99:
        noteinwort = "befriedigend"
    elif 9.00 <= errechneteNote <= 11.49:
        noteinwort = "vollbefriedigend"
    elif 11.50 <= errechneteNote <= 13.99:
        noteinwort = "gut"
    elif 14 <= errechneteNote <= 18.00:
        noteinwort = "sehr gut"
    return noteinwort

def berechnung_gesamtnote(SP_note, EJP_note): #(SP*0,3)+(EJP*0,7)
    errechneteNote=(SP_note*0.3)+(EJP_note*0.7)
    return errechneteNote

def berechnung_der_EJP_Note(Ergebniss_schriftliche, Ergebniss_mündliche):#Schriftliche 70% + mündliche 30%
    EJP_note = (Ergebniss_schriftliche*0.7)+(Ergebniss_mündliche*0.3)
    return EJP_note

def berechnung_Ergebniss_schriftliche(Zivil_1, Zivil_2, Zivil_3, StR, ÖffR_1, ÖffR_2): #Durchschnitt aus den Klausuren 
    Ergebniss_schriftliche = (Zivil_1 + Zivil_2 + Zivil_3 + StR + ÖffR_1 + ÖffR_2)/6
    return Ergebniss_schriftliche

Zivil_1 = float(input('Bitte geben Sie das Ergebniss der ersten Aufgabe ein'))
Zivil_2 = float(input('Bitte geben Sie das Ergebniss der zweiten Aufgabe ein'))
Zivil_3 = float(input('Bitte geben Sie das Ergebniss der dritten Aufgabe ein'))
StR = float(input('Bitte geben Sie das Ergebniss der vierten Aufgabe ein'))
ÖffR_1 = float(input('Bitte geben Sie das Ergebniss der fuenften Aufgabe ein'))
ÖffR_2 = float(input('Bitte geben Sie das Ergebniss der sechsten Aufgabe ein'))




SP_note = float(input('Gib SP '))
#EJP_note = float(input ('gib EJP '))


Ergebniss_schriftliche = berechnung_Ergebniss_schriftliche(Zivil_1, Zivil_2, Zivil_3, StR, ÖffR_1, ÖffR_2)
Ergebniss_mündliche = float(input('Bitte geben Sie Ihre Note aus der mündlichen Prüfung an'))
EJP_note = berechnung_der_EJP_Note(Ergebniss_schriftliche, Ergebniss_mündliche)
errechneteNote = berechnung_gesamtnote(SP_note, EJP_note)
noteinwort = bestimmung_der_notenskala(errechneteNote)

print(f"Sie haben Gesammtnote von{errechneteNote: .2f} Punkte erreicht." )
print(noteinwort)
print(f'Diese Note setzt sich aus {SP_note: .2f} und aus {EJP_note: .2f}')