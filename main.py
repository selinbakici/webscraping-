import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook
def n11():
    linkliste = []
    marka = []
    model = []
    islemci = []
    islemci_model = []
    isletim_sistemi = []
    disk_turu = []
    ram = []
    ekran_karti = []
    ekran_boyutu = []
    disk_kapasite = []
    fiyat = []
    fiyatliste = []
    for n in range(1, 21):
        dizi = []
        titles = []
        titles_ = []
        props = []
        props_ = []

        plain_text = "https://www.n11.com/arama?q=laptop&jpg="
        plain_text += str(n)
        url = plain_text
        dizi.append(url)

        response = requests.get(url)
        html_icerigi = response.content
        soup = BeautifulSoup(html_icerigi, "html.parser")

        data = soup.find_all("li", {"class": "column"})
        links = []
        for items in data:
            link = items.find('a')['href']
            links.append(link)
        linkliste += links

    for link in linkliste:
        response1 = requests.get(link)
        html_icerigi1 = response1.content
        soup1 = BeautifulSoup(html_icerigi1, "html.parser")
        bilgiler = soup1.find_all("ul", {"class": "unf-prop-list"})
        fiyatlar = soup1.find_all("div", {"class": "unf-p-summary-price"})
        if fiyatlar == []:
            continue
        else:
            for i in range(len(fiyatlar)):
                fiyatlar[i] = (fiyatlar[i].text).strip("\n").strip()
            fiyatliste.append(fiyatlar[i])
        for bilgi in bilgiler:
            title = bilgi.find_all("p", {"class": "unf-prop-list-title"})
            prop = bilgi.find_all("p", {"class": "unf-prop-list-prop"})
            titleloop = [titles.text for titles in title]
            proploop = [props.text for props in prop]

        for s in range(len(titleloop)):
            if (titleloop[s] == "Marka"):
                marka.append(proploop[s])
        for s in range(len(titleloop)):
            if (titleloop[s] == "Model"):
                model.append(proploop[s])
        for s in range(len(titleloop)):
            if (titleloop[s] == "İşlemci"):
                islemci.append(proploop[s])
        for s in range(len(titleloop)):
            if (titleloop[s] == "İşlemci Modeli"):
                islemci_model.append(proploop[s])
        for s in range(len(titleloop)):
            if (titleloop[s] == "İşletim Sistemi"):
                isletim_sistemi.append(proploop[s])
        for s in range(len(titleloop)):
            if (titleloop[s] == "Disk Türü"):
                disk_turu.append(proploop[s])
        for s in range(len(titleloop)):
            if (titleloop[s] == "Bellek Kapasitesi"):
                ram.append(proploop[s])
        for s in range(len(titleloop)):
            if (titleloop[s] == "Ekran Kartı Modeli"):
                ekran_karti.append(proploop[s])
        for s in range(len(titleloop)):
            if (titleloop[s] == "Ekran Boyutu"):
                ekran_boyutu.append(proploop[s])
        for s in range(len(titleloop)):
            if (titleloop[s] == "Disk Kapasitesi"):
                disk_kapasite.append(proploop[s])
    data = {
        "Disk Türü": disk_turu,
        "Ekran Kartı Modeli": ekran_karti,
        "Bellek Kapasitesi": ram,
        "İşlemci Modeli": islemci_model,
        "İşlemci": islemci,
        "Ekran Boyutu": ekran_boyutu,
        "İşletim Sistemi": isletim_sistemi,
        "Model": model,
        "Marka": marka,
        "Disk Kapasitesi": disk_kapasite,
        "Fiyat": fiyatliste
    }
    df = pd.DataFrame(data, columns=[
        "Disk Türü",
        "Ekran Kartı Modeli",
        "Bellek Kapasitesi",
        "İşlemci Modeli",
        "İşlemci",
        "İşletim Sistemi",
        "Model",
        "Disk Kapasitesi"
    ])
    df2 = pd.DataFrame(data, columns=[
        "Ekran Boyutu",
        "Marka"
    ])
    df3 = pd.DataFrame(data, columns=[
        "Fiyat"
    ])
    ekran_boyutu_ = df2['Ekran Boyutu']
    marka_ = df2['Marka']
    fiyat_ = df3['Fiyat']
    df = df.join(ekran_boyutu_)
    df = df.join(marka_)
    df = df.join(fiyat_)
    print(df.to_string())  # to_string hepsini tek tek görmemizi sağlıyor.
    #writer = pd.ExcelWriter('test.xlsx', engine='openpyxl')
    #wb = writer.book
    #df.to_excel(writer, index=False)
    #wb.save('test.xlsx')
n11()
def trendyol():
    # trendyol
    linkliste = []
    titles_ = []
    props_ = []
    fiyatliste = []
    markaliste = []

    islemci = []
    islemci_tip = []
    isletim_sistemi = []
    disk_turu = []
    ram = []
    ekran_karti = []
    ekran_boyutu = []
    disk_kapasite = []

    for n in range(2, 21):
        dizi = []
        plain_text = "https://www.trendyol.com/sr?q=laptop&qt=laptop&st=laptop&os=1&pi="
        plain_text += str(n)
        url = plain_text
        dizi.append(url)
        # print(plain_text)

        response = requests.get(url)
        html_icerigi = response.content
        soup = BeautifulSoup(html_icerigi, "html.parser")

        data = soup.find_all("div", {"class": "p-card-chldrn-cntnr card-border"})
        liste = list()
        links = []
        phn_name = []
        start_link = "https://www.trendyol.com"
        for items in data:
            rest_link = items.find('a')['href']
            name = items.find("span", attrs={"class": "prdct-desc-cntnr-ttl"})
            price = soup.find_all("div", attrs={"class": "prc-box-dscntd"})
            links.append(start_link + rest_link)
        linkliste += links
    for link in linkliste:
        response1 = requests.get(link)
        html_icerigi1 = response1.content
        soup1 = BeautifulSoup(html_icerigi1, "html.parser")

        fiyatlar = soup1.find("span", {"class": "prc-dsc"})
        if fiyatlar == []:
            continue
        else:
            fiyatliste += fiyatlar

        bilgiler = soup1.find_all("ul", {"class": "detail-attr-container"})
        for bilgi in bilgiler:
            ozellikler = bilgi.find_all("li", {"class": "detail-attr-item"})
            for ozellik in ozellikler:
                title = ozellik.find("span")
                prop = ozellik.find("b")
                titleloop = [titles.text for titles in title]
                proploop = [props.text for props in prop]
                titles_ += titleloop
                props_ += proploop
        basliklar = soup1.find("h1", {"class": "pr-new-br"}).find('a')
        markaliste.append(basliklar)

    for s in range(len(titles_)):
        if (titles_[s] == "Ram (Sistem Belleği)"):  # 2628
            ram.append(props_[s])
    for s in range(len(titles_)):
        if (titles_[s] == "Ekran Kartı"):  # 2628
            ekran_karti.append(props_[s])
    for s in range(len(titles_)):
        if (titles_[s] == "İşlemci Tipi"):  # 2628
            islemci_tip.append(props_[s])
    for s in range(len(titles_)):
        if (titles_[s] == "Ekran Boyutu"):  # 2628
            ekran_boyutu.append(props_[s])
    for s in range(len(titles_)):
        if (titles_[s] == "İşletim Sistemi"):  # 2628
            isletim_sistemi.append(props_[s])
    for s in range(len(titles_)):
        if (titles_[s] == "SSD Kapasitesi"):  # 2628
            disk_kapasite.append(props_[s])
    for s in range(len(props_)):
        disk_turu.append("SSD")

    data = {
        "Marka": markaliste,
        "Ekran Kartı Modeli": ekran_karti,
        "Bellek Kapasitesi": ram,
        "İşlemci Modeli": islemci_tip,
        "Ekran Boyutu": ekran_boyutu,
        "İşletim Sistemi": isletim_sistemi,
        "Disk Kapasitesi": disk_kapasite,
        "Fiyat": fiyatliste,
        "Disk türü": disk_turu
    }
    df = pd.DataFrame(data, columns=[
        "Marka",
        "Ekran Kartı Modeli",
        "Bellek Kapasitesi",
        "İşlemci Modeli",
        "Ekran Boyutu",
        "İşletim Sistemi",
        "Disk Kapasitesi",
        "Fiyat"
    ])
    df2 = pd.DataFrame(data, columns=[
        "Disk türü"
    ])
    disk_turu = df2['Disk türü']
    df = df.join(disk_turu)
    print(df.to_string())
trendyol()