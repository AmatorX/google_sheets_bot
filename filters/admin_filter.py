# from aiogram.filters import BaseFilter
# from aiogram.types import Message
# from config_data.config import Config, load_config
#
# config: Config = load_config('.env')
# admins = config.tg_bot.admin_ids
#
#
# # Собственный фильтр, проверяющий юзера на админа
# class IsAdmin(BaseFilter):
#     def __init__(self, admin_ids: list[int]) -> None:
#         # В качестве параметра фильтр принимает список с целыми числами
#         self.admin_ids = admin_ids
#
#     async def __call__(self, message: Message) -> bool:
#         return message.from_user.id in self.admin_ids
