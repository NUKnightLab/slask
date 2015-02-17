"""Reminds you to cool it."""
import re

def on_message(msg, context):
    """Context has keys: 'client', 'config', 'hooks'"""
    text = msg.get("text", "")

    if len(text) <= 5:
        return None
    text = re.sub(r'<@.+?>','',text) # Slack user IDs look like shouting...
    if len(text) > 4 and text.isupper():
        return "You don't have to shout."