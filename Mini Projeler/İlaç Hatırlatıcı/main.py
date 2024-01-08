import time

def ilac_kayit(saat, ilac_adi, ilac_dict):
    ilac_dict[saat] = ilac_adi
    print(f"{ilac_adi} isimli ilaç {saat} saatine kaydedildi.")

def ilac_hatirlatici(ilac_dict):
    while True:
        simdiki_saat = time.strftime("%H:%M")

        if simdiki_saat in ilac_dict:
            ilac_adi = ilac_dict[simdiki_saat]
            print(f"{ilac_adi} isimli ilacını al!")
            break

if __name__ == "__main__":
    ilac_dict= {}
    ilac = input("İlaç adını giriniz:")
    saat = input("İlaç almanız gereken saati girin:")
    ilac_kayit(saat, ilac, ilac_dict)
    ilac_hatirlatici(ilac_dict)