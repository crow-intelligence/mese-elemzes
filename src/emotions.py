#öröm, szomorúság, harag, félelem, meglepődés, undor
orom_wds = set(line.strip() for line in (open("src/emcisztrak/emo_orom_full.txt", encoding="utf-8")))
szomorusag_wds = set(line.strip() for line in (open("src/emcisztrak/emo_banat_full.txt", encoding="utf-8")))
harag_wds = set(line.strip() for line in (open("src/emcisztrak/emo_duh_full.txt", encoding="utf-8")))
felelem_wds = set(line.strip() for line in (open("src/emcisztrak/emo_felelem_full.txt", encoding="utf-8")))
meglepodes_wds = set(line.strip() for line in (open("src/emcisztrak/emo_meglepodes_full.txt", encoding="utf-8")))
undor_wds = set(line.strip() for line in (open("src/emcisztrak/emo_undor_full.txt", encoding="utf-8")))


################################# egyedi érzelem##############################
def meglepodes_szamlalo():
    with open("/home/zoltanvarju/PycharmProjects/mese-elemzes/data/processed/lemmatized.txt", "r",
              encoding="utf-8") as infile:
            data = infile.read().strip()
    mese = data.split(" ")
    mese_meglepodesszavak = []
    for i in mese:
        if i in meglepodes_wds:
            mese_meglepodesszavak.append(i)
    return mese_meglepodesszavak


#print(meglepodes_szamlalo())


################################### általános érzelem ############################
def erzelem_szamlalo(erzelem_tipus):
    with open("/home/zoltanvarju/PycharmProjects/mese-elemzes/data/processed/lemmatized.txt", "r", encoding="utf-8") as infile:
        data = infile.read().strip() # szedjük le a felesleges whitespace-t
    mese = data.split(" ")
    mese_erzelem = []
    for i in mese:
        if erzelem_tipus == "meglepodes":
            if i in meglepodes_wds:
                mese_erzelem.append(i)
        elif erzelem_tipus == "felelem":
            if i in felelem_wds:
                mese_erzelem.append(i)
        elif erzelem_tipus == "undor":
            if i in undor_wds:
                mese_erzelem.append(i)
        elif erzelem_tipus == "harag":
            if i in harag_wds:
                mese_erzelem.append(i)
        elif erzelem_tipus == "orom":
            if i in orom_wds:
                mese_erzelem.append(i)
        elif erzelem_tipus == "szomorusag":
            if i in szomorusag_wds:
                mese_erzelem.append(i)
    mese_hossz = len(mese)
    mese_erzelem_hossz = (len(mese_erzelem))
    ratio = (mese_erzelem_hossz / mese_hossz)
    return mese_erzelem


#print(erzelem_szamlalo("szomorusag"))





############################################egyedi szavak######################################
szomorusag_lista = erzelem_szamlalo("meglepodes")
myset = set(szomorusag_lista)
print(myset)