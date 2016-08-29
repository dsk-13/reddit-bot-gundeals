# reddit-bot-gundeals

## How It Works

***NOTE:*** For each of these fields (subject and body) capitalization does *not* matter, it will yield the exact same results.

#### To subscribe 
Send a private message to /u/GunDealsBot with the subject line as the item you want to receive notifications for, and the body of the message as "Subscribe". What the bot does is scans the first 100 most recent /r/gundeals submissions for either a title or body of a submission that matches the item you subscribed to. ***Currently, it must be an exact match to the term you gave me.*** I will work on using some sort of search in the future, but for now this will suffice. Because of this, try to keep your terms generic, e.g. use "AR500" instead of "AR500 Steel Targets". For now, feel free to have multiple subscriptions for the same item, just so I can cover the bases. By this, I mean it is okay to subscribe to "glock" ***and*** "g19" (notice the word "series" in the middle). Do **not** subscribe to two separate things like "glock g19" and "glock", since everything found for the second term covers that of the first. If all the subscriptions become unmanageable, I will change this rule. Also, if/when the search feature is implemented, in theory the multiple subscriptions for the same item won't be necessary.

If you would like to receive e-mail alerts, include the line "e-mail: <email address>". You will then receive an e-mail as well as a Reddit message everytime GunDealsBot finds a match. Currently you are unable to unsubscribe via e-mail. If you decide you don't want e-mail alerts anymore but still want Reddit messages, you'll have to unsubscribe from the item and re-subscribe without the email line.

#### Unsubscribe
To unsubscribe, either reply to the original message confirming your subscription to that item with the body as "Unsubscribe", or create a new message with the item to unsubscribe from as the subject and "Unsubscribe" as the body.

#### Unsubscribe from all
To Unsubscribe from ALL subscriptions you have, have the body be "Unsubscribe all" or some string that contains those two words (e.g. "All-unsubscribe" should work too). The subject can be whatever you want, or empty.

#### Get information
To get some detailed information, or view all your active subscriptions, send the bot a message with the subject as "Information" and the body whatever you want, or empty.

#### Send feedback
To send me feedback, send me a message with the subject as "Feedback" and the body whatever you want, or empty.

#### Default message
If you send a message that doesn't follow the above guidelines, you will get an error message from the bot saying the request wasn't recognized.


## Known Issues

1. If you subscribe to something like "glock g19" and "g19" the bot will treat them as different items, and you can receive matches for both for the same link. That is because everything found for the second term covers that of the first (a little more explanation is above). I will have to edit the SQL query to exclude the item as a parameter, and make it match against username and link only.


## Edits

**08/16/16 -** A ***HUGE*** shoutout to Tyler Brocket (/u/tylerbrockett) for providing most of this code. As of right now this is mostly just a fork of his code and I've changed the subreddit fron /r/buildapcsales to /r/gundeals. Hope to have some new features in the future.

**08/28/16 - Added the ability to receive e-mail notifications, read the Subscribe section above for details. As of now it's not possible to unsubscribe via e-mail, still trying to figure that one out.

## Developer Info

Author of Fork: Metroshica

Original Author: Tyler Brockett	

Bot Code: [Github Repository](https://github.com/metroshica/reddit-bot-gundeals)

Reddit: /u/Metroshica

Email: redditgundeals@gmail.com

&nbsp;
