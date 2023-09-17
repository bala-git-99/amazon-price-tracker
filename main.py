import requests
from bs4 import BeautifulSoup
from parameters import RECEIVER
from mail_sender import send_email

product_url = "https://www.amazon.in/Faber-Castell-48-Triangular-Colour-Pencils/dp/B0825W7LP8/ref=sr_1_1?" \
              "crid=8GQS6OO3S5T7&keywords=faber%2Bcastell%2B48%2Bcolor%2Bpencil&qid=1694973949&s=electronics&" \
              "sprefix=faber%2Bcastel%2B48%2Bcolor%2Bpenc%2Celectronics%2C572&sr=1-1&th=1"

url_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 "
                  "Safari/537.36 OPR/101.0.0.0",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url=product_url, headers=url_headers)

webpage_contents = BeautifulSoup(response.text, "html.parser")

product_title = webpage_contents.select_one("#productTitle").text
product_price = int(webpage_contents.select("#corePriceDisplay_desktop_feature_div .a-price-whole")[0].text)
product_currency = webpage_contents.select("#corePriceDisplay_desktop_feature_div .a-price-symbol")[0].text
print(f"Price of the product: {product_currency}{product_price}")

# Email Body
email_content = f"{product_title} is now {product_currency.encode('utf-8')}{product_price}\n\n{product_url}\n\n\n\n" \
                f"P.S. This e-mail is sent by a Python program"
email_receiver = RECEIVER
email_subject = "Amazon Price Alert!"

target_price = 500
if product_price <= target_price:
    send_email(receiver=email_receiver, subject=email_subject, content=email_content)






