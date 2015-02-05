"""!define <text> returns the Wordnik definition for the word (or maybe the URL for the wordnik page?)"""
import os
import re
import logging
from wordnik import *

logger = logging.getLogger(__name__)
WORDNIK_API_KEY = os.environ.get('WORDNIK_API_KEY')

apiUrl = 'http://api.wordnik.com/v4'
client = swagger.ApiClient(WORDNIK_API_KEY, apiUrl)
wordApi = WordApi.WordApi(client)

if not WORDNIK_API_KEY:
    logger.warn("You must set the WORDNIK_API_KEY environment variable to use this plugin.")

def define(text):
    definitions = wordApi.getDefinitions(text)
    lines = []
    for d in definitions:
        lines.append('*{}* _({})_: {}'.format(d.word, d.partOfSpeech, d.text))
    return '\n'.join(lines)

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!define (.*)", text)
    if not match: return

    return define(match[0])
