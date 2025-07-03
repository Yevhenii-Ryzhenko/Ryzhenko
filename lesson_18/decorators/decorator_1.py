import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f'Calling function: {func.__name__}')
        logger.info(f'Arguments: args={args}, kwargs={kwargs}')
        result = func(*args, **kwargs)
        logger.info(f'Result: {result}')
        return result
    return wrapper

@logging_decorator
def for_testing_logging_decorator(a,b):
    return a + b

for_testing_logging_decorator(2,3)
