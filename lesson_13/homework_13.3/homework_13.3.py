import xml.etree.ElementTree as ET
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

tree = ET.parse('groups.xml')
root = tree.getroot()

"""
Реалізовано введення числа для пошуку. Для перевірки ДЗ можна закоментувати 19-й рядок, і прибрати коментування 20-го
"""

find_number = input('Enter number what you find (0-5):')
# find_number = 0
found = False

for group in root.findall('group'):
    number = group.find('number')
    if number is not None and number.text == str(find_number):
        found = True
        timing_exbytes = group.find('timingExbytes')
        if timing_exbytes is not None:
            incoming = timing_exbytes.find('incoming')
            if incoming is not None:
                logger.info(f'The number {number.text} you are looking for has incoming: {incoming.text}')
            else:
                logger.warning(f'The number {number.text} you are looking for has not incoming')
        else:
            logger.error(f'The number {number.text} you are looking for has no timing_exbytes')
        break
if not found:
    logger.critical(f'The file does not contain the number you are looking for: {find_number}')
