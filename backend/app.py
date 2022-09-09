import logging

logging.basicConfig(
    level=logging.INFO, format="[%(module)s] [%(levelname)s] %(asctime)s --  %(message)s"
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    pass