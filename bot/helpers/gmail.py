'''
Module that will send emails from the redditgundeals@gmail.com account to users
that have requested e-mail alerts. Currently this will only send e-mails, it 
doesn't allow for people to unsubscribe from alerts via e-mail. Need to figure
out how to read the inbox to do that.
'''

from helpers import color, inbox
from private import accountinfo
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


def __init__(self):
    self.temp = 0


def send_email(email, username, item, title, permalink, url):
    subject = 'GunDealsBot found a match for ' + item
    sender = accountinfo.gmail_user
    recipient = email
    htmltext = inbox.compose_greeting(username) + \
    "<br><br>We have found a match for your subscription to <b>'" + item + "'</b>! " + \
    "Below you will find the details:" + \
    "<br><br><b>Deal Title:</b>" + title + \
    "<br><b>Links:</b>" + \
    "<br><a href='" + permalink + "'>Reddit Link</a>" +  \
    "<br><a href='" + url + "'>Sale Link</a>" + \
    "<br><br>To unsubscribe from these alerts, message /u/GunDealsBot with the subject '" + \
    item + "' and with the message body 'Unsubscribe'.<br>" + \
    "--GunDealBot<br><br><code><a href='https://github.com/metroshica/reddit-bot-gundeals'>Source Code on Github<a>" + \
    "<br><a href='http://reddit.com/u/metroshica'>/u/metroshica</a>" + \
    "<br><a href='http://reddit.com/r/gundeals'>/r/gundeals</a>"


    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    plaintext = "Hi there, this is just placeholder text."

    part1 = MIMEText(plaintext, 'plain')
    part2 = MIMEText(htmltext, 'html')

    msg.attach(part1)
    msg.attach(part2)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(accountinfo.gmail_user, accountinfo.gmail_pwd)
        server.sendmail(sender, recipient, msg.as_string())
        server.close()
        color.print_color('cyan', '\n\n' +
                            '----------- EMAIL SENT -----------\n' +
                            'destination: ' + email + '\n' +
                            'subject:     ' + subject + '\n\n') 
    except:
        color.print_color('red', '\n\n' +
                            '----------- EMAIL FAILED -----------\n' +
                            'destination: ' + email + '\n' +
                            'subject:     ' + subject + '\n\n') 
