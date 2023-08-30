import telegram
from django.conf import settings
from django.template.loader import render_to_string
from django.utils import timezone


def post_event_on_telegram(event):
    message_html = render_to_string('telegram_message.html', {
        'event': event
    })
    telegram_settings = settings.TELEGRAM
    bot = telegram.Bot(token=telegram_settings['bot_token'])
    bot.send_message(chat_id='%s' % telegram_settings['chat_id'],
                     text=message_html, parse_mode=telegram.ParseMode.HTML)


def send_notification_telegram(title, message):
    event = {
        'title':  title,
        'description': message,
        'start_date': timezone.now()
    }
    post_event_on_telegram(event)


def test_telegram():
    event = {
        'title': 'Susu Kuda Liar',
        'description': 'Minum Susu Yuk',
        'start_date': timezone.now,
    }
    post_event_on_telegram(event)
