from os import environ, getenv
from dotenv import load_dotenv
from aiogram.types import Message
load_dotenv(".env")

white_id = environ.get("ADMIN_ID")

class Admin:

    def user_id_check(message : Message) -> bool:

        """This method checks, whether if the current user has an acsess to this bot or not"""
        
        user_id = str(message.from_user.id)

        if user_id != white_id:
          
          return False
          
        return True
            