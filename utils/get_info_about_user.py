import json


def get_user_info(user_id: int, path: str):
    """
    Функция добавления данных текущего пользователя в data машины состояний
    """
    name, sh_url, materials = None, None, None
    with open(path, 'r', encoding="utf-8") as file:
        data = json.load(file)
        for key, building_data in data.items():
            users = building_data.get("users", {})
            if str(user_id) in users:
                name = users.get(str(user_id))
                sh_url = building_data.get("sh_url", None)
                materials = building_data.get("materials", {})
                building = key
                return name, sh_url, materials, building

