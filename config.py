import random
import json
from datetime import datetime

TOKEN = ''


OWNER_ID = 298410723586080768


months = {
    1: 'января',
    2: 'февраля',
    3: 'марта',
    4: 'апреля',
    5: 'мая',
    6: 'июня',
    7: 'июля',
    8: 'августа',
    9: 'сентября',
    10: 'октября',
    11: 'ноября',
    12: 'декабря'
}

sw_pattern = r'^\d{4}-\d{4}-\d{4}$'

colors = [0x9dffb0, 0x81f1f7, 0xfffffa, 0xc48d3f, 0xfff563, 0x84d9e0]

with open('text/isabelle_holiday_phrases.json', 'r', encoding='utf-8') as f:
    holiday_phrases = json.load(f)

# Loading data from JSON file
with open("text/bdays.json", "r") as f:
    bdays = json.load(f)

# Loading data from TXT file with random phrases
with open('text/isabelle_random_phrases.txt', 'r', encoding='utf-8') as f:
    random_phrases = f.readlines()

# Loading data from TXT file with random greetings
with open('text/greetings.txt', 'r', encoding='utf-8') as f:
    random_greetings = f.readlines()

# Loading data from TXT file which appears if no users has birthday
with open("text/no_bday.txt", "r") as f:
    no_bday_phrases = f.readlines()


# Function to get random message from isabelle_random_phrases.txt
def get_random_message():
    return random.choice(random_phrases)


# Function to get random message from greetings.txt
def get_random_greeting():
    return random.choice(random_greetings)


# Function for checking, if today is holiday
def is_holiday_today():
    today = datetime.today()
    month_day = f'{today.day:02d}.{today.month:02d}'
    holiday = holiday_phrases.get(month_day)
    return holiday
