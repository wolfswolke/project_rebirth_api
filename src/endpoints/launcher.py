from flask_definitions import *


@app.route('/api/v1/launcher', methods=["GET"])
def launcher():
    check_user_agent("soft")
    try:
        # INFO HERE
        return jsonify({"status": "success"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-launcher", message=e)
        return jsonify({"status": "error"})


@app.route('/api/v1/launcher/download', methods=["GET"])
def launcher_download():
    check_user_agent("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'tmp'), 'project_rebirth_launcher.zip')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-launcher-download", message=e)
        return jsonify({"status": "error"})


@app.route('/api/v1/launcher/version', methods=["GET"])
def launcher_version():
    check_user_agent("soft")
    try:
        return jsonify({"version": "1.0.0"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-launcher-version", message=e)
        return jsonify({"status": "error"})
