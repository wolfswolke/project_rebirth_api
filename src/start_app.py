"""

"""
# ------------------------------------------------------- #
# imports
# ------------------------------------------------------- #
from threading import Thread
import time
from waitress import serve

from flask_definitions import *
import endpoints.general
import endpoints.logging
import endpoints.launcher


# ------------------------------------------------------- #
# functions
# ------------------------------------------------------- #


def run():
    serve(app, host='0.0.0.0', port=8080)


def keep_alive():
    try:
        if dev_env == "true":
            logger.graylog_logger(level="info", handler="api", message={"event": "DEV api started."})
        else:
            logger.graylog_logger(level="info", handler="api", message={"event": "api started."})
        t = Thread(target=run)
        t.daemon = True
        t.start()
        while True:
            time.sleep(100)
    except (KeyboardInterrupt, SystemExit):
        print('Received keyboard interrupt, quitting threads.')
        logger.graylog_logger(level="info", handler="api", message={"event": "api stopped."})


# ------------------------------------------------------- #
# global variables
# ------------------------------------------------------- #


# ------------------------------------------------------- #
# main
# ------------------------------------------------------- #
logger.setup_graylog(use_graylog, graylog_server)
keep_alive()