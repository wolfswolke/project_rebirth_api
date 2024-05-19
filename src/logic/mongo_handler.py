import pymongo
import uuid
from logic.logging_handler import logger
import hashlib


class Mongo:
    def __init__(self):
        self.dyn_server = ""
        self.dyn_db = ""
        self.user_collection = ""
        # PYOTP for 2FA???
        self.user = {
            "user_id": "",
            "username": "",
            "password_hash": "",
            "eula": False,
            "access_level": 0,
            "raw_profile_image": ""
        }
        self.game_collection = ""
        self.game = {
            "id": "",
            "name": "",
            "image": "",
            "status": "hidden"
        }
        self.game_info_collection = ""
        self.game_info = {
            "id": "",
            "version": "0.0.0",
            "description": "Placeholder description",
            "team": "Team behind the rebirth",
            "status": "offline",
            "origin": "",
            "official": False
        }
        self.patch_collection = ""
        self.patch = {
            "id": "",
            "instructions": {
                "delete": [],
                "download": [],
                "rename": []
            },
            "provider": "",
            "provider_data": {}}
        # Maybe add a TEAM collection with ID cross-match so we know what who can change and go with that?

    def setup(self, server, db, user_collection, game_collection, game_info_collection, patch_collection):
        self.dyn_server = server
        self.dyn_db = db
        self.user_collection = user_collection
        self.game_collection = game_collection
        self.game_info_collection = game_info_collection
        self.patch_collection = patch_collection

    def user_handling(self, username, password, register=False):
        try:
            # todo change this to work
            client = pymongo.MongoClient(self.dyn_server)
            dyn_client_db = client[self.dyn_db]
            dyn_collection = dyn_client_db[self.user_collection]

            existing_document = dyn_collection.find_one({'username': username})
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            if existing_document:
                if register:
                    return {"status": "ERROR", "message": "username taken"}
                # todo Logic what to return when user is OK.
                if existing_document["password_hash"] == password_hash:
                    return {"status": "OK", "data": "SOMETHING"}
                else:
                    return {"status": "ERROR", "message": "Password wrong"}
            else:
                if not register:
                    return {"status": "ERROR", "message": "User not Found"}
                user_id = str(uuid.uuid4())
                new_user = {}
                for key, default_value in self.user.items():
                    new_user[key] = default_value

                new_user["user_id"] = user_id
                new_user["password_hash"] = password_hash
                new_user["username"] = username
                dyn_collection.insert_one(new_user)
                logger.graylog_logger(level="info", handler="mongodb", message=f"New user added to database: {username}")
                client.close()
                return {"status": "OK", "data": "SOMETHING"}
        except Exception as e:
            logger.graylog_logger(level="error", handler="mongodb_user_db_handler", message=e)
            return None

    def eula(self, userId, get_eula):
        try:
            client = pymongo.MongoClient(self.dyn_server)
            dyn_client_db = client[self.dyn_db]
            dyn_collection = dyn_client_db[self.user_collection]
            existing_document = dyn_collection.find_one({'user_id': userId})
            if existing_document:
                if get_eula:
                    eula = existing_document['eula']
                    client.close()
                    return eula
                else:
                    dyn_collection.update_one({'user_id': userId}, {'$set': {'eula': True}})
                    client.close()
                    return True
            else:
                client.close()
                return False
        except Exception as e:
            logger.graylog_logger(level="error", handler="mongodb_eula", message=e)
            return None, None

    def get_data_with_list(self, login, login_steam, items, collection):
        try:
            # todo rework
            document = {}
            login = f"{login}"
            client = pymongo.MongoClient(self.dyn_server)
            dyn_client_db = client[self.dyn_db]
            dyn_collection = dyn_client_db[collection]
            if login_steam:
                existing_document = dyn_collection.find_one({'steamid': login})
            else:
                existing_document = dyn_collection.find_one({"user_id": login})
            if existing_document:
                for item in items:
                    document[item] = existing_document.get(item)
            else:
                if login_steam:
                    print(f"No user found with steamid: {login}")
                else:
                    print(f"No user found with userId: {login}")
                client.close()
                return None
            client.close()
            return document
        except Exception as e:
            logger.graylog_logger(level="error", handler="mongo_get_data_with_list", message=e)
            return None

    def get_object(self, game_id, collection):
        client = pymongo.MongoClient(self.dyn_server)
        dyn_client_db = client[self.dyn_db]
        dyn_collection = dyn_client_db[collection]
        existing_document = dyn_collection.find_one({"id": game_id})
        if existing_document:
            return existing_document
        else:
            return {"status": "ERROR", "message": "ID not found"}

    def write_data_with_list(self, login, login_steam, items_dict, collection):
        try:
            # todo rework
            client = pymongo.MongoClient(self.dyn_server)
            dyn_client_db = client[self.dyn_db]
            dyn_collection = dyn_client_db[collection]
            if login_steam:
                steam_id = str(login)
                existing_document = dyn_collection.find_one({'steamid': steam_id})
            else:
                user_id = str(login)
                existing_document = dyn_collection.find_one({"user_id": user_id})
            if existing_document:
                update_query = {'$set': items_dict}
                if login_steam:
                    dyn_collection.update_one({'steamid': steam_id}, update_query)
                else:
                    dyn_collection.update_one({"user_id": user_id}, update_query)
                client.close()
                return {"status": "success", "message": "Data updated"}
            else:
                print(f"No user found with steamid: {steam_id}")
                client.close()
                return None
        except Exception as e:
            print(e)
            logger.graylog_logger(level="error", handler="mongo_write_data_with_list", message=e)
            return None

    def add_game(self, user_id, data):
        # Add all 3 base infos with the data
        pass

    def update_game(self, user_id, data):
        # update game
        pass

    def update_game_info(self, user_id ,data):
        # update game info data
        pass

    def update_patch(self, user_id, patch):
        # update patch
        pass

    def get_game(self, game_id):
        data = self.get_object(game_id, self.game_collection)
        return data

    def get_game_info(self, game_id):
        data = self.get_object(game_id, self.game_info_collection)
        return data

    def get_patch(self, game_id):
        data = self.get_object(game_id, self.patch_collection)
        return data


mongo = Mongo()
