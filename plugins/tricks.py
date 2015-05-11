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
    user = context['client'].server.users.get(user_id,None)
    if user and user['name'] == 'leelou':
        for pat, func in PHRASES:
            if pat.match(command):
                return func(command)
        return None

def on_presence_change(msg, context):
    if msg.get('presence') == 'active':
        user_id = user_obj = user_name = None
        user_id = msg.get('user',None)
        if user_id:
            user_obj = context['client'].server.users.get(user_id,None)
            if user_obj:
                user_name = user_obj.get('name',None)
        logging.debug(u"Leelou sees {} ({})".format(user_id,user_name))

    return None

ROLL_OVER_GIFS = ['http://stream1.gifsoup.com/view4/2110073/french-bulldog-roll-over-o.gif', 'http://www.beheadingboredom.com/wp-content/uploads/2013/04/cat-teaches-dog-trick.gif', 'http://giphy.com/gifs/NnafYvjXZK9j2/html5']

SHAKE_GIFS = ['http://petapixel.com/assets/uploads/2011/07/dog2.jpg', 'http://petapixel.com/assets/uploads/2013/10/shake3.jpg', 'http://thumbs.dreamstime.com/x/wet-dog-shaking-6990844.jpg', 'http://pad1.whstatic.com/images/thumb/c/c4/Teach-Your-Dog-to-Shake-Hands-Step-3.jpg/670px-Teach-Your-Dog-to-Shake-Hands-Step-3.jpg', 'http://petsitterpatrol.com/wp-content/uploads/2012/04/high-five1-300x213.jpg', 'http://giphy.com/gifs/KW6evDKuJkv4s/html5', 'http://giphy.com/gifs/PWuPMJggRWDCM/html5']

PLAY_DEAD_GIFS = [ 'http://giphy.com/gifs/cute-sloth-playing-dead-y5owIXKzlPYA0', 'http://giphy.com/gifs/NaSfr9cS4maLC/html5', 'http://giphy.com/gifs/55HTlUXBKXGWA/html5', 'http://giphy.com/gifs/ZptvPz6BWZM8U/html5'  ]

def roll_over(command):
    return choice(ROLL_OVER_GIFS)

def shake(command):
    return choice(SHAKE_GIFS)

def play_dead(command):
    return choice(PLAY_DEAD_GIFS)


PHRASES = [
    (re.compile(r'^.*roll over.*$', re.IGNORECASE), roll_over),
    (re.compile(r'^.*shake.*$', re.IGNORECASE), shake,
    (re.compile(r'^.*play ded.*$', re.IGNORECASE), play_dead),
]    

