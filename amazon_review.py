import json
import logging

from playwright.sync_api import sync_playwright
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

logger = logging.getLogger(__name__)


class AmazonReviews:
    def __init__(self, asin, max_pages=25) -> None:
        self.asin = asin
        self.url = f"https://www.amazon.com/-/de/product-reviews/{self.asin}/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="
        self.max_pages = max_pages

    def pagination(self, page_obj, page_num):
        page_obj.goto(self.url + str(page_num))
        try:
            return page_obj.query_selector_all("div[data-hook='review']")
        except Exception:
            logger.info("No reviews left.")
            return False

    def parse(self):
        total = []
        with logging_redirect_tqdm():
            for page_num in tqdm(range(1, self.max_pages)):
                with sync_playwright() as p:
                    browser = p.chromium.launch(headless=True)
                    page = browser.new_page()
                    page.route(
                        "**/*",
                        lambda route: route.abort()
                        if route.request.resource_type == "image"
                        else route.continue_(),
                    )

                    reviews = self.pagination(page, page_num)
                    if reviews:
                        for review in reviews:
                            try:
                                # title = review.find_element(By.CSS_SELECTOR, "a[data-hook='review-title']").text
                                # rating = review.find_element(By.CSS_SELECTOR, "i[data-hook='review-star-rating'] span").get_attribute("innerHTML")
                                body = (
                                    review.query_selector(
                                        "span[data-hook='review-body'] span"
                                    )
                                    .inner_text()
                                    .replace("\n", "")
                                    .replace("\u2018", "'")
                                    .replace("\u2019", "'")
                                    .strip()
                                )

                                data = {
                                    # "title": title,
                                    #     "rating": rating,
                                    "body": body
                                }

                                total.append(data)
                            except Exception:
                                continue
                        page.close()
                    else:
                        page.close()
                        break
        return total

    def save(self, results):
        with open(f"{self.asin}-reviews.json", "w") as f:
            json.dump(results, f)
        logger.info("Reviews saved in JSON File.")
