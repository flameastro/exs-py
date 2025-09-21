# ex243: Formatar Telefone: Peça um número de telefone (apenas números) e formate-o como (XX) XXXXX-XXXX.
def formata_telefone(telefone) -> str:
    return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}" if len(telefone) == 11 else ""


if __name__ == "__main__":
    print(formata_telefone("51937665634"))  # (51) 93766-5634
    print(formata_telefone("67945342231"))  # (67) 94534-2231
    print(formata_telefone("76987665343"))  # (76) 98766-5343
