from flask_definitions import *


@app.route('/', methods=["GET"])
def index():
    check_user_agent("soft")
    return render_template("index.html")


@app.route('/robots.txt', methods=["GET"])
def robots():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/.well-known/security.txt', methods=["GET"])
def security():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/.well-known/gpc.json', methods=["GET"])
def gpc():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/.well-known/dnt-policy.txt', methods=["GET"])
def dnt():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/favicon.ico')
def favicon():
    check_user_agent("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'static', 'images'), 'favicon.ico',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-favicon", message=e)


@app.route('/apple-touch-icon.png')
def apple_touch_icon():
    check_user_agent("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'static', 'images'), 'apple-touch-icon.png',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-apple_touch_icon", message=e)


@app.route('/android-chrome-192x192.png')
def android_chrome_192x192():
    check_user_agent("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'static', 'images'), 'android-chrome-192x192.png',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-android-chrome-192x192", message=e)


@app.route('/android-chrome-256x256.png')
def android_chrome_256x256():
    check_user_agent("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'static', 'images'), 'android-chrome-256x256.png',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-android-chrome-256x256", message=e)


@app.route('/browserconfig.xml')
def browserconfig():
    check_user_agent("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'static', 'images'), 'browserconfig.xml')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-browserconfig", message=e)


@app.route('/favicon-16x16.png')
def favicon_16x16():
    check_user_agent("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'static', 'images'), 'favicon-16x16.png',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-favicon-16x16", message=e)


@app.route('/favicon-32x32.png')
def favicon_32x32():
    check_user_agent("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'static', 'images'), 'favicon-32x32.png',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-favicon-32x32", message=e)


@app.route('/favicon.png')
def favicon_png():
    check_user_agent("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'static', 'images'), 'favicon.png',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-favicon", message=e)


@app.route('/mstile-150x150.png')
def mstile_150x150():
    check_user_agent("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'static', 'images'), 'mstile-150x150.png',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-mstile-150x150", message=e)


@app.route('/safari-pinned-tab.svg')
def safari_pinned_tab():
    check_user_agent("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'static', 'images'), 'safari-pinned-tab.svg',
                                   mimetype='image/svg+xml')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-safari-pinned-tab", message=e)


@app.route('/site.webmanifest')
def site_webmanifest():
    check_user_agent("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'static', 'images'), 'site.webmanifest')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-site.webmanifest", message=e)


@app.route('/apple-touch-icon-precomposed.png')
def apple_touch_icon_precomposed():
    check_user_agent("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'static', 'images'), 'favicon.png',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-apple-touch-icon-precomposed", message=e)


@app.route('/apple-touch-icon-120x120.png')
def apple_touch_icon_120x120():
    check_user_agent("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'static', 'images'), 'favicon.png',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-apple-touch-icon-120x120", message=e)


@app.route("/api/v1/healthcheck", methods=["GET"])
def healthcheck():
    check_user_agent("soft")
    try:
        return jsonify({"Health": "Alive"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-healthcheck", message=e)

