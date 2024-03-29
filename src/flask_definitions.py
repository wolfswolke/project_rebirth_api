from flask import Flask, jsonify, request, send_from_directory, abort, render_template, url_for
from logic.setup_handlers import load_config
from logic.logging_handler import logger
from logic.global_handlers import session_manager
from logic.global_handlers import check_user_agent
from logic.global_handlers import sanitize_input
from logic.hash_handler import hash_handler
from logic.webhook_handler import sender as discord_sender
import json
import os

app = Flask(__name__)

config = load_config()
use_graylog = config['graylog']['use']
graylog_server = config['graylog']['host']
dev_env = os.environ['DEV']
local_ip = config['local_ip']
discord_urls = config['discord']['webhook_urls']
use_discord = config['discord']['use']
version = config['global']['version']
name = config['global']['name']
