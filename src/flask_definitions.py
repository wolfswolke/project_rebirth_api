from flask import Flask, jsonify, request, send_from_directory, abort, render_template, url_for
from logic.setup_handlers import load_config
from logic.logging_handler import logger
from logic.global_handlers import session_manager
from logic.global_handlers import check_user_agent
from logic.global_handlers import sanitize_input
from logic.hash_handler import hash_handler
import json
import os

app = Flask(__name__)

config = load_config()
use_graylog = config['graylog']['use']
graylog_server = config['graylog']['host']
dev_env = os.environ['DEV']
local_ip = config['local_ip']
