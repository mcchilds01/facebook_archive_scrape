import csv
from bs4 import BeautifulSoup

rows = []

with open("facebook-mattchilds313/ads_and_businesses/advertisers_you've_interacted_with.html") as f:
    soup = BeautifulSoup(f, 'html.parser')
    contents = soup.find('div', class_='_4t5n')
    ads_list = contents.find_all('div', class_='uiBoxWhite')

for ad in ads_list:
    adName = ad.find('div', class_='_2let').get_text()
    timeClicked = ad.find('div', class_='_2lem').get_text()
    row = {
        'advertisement': adName,
        'time accessed': timeClicked
    }
    rows.append(row)

with open('my_ads.csv', 'w') as csv_file:
    fieldnames  = ['advertisement', 'time accessed']
    csv_writer = csv.DictWriter(csv_file, fieldnames)
    csv_writer.writeheader()
    for row in rows:
        csv_writer.writerow(row)
        
"""Based on an exercise in Lam Thuy Vo's "Mining Social Media", No Starch Press, 2020"""
