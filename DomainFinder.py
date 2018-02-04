from bs4 import BeautifulSoup
import urllib.request
metin = """
             Finding the sites on the IP address
                 Coded By : Murat YEŞİLTEPE
           Exit Door : Enter the IP address : exit
"""
print(metin)
while True:
    ip_adresi = input("Enter the IP address : ")
    url = "https://www.bing.com/search?q=ip%3a" + ip_adresi + "&first="
    ek = 1
    if ip_adresi == "exit":
        break
    else:
        for i in range(7):
            url_ek = url+str(ek)
            url_oku = urllib.request.urlopen(url_ek)
            soup = BeautifulSoup(url_oku,'html.parser')
            icerik = soup.find_all('div', attrs={'class':'b_attribution'})
            ek+=10
            print(icerik[0].text, icerik[1].text, icerik[2].text, icerik[3].text, sep="\n", end="\n")
            print(icerik[4].text, icerik[5].text, icerik[6].text, icerik[7].text, sep="\n", end="\n")
            print(icerik[8].text, icerik[9].text, sep="\n")
