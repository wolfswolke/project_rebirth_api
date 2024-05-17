import random

from flask_definitions import *


@app.route('/api/v1/log', methods=["POST"])
def log():
    check_user_agent("soft")
    random_id = random.randint(1, 10000000)
    try:
        data = request.json
        logger.graylog_logger(level="info", handler="log_upload", message=data)
        return jsonify({"status": "success", "random_id": random_id}), 200
    except TimeoutError:
        return jsonify({"status": "error"}), 500
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-log", message=e)
        return jsonify({"status": "UNKNOWN ERROR"}), 500


@app.route("/api/v1/bug_report", methods=["POST"])
def bug_report():
    check_user_agent("soft")
    try:
        # Data:
        # {"Reporter": "STRING", "Description": "STRING", "Steps": "STRING", "Expected": "STRING", "Discord": "STRING",
        # "Email": "STRING", "Attachments": "FILE", "Logs": "FILE", "Anonymous": "BOOL"}
        data = request.json
        logger.graylog_logger(level="info", handler="bug_report", message=data)
        sender(discord_urls,
               "Bug Report",
               f"Reporter: {data['Reporter']}\nDescription: "
               f"{data['Description']}\nSteps: {data['Steps']}\nExpected: "
               f"{data['Expected']}\nContact: {data['contact']}\nLogID: {data['log_id']}")
        return jsonify({"status": "success"})
    except TimeoutError:
        return jsonify({"status": "error"}), 500
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-bug_report", message=e)
        return jsonify({"status": "UNKNOWN ERROR"}), 500
