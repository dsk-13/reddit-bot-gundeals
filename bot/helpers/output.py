'''
Output messages for commands run by bot.py
'''

import traceback
from helpers import color, logger

#Litte function to help with trying to concatenante null values and strings.
def xstr(s):
    if s is None:
        return 'None'
    return str(s)

def subscribe_exception(username, item):
    color.print_color('red', 'subscribe exception caught\n' +
                      "username:   " + username + "\n" +
                      "item:       " + item + "\n" +
                      "stacktrace: " + "\n" +
                      traceback.format_exc() + "\n\n")
    logger.log('Subscribe exception caught')


def unsubscribe_all_exception(username):
    color.print_color('red', 'unsubscribe all exception caught\n' +
                      "username:   " + username + "\n" +
                      "stacktrace: " + "\n" +
                      traceback.format_exc() + "\n\n")
    logger.log('Unsubscribe all exception caught')


def unsubscribe_exception(username, item):
    color.print_color('red', 'unsubscribe exception caught\n' +
                      "username:   " + username + "\n" +
                      "item:       " + item + "\n" +
                      "stacktrace: " + "\n" +
                      traceback.format_exc() + "\n\n")
    logger.log('Unsubscribe exception caught')


def default_exception(username, subject, body):
    color.print_color('red', 'unsubscribe exception caught\n' +
                      "username:   " + username + "\n" +
                      "subject:    " + subject + "\n" +
                      "body:       " + body + "\n" +
                      "stacktrace: " + "\n" +
                      traceback.format_exc() + "\n\n")
    logger.log('Unsubscribe exception caught')


def information_exception(username):
    color.print_color('red', 'information exception caught\n' +
                      "username:   " + username + "\n" +
                      "stacktrace: " + "\n" +
                      traceback.format_exc() + "\n\n")
    logger.log('Information exception caught')


def feedback_exception(username, user_feedback):
    color.print_color('red', 'feedback exception caught\n' +
                      "username:   " + username + "\n" +
                      "feedback:   " + "\n" + user_feedback + "\n" +
                      "stacktrace: " + "\n" +
                      traceback.format_exc() + "\n\n")
    logger.log('Feedback exception caught')


def match_exception(username, item, message_id, title, permalink, url):
    color.print_color('red', "match exception caught\n" +
                      "username:   " + username + "\n" +
                      #"email:   " + email + "\n" +
                      #"twitter:   " + twitter + "\n" +
                      "message id: " + message_id + "\n" +
                      "item:       " + item + "\n" +
                      "title:      " + title + "\n" +
                      "reddit url: " + permalink + "\n" +
                      "sale link:  " + url + "\n" +
                      "stacktrace:\n" + traceback.format_exc() + "\n\n")
    logger.log('Match exception caught')


def get_submissions_exception():
    color.print_color('red', "get submissions exception caught\n" +
                      "stacktrace:\n" + traceback.format_exc() + "\n\n")
    logger.log('Get submissions exception caught')


def read_inbox_exception():
    color.print_color('red', "read inbox exception caught\n" +
                      "stacktrace:\n" + traceback.format_exc() + "\n\n")
    logger.log('Read inbox exception caught')


def subscribe(username, item):
    color.print_color('green',
                      '-------------------------------\n' +
                      '           SUBSCRIBE\n' +
                      'username: ' + username + "\n" +
                      'item:     ' + item + "\n" +
                      '-------------------------------\n\n')
    logger.log(username + ' subscribed to ' + item)


def unsubscribe_all(username):
    color.print_color('red',
                      '-------------------------------\n' +
                      '         UNSUBSCRIBE ALL\n' +
                      'username: ' + username + "\n" +
                      '-------------------------------\n\n')
    logger.log(username + ' unsubscribed from all notifications')


def unsubscribe(username, item):
    color.print_color('red',
                      '-------------------------------\n' +
                      '           UNSUBSCRIBE\n' +
                      'username: ' + username + "\n" +
                      'item:     ' + item + '\n' +
                      '-------------------------------\n\n')
    logger.log(username + ' unsubscribed from ' + item)


def information(username):
    color.print_color('green',
                      '-------------------------------\n' +
                      '         INFORMATION\n' +
                      'username: ' + username + "\n" +
                      '-------------------------------\n\n')
    logger.log(username + ' asked for information')


def feedback(username, user_feedback):
    color.print_color('yellow',
                      '-------------------------------\n' +
                      '            FEEDBACK\n' +
                      'username: ' + username + "\n" +
                      'feedback: ' + user_feedback + "\n" +
                      '-------------------------------\n\n')
    logger.log(username + ' submitted feedback')


def default(username, subject, body):
    color.print_color('yellow',
                      '-------------------------------\n' +
                      "             DEFAULT\n" +
                      "username: " + username + "\n" +
                      "subject:  " + subject + "\n" +
                      "body:     " + body + "\n" +
                      '-------------------------------\n\n')
    logger.log(username + ' submitted an incorrect command')


def match(username, email, twitter, item, message_id, title, permalink, url):
    emailmsg = ''
    if email != None:
        emailmsg = ' and email was sent to ' + email
    color.print_color('magenta',
                      "-------------------------------\n" +
                      "        SUBMISSION MATCH\n" +
                      "username:   " + username + "\n" +
                      "email:   " + xstr(email) + "\n" +
                      "twitter:   " + xstr(twitter) + "\n" +
                      "message id: " + message_id + "\n" +
                      "item:       " + item + "\n" +
                      "title:      " + title + "\n" +
                      "reddit url: " + permalink + "\n" +
                      "sale link:  " + url + "\n" +
                      '-------------------------------\n\n')
    logger.log('Notified ' + username + ' of match for ' + item + emailmsg)


def about_message():
    color.print_color(
        'yellow',
        "================================================================\n" +
        "\t\tGunDealsBot - A Sales Notifier Bot\n" +
        "================================================================\n\n")
    color.print_color(
        'blue',
        '\n--------------------------------------------------\n' +
        '\t\twww.reddit.com/r/gundeals' + '\n' +
        '--------------------------------------------------\n')
