from aiogram import types
from aiogram.dispatcher import FSMContext
from config import dp, bot
from database import Task, Priority, Template
from keyboards import *
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    text = "📝 Todo Bot: Управляй задачами как профи!"
    await message.answer(text, reply_markup=main_keyboard())

# Создание задачи с приоритетом
@dp.message_handler(commands=['add_task'])
async def add_task(message: types.Message):
    await message.answer("Введите название задачи:", reply_markup=priority_keyboard())

@dp.callback_query_handler(lambda c: c.data.startswith('priority'))
async def set_priority(callback: types.CallbackQuery):
    priority = callback.data.split('_')[1]
    # Сохраняем в FSM контекст и запрашиваем остальные данные
    # ... (полная реализация зависит от вашего FSM)

# Показ статистики
@dp.message_handler(commands=['stats'])
async def show_stats(message: types.Message):
    tasks = get_user_tasks(message.from_user.id)  # Ваша функция для выборки из БД
    
    # Генерация графика
    plt.figure(figsize=(10,5))
    categories = [t.category for t in tasks]
    plt.hist(categories, bins=len(set(categories)))
    plt.title("Распределение задач по категориям")
    plt.savefig('stats.png')
    
    await message.answer_photo(photo=open('stats.png', 'rb'))

# Умные напоминания (крон-задача)
async def check_postponed_tasks():
    tasks = session.query(Task).filter(Task.postponed_count > 3).all()
    for task in tasks:
        await bot.send_message(
            task.user_id,
            f"⚠️ Задача '{task.title}' переносится {task.postponed_count} раз. Может, её удалить?",
            reply_markup=postponed_keyboard(task.id)
        )

# Применение шаблона
@dp.message_handler(commands=['apply_template'])
async def apply_template(message: types.Message):
    templates = get_user_templates(message.from_user.id)
    await message.answer("Выберите шаблон:", reply_markup=templates_keyboard(templates))
