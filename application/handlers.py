from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_command_handler(message: Message):
    await message.answer("Hi!")


@router.message()
async def unknown_commands_handler(message: Message):
    await message.answer("Unknown command, please use /start to begin 😕")
