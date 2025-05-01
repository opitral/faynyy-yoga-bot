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

WANT_IN_GROUP_BNT = InlineKeyboardButton(
    text="💫Хочу в міні-групу",
    callback_data=WantInGroupCbData().pack()
)


WANT_INDIVIDUALLY_BNT = InlineKeyboardButton(
    text="🔝Хочу індивідуально",
    callback_data=WantIndividuallyCbData().pack()
)

START_KB = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🦾Старт практики",
                callback_data=StartPracticeCbData().pack()
            ),
        ],
        [
            WANT_IN_GROUP_BNT
        ],
        [
            WANT_INDIVIDUALLY_BNT
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

SUBSCRIBE_BTN = InlineKeyboardButton(
    text="Підписатись✅",
    url="https://www.instagram.com/faynyy?igsh=MXUxOXRzZ3pxdmhocg%3D%3D&utm_source=qr"
)

SUBSCRIBE_KB = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            SUBSCRIBE_BTN
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
                text="🦾Старт практики",
                url="https://youtu.be/nyHFKVLXV64"
            )
        ]
    ]
)

REMEMBER_KB = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            WANT_IN_GROUP_BNT
        ],
        [
            WANT_INDIVIDUALLY_BNT
        ],
        [
            SUBSCRIBE_BTN
        ]
    ]
)