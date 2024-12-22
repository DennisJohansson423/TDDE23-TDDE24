def viktsiffror(pnr_lista):
    vikt_lista = []
    vikt = 2
    for siffra in pnr_lista[:-1]:
        vikt_lista.append(siffra * vikt)
        if vikt == 2:
            vikt = 1
        else:
            vikt = 2
    return vikt_lista

def siffersummaFunk(vikt_lista):
    siffersumma = 0
    for siffra in vikt_lista:
        if siffra >= 10:
            ental = siffra - 10
            siffersumma += ental + 1
        else:
            siffersumma += siffra
    return siffersumma

def närmaste_tiotalFunk(siffersumma):
    if siffersumma >= 100:
        tiotal = int(str(siffersumma)[1])
    else:
        tiotal = int(str(siffersumma)[0])
    return (tiotal + 1) * 10

def kontroll(tiotal,siffersumma,kontroll_siffra):
    if kontroll_siffra == 0:
        differens = tiotal - siffersumma -10
    else:
        differens = tiotal - siffersumma
    return differens == kontroll_siffra

def check_pnr(pnr_list):
    vikt_lista = viktsiffror(pnr_list)
    print(vikt_lista)
    kontrollsiffra = pnr_list[-1]
    siffersumma = siffersummaFunk(vikt_lista)
    närmaste_tiotal = närmaste_tiotalFunk(siffersumma)
    return kontroll(närmaste_tiotal,siffersumma,kontrollsiffra)

#check_pnr([0, 2, 0, 2, 0, 5, 9, 5, 7, 2])