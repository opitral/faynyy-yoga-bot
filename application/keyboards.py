from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class StartPracticeCbData(CallbackData, prefix="start_practice"):
    pass

class WantInGroupCbData(CallbackData, prefix="want_in_group"):
    pass

class WantIndividuallyCbData(CallbackData, prefix="want_individually"):
    pass


class BackToStartCbData(CallbackData, prefix="back_to_start"):
    pass


START_KB = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🦾старт практики",
                callback_data=StartPracticeCbData().pack()
            ),
        ],
        [
            InlineKeyboardButton(
                text="⭐хочу в міні-групу",
                callback_data=WantInGroupCbData().pack()
            ),
        ],
        [
            InlineKeyboardButton(
                text="⭐хочу персональне тренування",
                callback_data=WantIndividuallyCbData().pack()
            )
        ]
    ]
)

RETURN_TO_START_BTN = InlineKeyboardButton(
    text="🔙Повернутись в меню",
    callback_data=BackToStartCbData().pack()
)


RETURN_TO_START_KB = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            RETURN_TO_START_BTN
        ]
    ]
)

WANT_INDIVIDUALLY_KB = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Анкета тут",
                url="https://forms.gle/fA5DvwsXgTjmnVvw6"
            )
        ],
        [
            RETURN_TO_START_BTN
        ]
    ]
)

SUBSCRIBE_KB = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Підписатись✅",
                url="https://www.instagram.com/faynyy?igsh=MXUxOXRzZ3pxdmhocg%3D%3D&utm_source=qr"
            )
        ],
        [
            RETURN_TO_START_BTN
        ]
    ]
)

START_PRACTICE_KB = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🦾старт практики",
                url="https://youtu.be/nyHFKVLXV64"
            )
        ]
    ]
)
