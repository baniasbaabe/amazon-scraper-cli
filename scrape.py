import logging
import time

from logger_ import logger
import typer

from amazon_review import AmazonReviews

app = typer.Typer()

@app.command()
def reviews(asin: str):
    amz = AmazonReviews(asin=asin)

    all_reviews = amz.parse()

    all_reviews = {"reviews": all_reviews}

    amz.save(all_reviews)
    
    logger.info("Scraping completed.")


if __name__ == "__main__":
    app()
