from helpers import color
from private import accountinfo
import smtplib


def __init__(self):
    self.temp = 0


def send_email(self, destination, subject, message):
    color.print_color('cyan', '\n\n' +
                            '----------- MESSAGE SENT -----------\n' +
                            'destination: ' + destination + '\n' +
                            'subject:     ' + subject + '\n' +
                            'message:     ' + message + '\n\n\n')
    FROM = accountinfo.gmail_user
    TO = destination
    SUBJECT = subject
    TEXT = message

    email = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        color.print_color('cyan', '\n\n' +
                            '----------- EMAIL SENT -----------\n' +
                            'destination: ' + destination + '\n' +
                            'subject:     ' + subject + '\n' +
                            'message:     ' + message + '\n\n\n')
    except:
        color.print_color('red', '\n\n' +
                            '----------- EMAIL FAILED -----------\n' +
                            'destination: ' + destination + '\n' +
                            'subject:     ' + subject + '\n' +
                            'message:     ' + message + '\n\n\n')
