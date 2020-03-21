from bs4 import BeautifulSoup

def checkMarksChange(studDetailPage):

    soup = BeautifulSoup(studDetailPage,'html.parser')

    table = str(soup.find('table',{'id':'ctl00_ContentPlaceHolder1_grdExaMarDetl'}))
    #print(table.prettify)
    prev_marks= open('prev_marks.html','r')

    prev_marks_string = prev_marks.read()
    
    if(table==prev_marks_string):
        print('No change in marks')
    else :
        print('Change in marks')
        prev_marks.close()
        prev_marks = open('prev_marks.html','w')
        prev_marks.write(table)
        return True

    return False

def checkAttendaceChange(studDetailPage):

    soup = BeautifulSoup(studDetailPage,'html.parser')

    parent_div = (soup.find('div',{'id':'div3'}))
    #print(parent_div)
    table = str(parent_div.find('table',{'class':'table table-hover table-bordered'}))
    #print(table.prettify)
    prev_marks= open('prev_attd.html','r')

    prev_marks_string = prev_marks.read()
    
    if(table==prev_marks_string):
        print('No change in attendance')
    else :
        print('Change in attendance')
        prev_marks.close()
        prev_marks = open('prev_attd.html','w')
        prev_marks.write(table)
        return True

    return False
