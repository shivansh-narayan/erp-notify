# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
# Define these once; use them twice!

def sendIt():
    strFrom = 'narayanshivansh49@gmail.com'
    strTo = 'narayanshivansh49@gmail.com'

    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Change in Erp'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)

    # We reference the image in the IMG SRC attribute by the ID we give it below

    #attendace attach
    prev_marks= open('prev_attd.html','r')
    prev_marks_string = prev_marks.read()

    prev_attendace= open('prev_marks.html','r')
    prev_attendace_string = prev_attendace.read()
    msgText = MIMEText('<h2>Marks</h2>'+prev_attendace_string+'<h2>Attendace</h2>'+prev_marks_string, 'html')
    msgAlternative.attach(msgText)


    # Send the email (this example assumes SMTP authentication is required)

    smtp = smtplib.SMTP()
    smtp.connect('smtp.gmail.com:587')
    smtp.starttls()
    smtp.login('narayanshivansh49@gmail.com', '***REMOVED***')
    smtp.sendmail(strFrom, strTo, msgRoot.as_string())
    smtp.quit()


if __name__ == "__main__":
    sendIt()