"""Directly addressing @leelou, you can ask her to do a trick."""

import re
from random import choice

TRIGGER = re.compile(r'^@leelou\s+(.+)',re.IGNORECASE)

def on_message(msg, server):
    text = msg.get("text", "")
    match = TRIGGER.match(text)
    if not match: return

    command = match.group(1)

    for pat, func in PHRASES:
        if pat.match(command):
            return func(command)
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