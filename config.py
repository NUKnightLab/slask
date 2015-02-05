import logging
import os
logger = logging.getLogger(__name__)

loglevel = os.environ.get('SLACK_LEELOU_LOGLEVEL', logging.WARN)

try:
    loglevel = int(loglevel)
except:
    try:
        loglevel = int(LEVELS[loglevel])
    except KeyError:
        loglevel = logging.WARN
        logger.warn("Invalid loglevel in config file. Defaulting to WARN")
config = {
    # Your slask API token
    "token": os.environ.get('SLACK_LEELOU_KEY'),

    # The log level. Valid options are logging.{DEBUG, INFO, WARNING, ERROR, CRITICAL})
    "loglevel": loglevel

    # The log file to write to. By default writes to whatever the pwd is, you probably want
    # to change that. The log goes to stderr unless you uncomment this
    #"logfile": "slask.log",

    # The log file format. This is the default; you can uncomment this line to change it if you want
    # "logformat": '%(asctime)s:%(levelname)s:%(message)s',
}
