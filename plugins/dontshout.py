"""Reminds you to cool it."""

def on_message(msg, context):
    """Context has keys: 'client', 'config', 'hooks'"""
    text = msg.get("text", "")

    if len(text) <= 5:
        return None
    text = re.sub(r'<@.+?>','',text) # Slack user IDs look like shouting...
    if text == text.upper():
        return "You don't have to shout."