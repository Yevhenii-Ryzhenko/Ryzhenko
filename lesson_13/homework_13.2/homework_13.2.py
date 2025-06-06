import json
import logging

logging.basicConfig(
    filename='json__ryzhenko.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    with open('localizations_en.json', 'r', encoding='utf-8') as f1:
        data_localizations_en = json.load(f1)
except json.JSONDecodeError as e1:
    logging.error(f'The file "localizations_en.json" is not valid JSON: {e1}')

try:
    with open('localizations_ru.json', 'r', encoding='utf-8') as f2:
        data_localizations_ru = json.load(f2)
except json.JSONDecodeError as e2:
    logging.error(f'The file "localizations_ru.json" is not valid JSON: {e2}')

try:
    with open('login.json', 'r', encoding='utf-8') as f3:
        data_login = json.load(f3)
except json.JSONDecodeError as e3:
    logging.error(f'The file "login.json" is not valid JSON: {e3}')

try:
    with open('swagger.json', 'r', encoding='utf-8') as f4:
        data_swagger = json.load(f4)
except json.JSONDecodeError as e4:
    logging.error(f'The file "swagger.json" is not valid JSON: {e4}')



