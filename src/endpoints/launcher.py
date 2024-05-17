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
        return jsonify({"version": "0.0.1"})
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
                    "id": "dg_bh",
                    "name": "Deathgarden Bloodharvest",
                    "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/730/library_600x900_2x.jpg?t=1696269591",
                    "status": "shown"
                },
                {
                    "id": "vhs",
                    "name": "VHS (Video Horror Society)",
                    "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/611360/library_600x900_2x.jpg?t=1671064440",
                    "status": "shown"
                },
                {
                    "id": "dg",
                    "name": "Deathgarden",
                    "image": "https://cdn.mmohuts.com/wp-content/uploads/2018/12/Deathgarden_604x423.jpg",
                    "status": "hidden"
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
        if game == "dg_bh":
            return jsonify({
                "version": "9.0.0",
                "description": "Placeholder description",
                "team": "Team Project Rebirth",
                "status": "online",
                "origin": "https://store.steampowered.com/app/555440/",
                "official": True
            })
        if game == "dg":
            return jsonify({
                "version": "1.0.0",
                "description": "Placeholder description",
                "team": "Team Project Rebirth",
                "status": "online",
                "origin": "https://store.steampowered.com/app/555440/",
                "official": True
            })
        if game == "vhs":
            return jsonify({
                "version": "1.0.0",
                "description": "Placeholder description",
                "team": "Team behind the rebirth",
                "status": "offline",
                "origin": "https://store.steampowered.com/app/611360/",
                "official": True
            })
        return jsonify({
            "version": "1.0.0",
            "description": "Placeholder description",
            "team": "Team behind the rebirth",
            "status": "maintenance",
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
        if game == "dg_bh":
            provider_value = {
                "app_id": 555440,
                "mode": "live"
            }
            provider = "steam"
            return jsonify(
                {
                    "instructions": {
                        "delete": [
                            "DEATHGARDEN\\TheExit\\Binaries\\Win64\\BattlEye\\",
                            "DEATHGARDEN\\TheExit\\Binaries\\Win64\\TheExit_BE.exe",
                        ],
                        "download": [
                            {
                                "name": "TheExitRebirthBackendAPI-WindowsNoEditor_P.pak",
                                "location": "DEATHGARDEN\\TheExit\\Content\\Paks\\",
                                "url": "https://api.zkwolf.com/updater/files/pak/",
                            },
                            {
                                "name": "TheExitRebirthBackendAPI-WindowsNoEditor_P.sig",
                                "location": "DEATHGARDEN\\TheExit\\Content\\Paks\\",
                                "url": "https://api.zkwolf.com/updater/files/sig/",
                            }
                        ],
                        "rename": [
                            {
                                "name": "TheExit.exe",
                                "location": "DEATHGARDEN\\TheExit\\Binaries\\Win64\\",
                                "new_name": "TheExit_BE.exe"
                            }
                        ]
                    },
                    "provider": provider,
                    provider: provider_value})
        elif game == "vhs":
            provider_value = {
                "app_id": 611360,
                "mode": "live"
            }
            provider = "steam"
        elif game == "dg":
            provider_value = {
                "app_id": 555440,
                "depot_id": 556,
                "manifest_id": 3183503801510301321,
                "mode": "manifest"
            }
            provider = "steam"
        else:
            provider_value = {
                "app_id": 480,
                "mode": "live"
            }
            provider = "steam"
        # .\bnetinstaller.exe --prod prot --uid prometheus_test --lang enus --dir "<PATH>"
        battlenet = {
            "product": "prot",
            "uid": "prometheus_test",
            "lang": "enus"
        }
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
                        "location": "path/sub3",
                        "url": "https://example.com"
                    }
                ],
                "rename": [
                    {
                        "name": "game.exe",
                        "location": "path/sub3",
                        "new_name": "game2.exe"
                    }
                ]
            },
            "provider": provider,
            provider: provider_value
        })
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-launcher-game-patch", message=e)
        return jsonify({"status": "error"})
