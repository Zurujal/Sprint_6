import data
import random

from faker import Faker


def generate_name():
    return random.choice(data.NAMES)


def generate_surname():
    return random.choice(data.SURNAMES)


def generate_phone_number():
    number = random.randint(0000000000, 9999999999)
    return f'+7{number}'


def generate_address():
    return random.choice(data.ADDRESS)


def generate_station_name():
    return random.choice(data.STATION_NAMES)


def generate_date():
    fake = Faker()
    return fake.date()


def generate_duration_name():
    return random.choice(data.DURATION_NAMES)


def generate_scooter_color():
    return random.choice(data.SCOOTER_COLORS)


def generate_text():
    fake = Faker()
    return fake.text(max_nb_chars=200)
