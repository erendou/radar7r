import os
import requests
from bs4 import BeautifulSoup
import time
from telegram import Bot

TOKEN = os.getenv('8069247846:AAHpBMszmk_BscL7PHpPU5ckM4-X_3LBYwM')
CHAT_ID = os.getenv('1011874258')

bot = Bot(token=TOKEN)

def get_last_colors():
    url = 'https://casinoscores.com/xxxtreme-lightning-roulette/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    colors = []
    results_div = soup.find('div', class_='results')
    if not results_div:
        return []
    for span in results_div.find_all('span', class_=['red', 'black', 'green']):
        if 'red' in span['class']:
            colors.append('red')
        elif 'black' in span['class']:
            colors.append('black')
        elif 'green' in span['class']:
            colors.append('green')
    return colors[:10]

def main():
    last_check = []
    while True:
        try:
            colors = get_last_colors()
            if len(colors) < 2:
                print("Yeterli sonuç yok.")
                time.sleep(10)
                continue

            if colors[0] == colors[1] and colors[0] != 'green':
                if last_check != colors[:2]:
                    msg = f"⚠️ İki kere üst üste {colors[0]} geldi!"
                    print(msg)
                    bot.send_message(chat_id=CHAT_ID, text=msg)
                    last_check = colors[:2]
            else:
                last_check = []
        except Exception as e:
            print(f"Hata: {e}")
        time.sleep(10)

if __name__ == '__main__':
    main()
