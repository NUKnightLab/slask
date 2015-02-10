"""Directly addressing @leelou, you can ask her to do a trick."""

import re
from random import choice
import logging
# U03J911F1
TRIGGER = re.compile(r'<@(.+)>\s+(.+)',re.IGNORECASE)

def on_message(msg, context):
    """Context has keys: 'client', 'config', 'hooks'"""
    text = msg.get("text", "")
    match = TRIGGER.match(text)
    if not match: return

    user_id, command = match.groups()
    if user_id == 'U03J911F1' or user_id == 'leelou':
        logging.debug(context['client'].server.users.get(user_id,'no such user id'))
        for pat, func in PHRASES:
            if pat.match(command):
                logging.debug(u"Leelou matched /{}/".format(pat.pattern))
                return func(command)
        logging.debug(u"Leelou doesn't know how to {}".format(command))
        return None

def on_presence_change(msg, context):
    if msg.get('presence') == 'active':
        logging.debug(u"Leelou sees {}".format(msg.get('user',"no user?")))
    return None

ROLL_OVER_GIFS = ['http://stream1.gifsoup.com/view4/2110073/french-bulldog-roll-over-o.gif', 'http://www.beheadingboredom.com/wp-content/uploads/2013/04/cat-teaches-dog-trick.gif', 'http://giphy.com/gifs/dog-puppy-tired-NnafYvjXZK9j2', 'http://giphy.com/gifs/cute-sloth-playing-dead-y5owIXKzlPYA0' ]

SHAKE_GIFS = ['http://petapixel.com/assets/uploads/2011/07/dog2.jpg', 'http://petapixel.com/assets/uploads/2013/10/shake3.jpg', 'http://thumbs.dreamstime.com/x/wet-dog-shaking-6990844.jpg', 'http://pad1.whstatic.com/images/thumb/c/c4/Teach-Your-Dog-to-Shake-Hands-Step-3.jpg/670px-Teach-Your-Dog-to-Shake-Hands-Step-3.jpg', 'http://petsitterpatrol.com/wp-content/uploads/2012/04/high-five1-300x213.jpg']

def roll_over(command):

    return choice(ROLL_OVER_GIFS)

def shake(command):
    return choice(SHAKE_GIFS)


PHRASES = [
    (re.compile(r'^.*roll over.*$', re.IGNORECASE), roll_over),
    (re.compile(r'^.*shake.*$', re.IGNORECASE), shake),
]    