import requests

from html5lib import parse
from bs4 import BeautifulSoup
import smtplib
URL = 'https://www.amazon.in/Fossil-Touchscreen-Smartwatch-Smartphone-Notifications/dp/B07SSVWD1X/ref=sr_1_3?crid=1BHGHWUEIQNTG&dchild=1&keywords=fossil+smart+watch+gen+5&qid=1595172090&sprefix=fossil++smart+watch%2Caps%2C387&sr=8-3'

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.64'}

def check_price():
    page = requests.get(URL,headers=headers)


    soup = BeautifulSoup(page.content,  "html.parser")

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[2:4])
    

    #if converted_price < 13000:
      #  send_mail()
    
    print(converted_price)
    print(title.strip())

    

    if converted_price < 130:
        send_mail()
    else:
        print('The price is still high')

def send_mail():
   #/* pagep = requests.get(URL,headers=headers)


    #soupp = BeautifulSoup(pagep.content,  "html.parser")

    #titlep = soupp.find(id="productTitle").get_text()
    #pricep = soupp.find(id='priceblock_ourprice').get_text()
    # converted_pricep = float(pricep[2:4])
    # cp = pricep[0:8]
    # tile = titlep.strip()*

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('fardeenkhan.works365@gmail.com','@f1478956K')

    subject = 'Fardeen fossil wacth is < rs 13000'
    body = 'Price of  is below Rs 13000  \n Check the link for the price https://www.amazon.in/Fossil-Touchscreen-Smartwatch-Smartphone-Notifications/dp/B07SSVWD1X/ref=sr_1_3?crid=1BHGHWUEIQNTG&dchild=1&keywords=fossil+smart+watch+gen+5&qid=1595172090&sprefix=fossil++smart+watch%2Caps%2C387&sr=8-3'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'fardeenkhan.works365@gmail.com',
        'fardeenkhan.nmims@gmail.com',
        msg
    )

    print('The Mail has been sent!!')

    server.quit()

check_price()