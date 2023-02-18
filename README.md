# 🕷️ Amazon-Scraper-CLI 🕷️

A Python CLI program for scraping reviews from Amazon product pages.. Without headaches.

## Overview

The Amazon Reviews Scraper program allows users to retrieve reviews from Amazon product pages and export them to a JSON file. The program uses the Playwright library to extract the review data from the HTML source code of the product page.

## Features

- Scrape Reviews from Amazon product pages
- Export to JSON
- CLI Interface for easy usage

## Installation

1. Clone the repository

```bash
$ git clone 
```

2. Install requirements with Poetry

```bash
$ poetry install
```

## Usage

The programm can be used from the command line by running the `scrape.py` script. You only have to provide the ASIN from the Amazon Product. 

Example Usage:

```bash
$ poetry run python scrape.py B07RKZFD5Z
```

## Enhancements

- Export to CSV
- Filter by Rating, Date
- Sort by Date, Relevance
