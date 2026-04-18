# ex335: Um caramujo está na parede de um poço a cinco metros de sua borda. Tentando sair do poço, ele sobe três metros durante o dia, porém desce escorregando dois metros durante a noite. Quantos dias levará para o caramujo conseguir sair do poço?
dias = 0
metros = 0

while True:
    dias += 1
    metros += 3

    if metros == 5:
        break

    metros -= 2


print(f"Levariam {dias} dias para o caramujo conseguir sair do poço")
# Levariam 3 dias para o caramujo sair do poço, agora vamos ver o porque (e nesse algoritmo, a ordem faz total diferença)
# No primeiro dia: o caramujo alcança seu limite de 3 metros, e na noite, desce 2 metros, resultando em 1 metro. No segundo dia, sobe + 3 metros, resultando em 4 metros, mas cai 2 metros para baixo na noite. E no terceiro dia, o caramujo sobe + 3 metros, resultando em 5 metros, e agora o caramujo não pode mais descer porque já ultrapassou a borda do poço, então depois da noite, não tem como ele cair 2 metros
