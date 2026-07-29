import logging

#logging.getLogger(...) creates a logger object
logger = logging.getLogger(__name__ + "_parameter_log")

#setLevel(logging.INFO) tells the logger to record INFO messages
logger.setLevel(logging.INFO)

#FileHandler("./decorator.log", "a") writes all log messages into decorator.log. "a" means append to the file if it already exists
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):

    def wrapper(*args, **kwargs):

        logger.info(f"function: {func.__name__}")

        if args:
            logger.info(f"positional parameters: {args}")
        else:
            logger.info("positional parameters: none")

        if kwargs:
            logger.info(f"keyword parameters: {kwargs}")
        else:
            logger.info("keyword parameters: none")

        result = func(*args, **kwargs)

        logger.info(f"return: {result}")
        logger.info("-" * 40)

        return result

    return wrapper

@logger_decorator
def hello_world():
    print("Hello, World!")

@logger_decorator
def test_args(*args):
    return True

@logger_decorator
def test_kwargs(**kwargs):
    return logger_decorator

hello_world()

test_args(10, 20, 30)

test_kwargs(
    first_name="Alex",
    course="Python",
    city="Wichita"
)

#print(logger)