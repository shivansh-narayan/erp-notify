from bs4 import BeautifulSoup
import requests
import solve_captcha

def download_captcha(soup):
    img = soup.findAll('img')
    div = soup.find('div',{'class':'col-sm-5 col-xs-5'})
    img = div.find('img')
    url='https://erp.bitmesra.ac.in/'+img.get('src')
    downlaod_image= session.get(url).content
    image = open('image.jpg', 'wb')
    image.write(downlaod_image)


session = requests.Session()
login_url = 'https://erp.bitmesra.ac.in/iitmsv4eGq0RuNHb0G5WbhLmTKLmTO7YBcJ4RHuXxCNPvuIw=?enc=EGbCGWnlHNJ/WdgJnKH8DA=='
s = session.get(login_url)

#print(s.content)
soup = BeautifulSoup(s.content,'html.parser')
download_captcha(soup)
captcha_text= solve_captcha.getCaptcha()

print(captcha_text)
#print(soup.prettify)