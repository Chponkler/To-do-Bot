from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

def main_keyboard():
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        "📥 Новая задача", "📊 Статистика"
    ).row("🔄 Шаблоны", "⚙️ Настройки")

def priority_keyboard():
    return InlineKeyboardMarkup().row(
        InlineKeyboardButton("🔴 Высокий", callback_data="priority_high"),
        InlineKeyboardButton("🟡 Средний", callback_data="priority_medium"),
        InlineKeyboardButton("🟢 Низкий", callback_data="priority_low")
    )

def templates_keyboard(templates):
    keyboard = InlineKeyboardMarkup()
    for template in templates[:3]:  # Только 3 шаблона для мобил
        keyboard.add(InlineKeyboardButton(template.name, callback_data=f"template_{template.id}"))
    return keyboard
