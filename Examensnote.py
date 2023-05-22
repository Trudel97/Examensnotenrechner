# Examensnotenrechner

def notenskala(errechneteNote): #nach § 2 urPrNotSkV

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

def gesamtnote(SP_note, EJP_note):
    errechneteNote=(SP_note*0.3)+(EJP_note*0.7)
    return errechneteNote

SP_note = float(input('Gib SP '))
EJP_note = float(input ('gib EJP '))
errechneteNote = gesamtnote

print(gesamtnote)