import os
from vzor import PREVOD

# f = open(os.path.join(cesta, jmeno), mode="r")


def nacitani_txt(cesta: str) -> list[str]:
    with open(cesta, mode="r", encoding="utf-8") as f:
        return f.readlines()
    #     obsah = f.readlines()
    # return obsah


def najdi_vsechny_txt(cesta: str) -> list[str]:
    cesty = []
    for jmeno in os.listdir(cesta):
        if jmeno.endswith(".txt"):
            cesty.append(os.path.join(cesta, jmeno))
    return cesty


def ulozit_vysledek(cesta: str, obsah: list[str]):
    print(cesta)
    with open(cesta, mode="w", encoding="utf-8") as f:
        f.writelines(obsah)


def zformatuj_data(obsah: list[str]) -> list[str]:
    zformatovany_obsah = []
    for radek in obsah:
        radek_list = radek.split(",")
        # if radek_list[0] in PREVOD:
        radek_list[0] = PREVOD.get(radek_list[0], "unknown")
        zformatovany_obsah.append(",".join(radek_list))
    return zformatovany_obsah


def main():
    cesta_in = "input"
    cesta_out = "output"
    cesty = najdi_vsechny_txt(cesta_in)
    for i, cesta in enumerate(cesty):
        obsah = nacitani_txt(cesta)
        zformatovany_obsah = zformatuj_data(obsah)
        cesta_out_soubor = os.path.join(cesta_out, f"vysledek_{i+1}.txt")
        ulozit_vysledek(cesta_out_soubor, zformatovany_obsah)


main()
