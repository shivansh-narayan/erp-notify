from bs4 import BeautifulSoup

def checkMarksChange(studDetailPage):

    soup = BeautifulSoup(studDetailPage,'html.parser')

    table = str(soup.find('table',{'id':'ctl00_ContentPlaceHolder1_grdExaMarDetl'}))
    #print(table.prettify)
    prev_marks= open('prev_marks.html','r')

    prev_marks_string = prev_marks.read()
    
    if(table==prev_marks_string):
        print('Print no change in marks')
    else :
        print('Change in marks')
        prev_marks.close()
        prev_marks = open('prev_marks.html','w')
        prev_marks.write(table)


    