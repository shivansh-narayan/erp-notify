from bs4 import BeautifulSoup
import requests
import solve_captcha
import constants
import change
import send
def download_captcha(soup,session):
    img = soup.findAll('img')
    div = soup.find('div',{'class':'col-sm-5 col-xs-5'})
    img = div.find('img')
    url='https://erp.bitmesra.ac.in/'+img.get('src')
    downlaod_image= session.get(url).content
    image = open('image.jpg', 'wb')
    image.write(downlaod_image)

def update_captcha():
    captcha_text= solve_captcha.getCaptcha()
    constants.payload['txtcaptcha']=captcha_text
    print('The captcha is '+captcha_text)

def updateViewState(soup):
    view=soup.find('input',{'id':'__VIEWSTATE'})
    value=view.get('value')
    constants.payload['__VIEWSTATE']=value
def login(session):
    
    post=session.post('https://erp.bitmesra.ac.in/iitmsv4eGq0RuNHb0G5WbhLmTKLmTO7YBcJ4RHuXxCNPvuIw=?enc=EGbCGWnlHNJ/WdgJnKH8DA==',data=constants.payload,headers=constants.header)
    
    soup = BeautifulSoup(post.content,'html.parser')
    html = open('afterlogin.html','wb')
    html.write(post.content)
    if('Academic' in post.text) :
        #print('Login Sccessfull')
        return True
    else :
        #print('Login Unsuccessfull')
        return False
    
    #print(soup.prettify)
    #print(constants.payload)

def getCompleteDetails(session):
    data=session.get('https://erp.bitmesra.ac.in/Academic/iitmsPFkXjz+EbtRodaXHXaPVt3dlW3oTGB+3i1YZ7alodHeRzGm9eTr2C53AU6tMBXuOAm5RgR4bqtOVgfGG9isuhw==?enc=3Q2Y1k5BriJsFcxTY7ebQh0hExMANhAKSl1CmxvOF+Y=',data=constants.payload,headers=constants.header)
    soup = BeautifulSoup(data.content,'html.parser')
    html = open('after_redirecting.html','wb')
    html.write(data.content)
    #print(soup.prettify)
    return data


def start():

    count = 0
    while True :
        print('iteration '+str(count+1))
        session = requests.Session()
        login_url = 'https://erp.bitmesra.ac.in/iitmsv4eGq0RuNHb0G5WbhLmTKLmTO7YBcJ4RHuXxCNPvuIw=?enc=EGbCGWnlHNJ/WdgJnKH8DA=='
        s = session.get(login_url)
        #print(s.content)
        soup = BeautifulSoup(s.content,'html.parser')
        download_captcha(soup,session)
        update_captcha()
        updateViewState(soup)
        #print(constants.payload)
        login_status=login(session)
        if(login_status==True):
            print('successfull login')
            stude_details=getCompleteDetails(session)
            t1=change.checkMarksChange(stude_details.content)
            t2=change.checkAttendaceChange( stude_details.content)
            if(t1 or t2):
                send.sendIt()
                return 'There was change in erp'
            break

        if(count==15):
            return ('No valid response in 15 tries !!')
            break
        
        #print(soup.prettify)
        count=count+1

    return 'there was no change in erp'

if __name__ == "__main__":
    start()