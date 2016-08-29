"""
==========================================
Author of Fork:          Metroshica
Original Author:         Tyler Brockett
Description:    Reddit Alerts Bot
Date:           08/11/2015
==========================================
"""

import os
import sqlite3
import time
import traceback
from sys import stdout
import praw

from helpers import database, color
from helpers import inbox
from private import accountinfo

connection = None
reddit = None

subject = "gundeals bot - message from developer"
signature = "\n\t \n\t \n-Metroshica"

select_users = []


def compose_alert(username):
    # Insert alert message here!
    result = inbox.compose_greeting(username) 
    result += compose_salutation()
    return result


def run_alerts():
    global connection, select_users
    # if selected_users is empty, send to all, otherwise just send to selected_users
    i = 0
    num = 0
    if not select_users:
        needs_alert = connection.cursor().execute(database.GET_USERNAMES_THAT_NEED_ALERT).fetchall()
        num = len(needs_alert)
        for row in needs_alert:
            username = row[database.COL_ALERTS_USERNAME]
            entry = (username, 1)  # 1 == True
            try:
                reddit.send_message(username, subject, compose_alert(username))
                connection.cursor().execute(database.INSERT_ROW_ALERTS, entry)
                connection.commit()
                color.print_color('blue', 'message sent to ' + username)
                i += 1
            except:
                color.print_color('red', "ALERT FAILED: " + username + \
                                  "\n\t \n\t \n" + traceback.format_exc())
                connection.rollback()
                connection.close()
                exit()
            sleep(2)
    else:
        num = len(select_users)
        for username in select_users:
            try:
                reddit.send_message(username, subject, compose_alert(username))
                color.print_color('blue', 'message sent to ' + username)
                i += 1
            except:
                color.print_color('red', "ALERT FAILED: " + username + \
                                  "\n\t \n\t \n" + traceback.format_exc())
            sleep(2)
    print "Sent message to " + str(i) + "/" + str(num) + " users."


def compose_salutation():
    result = signature + "\n\t \n\t \n" + \
             "[code](https://github.com/metroshica/reddit-bot-gundeals)" + \
             " | /u/" + accountinfo.developerusername + \
             " | /r/gundeals\n"
    return result


def open_database():
    global connection
    connection = sqlite3.connect(os.path.realpath('.') + database.DATABASE_LOCATION)
    cursor = connection.cursor()
    cursor.execute(database.CREATE_TABLE_SUBSCRIPTIONS)
    cursor.execute(database.CREATE_TABLE_MATCHES)
    cursor.execute(database.CREATE_TABLE_ALERTS)


def connect_to_reddit():
    global reddit
    # Connecting to Reddit
    user_agent = 'Metroshica - developer'
    reddit = praw.Reddit(user_agent=user_agent)
    # TODO - TAKE OUT DISABLE WARNING AND FIGURE OUT REPLACEMENT CODE
    reddit.login(accountinfo.developerusername, accountinfo.developerpassword, disable_warning=True)


def sleep(seconds):
    print 'Sleeping',
    for i in range(seconds):
        stdout.write(".")
        stdout.flush()
        time.sleep(1)
    print ''


def initialize():
    open_database()
    connect_to_reddit()


def finish_up():
    global connection
    connection.cursor().execute(database.DROP_TABLE_ALERTS)
    connection.commit()
    connection.close()


def handle_crash(stacktrace):
    global connection, reddit
    color.print_color('red', stacktrace)
    reddit.send_message(accountinfo.developerusername, "Bot Alerts Crashed", stacktrace)
    connection.close()
    exit()


if __name__ == "__main__":
    try:
        initialize()
        run_alerts()
        finish_up()
    except:
        handle_crash(traceback.format_exc())

