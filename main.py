import smtplib

import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/118.0.0.0 Safari/537.36'
    ),
    'Accept-Language': 'en-IN,en;q=0.9',
}
url = 'https://www.flipkart.com/apple-iphone-15-blue-128-gb/p/itm387c20f1f5347?pid=MOBHQV9YZGYG64U7&param=7681&pageUID=1793008845779'
response = requests.get(url=url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
curr_price = soup.find(class_='v1zwn21n v1zwn20 _1psv1zeb9 _1psv1ze0').get_text()
# print(curr_price)
curr_price_without_sym = curr_price.replace('₹', '')
# print(curr_price_without_sym)
curr_price_without_comma = curr_price_without_sym.replace(',', '')
# print(curr_price_without_comma)
final_current_price = float(curr_price_without_comma)
print(final_current_price)

title = soup.find(class_='v1zwn21n v1zwn27 _1psv1zeb9 _1psv1ze0').get_text()
expected_price = 70000
if final_current_price < expected_price:
    message = f'{title} is on sale for {final_current_price}'
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(os.getenv('SMTP_EMAIL'), os.getenv('SMTP_PASS'))
        connection.sendmail(
            from_addr=os.getenv('SMTP_EMAIL'),
            to_addrs=os.getenv('SMTP_EMAIL'),
            msg=f'Subject:Flipkart Price Alert!\n\n{message}\n{url}'.encode('utf-8')
        )