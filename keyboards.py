import telebot
from seatable_api import Base
from telebot import types
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from config import *
base = Base(api_token, server_url)
base.auth()

def start_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.row_width = 2
    keyboard.add(InlineKeyboardButton("Хорошо", callback_data="start_ok"),)
    return keyboard

def admin_inline():
    keyboard = InlineKeyboardMarkup()
    keyboard.row_width = 2
    keyboard.add(InlineKeyboardButton("48 часов", callback_data="newsletter_48"))
    keyboard.add(InlineKeyboardButton("3 дня", callback_data="newsletter_3days"))
    keyboard.add(InlineKeyboardButton("Вебинар завтра", callback_data="newsletter_tomorrow"))
    keyboard.add(InlineKeyboardButton("Вебинар сегодня", callback_data="newsletter_today"))
    keyboard.add(InlineKeyboardButton("15", callback_data="newsletter_15"))
    keyboard.add(InlineKeyboardButton("Начали", callback_data="newsletter_started"))
    keyboard.add(InlineKeyboardButton("Начали 2", callback_data="newsletter_started2"))
    keyboard.add(InlineKeyboardButton("После", callback_data="newsletter_after"))
    return keyboard