palestra1 = {
    "Marley Beltran",
    "Allen Black",
    "Flynn Adams",
    "Ajay Copeland",
    "Keziah Shaw",
    "Junaid Hogan",
    "Leanne Fields",
}

palestra2 = {
    "Tara Blackwell",
    "Jared Salas",
    "Samira Sykes",
    "Junaid Hogan",
    "Leanne Fields",
}

palestra3 = {
    "Flynn Adams",
    "Ajay Copeland",
    "Keziah Shaw",
    "Leanne Fields",
    "Junaid Hogan",
}

participantesAssiduos = palestra1.intersection(palestra2).intersection(palestra3)
participacaoGeral = palestra1.union(palestra2).union(palestra3)

lstPA = list(participantesAssiduos)
lstPG = list(participacaoGeral)
lstPA.sort()
lstPG.sort()

print("Pessoas que participaram de todas as palestras:")
for p in lstPA:
    print(p)

print("Presenca geral:")
for pg in lstPG:
    print(pg)