from flask_definitions import *


@app.route('/api/v1/launcher', methods=["GET"])
def launcher():
    check_user_agent("soft")
    try:
        # todo add HTML here
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


@app.route('/api/v1/launcher/game', methods=["GET"])
def launcher_games():
    check_user_agent("soft")
    try:
        # todo move from static to DB
        # Status shown, hidden
        data = {
            "games": [
                {
                    "name": "Deathgarden Bloodharvest",
                    "image": "https://via.placeholder.com/150",
                    "status": "shown"
                },
                {
                    "name": "VHS (Video Horror Society)",
                    "image": "https://via.placeholder.com/150",
                    "status": "shown"
                }
            ]
        }
        return jsonify(data)
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-launcher-games", message=e)
        return jsonify({"status": "error"})


@app.route('/api/v1/launcher/game/<game>', methods=["GET"])
def launcher_game(game):
    check_user_agent("soft")
    try:
        # todo add DB logic here
        # Status online, maintenance, offline, error
        logger.graylog_logger(level="info", handler="launcher_game", message=f"Game Req: {game}")
        return jsonify({
            "version": "1.0.0",
            "image": "https://via.placeholder.com/150",
            "description": "Placeholder description",
            "team": "Team behind the rebirth",
            "status": "online",
            "origin": "https://store.steampowered.com/app/10/",
            "official": True
        })
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-launcher-game", message=e)
        return jsonify({"status": "error"})


@app.route('/api/v1/launcher/game/<game>/patch', methods=["GET"])
def launcher_game_patch(game):
    check_user_agent("soft")
    try:
        # todo add DB logic here
        # "providers": ["steam", "epic", "origin", "uplay", "web", "battlenet"]
        steam = {
                "app_id": 480,
                "depot_id": 481,
                "manifest_id": 3183503801510301321
        }
        # .\bnetinstaller.exe --prod prot --uid prometheus_test --lang enus --dir "<PATH>"
        battlenet = {
            "product": "prot",
            "uid": "prometheus_test",
            "lang": "enus"
        }
        provider = "steam"
        provider_value = steam
        return jsonify({
            "instructions": {
                "delete": [
                    "path/file1",
                    "path/sub/file2"
                ],
                "move": [
                    {
                        "name": "file1",
                        "source": "path/sub/",
                        "location": "path/sub2"
                    }
                ],
                "download": [
                    {
                        "name": "game.exe",
                        "location": "path/sub3"
                    }
                ]
            },
            "files": [
                {
                    "name": "game.exe",
                    "id": "1238712381283"
                },
                {
                    "name": "patch.dll",
                    "id": "184563454568"
                }
            ],
            "provider": provider,
            provider: provider_value
        })
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-launcher-game-patch", message=e)
        return jsonify({"status": "error"})
