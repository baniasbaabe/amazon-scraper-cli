import logging
import time

import typer

from amazon_review import AmazonReviews

app = typer.Typer()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


@app.command()
def reviews(asin: str):
    amz = AmazonReviews(asin=asin)

    all_reviews = amz.parse()

    all_reviews = {"reviews": all_reviews}

    amz.save(all_reviews)

    logger.info("Scraping completed.")


if __name__ == "__main__":
    app()
