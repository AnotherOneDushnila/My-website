from aiogram.types import KeyboardButton, ReplyKeyboardMarkup



class Keyboards:

    def k_button() -> ReplyKeyboardMarkup:
        """
        Creates a keyboard with two buttons: "Get new messages" and "Get all messages".
        """
        kb = [
            [  
                KeyboardButton(text="Get new messages"),  
                KeyboardButton(text="Get all messages")   
            ]
        ]

        keyboard = ReplyKeyboardMarkup(
            keyboard=kb, 
            resize_keyboard=True,  
            input_field_placeholder="Please, choose an action:" 
        )

        return keyboard

    