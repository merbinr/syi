import logging


def get_logger() -> logging.Logger:
    """Create logger and return it"""
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logger = logging.getLogger("collector")
    logger.setLevel(logging.INFO)
    return logger
