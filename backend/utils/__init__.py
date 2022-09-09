import time
import logging
import functools

logging.basicConfig(
    level=logging.INFO, format="[%(module)s] [%(levelname)s] %(asctime)s --  %(message)s"
)
logger = logging.getLogger(__name__)

def wait(in_seconds: int):
    def _wait(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            res = fn(*args, **kwargs)
            logger.info(f"Waiting for {in_seconds}s ...")
            time.sleep(in_seconds)
            return res
        return wrapper
    return _wait