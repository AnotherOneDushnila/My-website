from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import html, F, Router
from Keyboards.keyboards import Keyboards
from Base.base import *
from Admin.admin import *




router = Router()


def non_admin_response(message : Message) -> Message:
    """
    This handler sends a message, if current user isn't an admin.
    """
    return message.answer(f"Hello, {html.bold(message.from_user.full_name)}!\n You aren't an admin, so you don't have an acsess to this bot")



@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    if Admin.user_id_check(message=message):

        await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!\n Do you want to get new messages from your website?", 
                    reply_markup=Keyboards.k_button())
        
    else:   

        await message.answer(non_admin_response(message))
    


@router.message(F.text.lower() == "get new messages")
async def get_new_messages(message: Message) -> Message:
    """
    This handler gets new messages from my website database
    """
    if Admin.user_id_check(message):

        try:
            data = Base.fetch_new()
            await message.reply(f"Here are some new messages:\n{data}")

        except:
            message.answer(f"Sorry, something went wrong!")
   
    else:
        
        await message.answer(non_admin_response(message))



@router.message(F.text.lower() == "get all messages")
async def all_messages(message: Message) -> Message:
    """
    This handler gets all messages from my website database
    """
    if Admin.user_id_check(message):

        try:
            data = Base.fetch_all()
            await message.reply(f"Here are all messages:\n{data}")

        except:
            message.answer(f"Sorry, something went wrong!")

    else:
        
        await message.answer(non_admin_response(message))
