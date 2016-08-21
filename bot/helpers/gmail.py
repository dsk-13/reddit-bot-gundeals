'''
Module that will send emails from the redditgundeals@gmail.com account to users
that have requested e-mail alerts. Currently this will only send e-mails, it 
doesn't allow for people to unsubscribe from alerts via e-mail. Need to figure
out how to read the inbox to do that.
'''

from helpers import color, inbox
from private import accountinfo
import smtplib


def __init__(self):
    self.temp = 0


def send_email(email, username, item, title, permalink, url):
    FROM = accountinfo.gmail_user
    TO = email
    subject = 'We found something'
    SUBJECT = subject
    TEXT = inbox.compose_greeting(username) + \
    "We have found a match for your subscription to '" + item + "'! " + \
    "Below you will find the details:\n\t \n\t \n" + \
     "**Deal Title:**\t \n" + \
     title + "\t \n\t \n" + \
     "**Links:**\t \n" + \
     "[Reddit URL](" + permalink + ")" + "     |     " + \
     "[Sale URL](" + url + ")\n\n" + \
     "To unsubscribe from these alerts, message /u/GunDealsBot with the subject " + \
     item + "and with the message body 'Unsubscribe'.\n\n" + \
     inbox.compose_salutation()

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(accountinfo.gmail_user, accountinfo.gmail_pwd)
        server.sendmail(FROM, TO, TEXT)
        server.close()
        color.print_color('cyan', '\n\n' +
                            '----------- EMAIL SENT -----------\n' +
                            'destination: ' + email + '\n' +
                            'subject:     ' + subject + '\n' +
                            'message:     ' + message + '\n\n\n')
    except:
        color.print_color('red', '\n\n' +
                            '----------- EMAIL FAILED -----------\n' +
                            'destination: ' + email + '\n' +
                            'subject:     ' + subject + '\n' +
                            'message:     ' + message + '\n\n\n')
