import logging


logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)-10s - %(module)s - %(funcName)s:%(lineno)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)