from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

import requests
from bs4 import BeautifulSoup


class Home(MDScreen):
    def __init__(self, **kw):
        Builder.load_file("kv/home.kv")
        super().__init__(**kw)

    def get_price(self):

        try:
            url= 'https://harga-emas.org/'
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            Day = soup.find_all('table', class_ = 'in_table')[0].find('tr', style = "text-align: center; font-weight: bold;").find('td', colspan = "2").text
            table_emas_mulia = soup.find_all('table', class_ = 'in_table')[0].find('tr', style = "text-align: right;").find_all('td')[8].text
            table_emas_perhiasan = soup.find_all('table', class_ = 'in_table')[1].find_all('tr', style = 'vertical-align: top; text-align: right;')[1].find('td', bgcolor="yellow").text
            self.ids.emas_mulia.text = "RP. " + table_emas_mulia
            self.ids.emas_mulia.font_size = "40sp"
            self.ids.emas_perhiasan.text = "RP. " + table_emas_perhiasan[:7]
            self.ids.emas_perhiasan.font_size = "40sp"
            self.ids.status.text = "Data Harga pada" + Day
            self.ids.status.color = "black"

        except requests.ConnectionError:
            print('No Internet Connection')
            self.ids.emas_mulia.text = "Tidak Ada Internet"
            self.ids.emas_mulia.font_size = "20sp"
            self.ids.emas_perhiasan.text = "Tidak Ada Internet"
            self.ids.emas_perhiasan.font_size = "20sp"
            self.ids.status.text = "Tolong Hubungkan ke Internet"
            self.ids.status.color = "red"

    


