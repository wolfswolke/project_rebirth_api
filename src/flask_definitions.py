from flask import Flask, jsonify, request, send_from_directory, abort, render_template, url_for
from logic.mongo_handler import mongo
from logic.setup_handlers import load_config
from logic.logging_handler import logger
from logic.global_handlers import session_manager
from logic.global_handlers import check_user_agent
from logic.global_handlers import sanitize_input
from logic.hash_handler import hash_handler
from logic.webhook_handler import sender
import json
import os
import random

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
mongo_server = config['mongo']['host']
mongo_db = config['mongo']['db']
mongo_user_collection = config['mongo']['user_collection']
mongo_game_collection = config['mongo']['game_collection']
mongo_game_info_collection = config['mongo']['game_info_collection']
mongo_patch_collection = config['mongo']['patch_collection']