#!/usr/bin/env python3
import csv
import requests
from bs4 import BeautifulSoup


def scrape_sa_news():
    url = "https://www.sanews.gov.za/south-africa"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0.0.0 Safari/537.36"
        )
    }

    print(f"Fetching local news from {url}...")
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(
            f"Failed to retrieve page. Status code: {response.status_code}"
        )
        return

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("div", class_="views-row")

    scraped_data = []

    for article in articles:
        title_tag = article.find(
            ["h2", "h3", "span"], class_="field-content"
        )
        link_tag = article.find("a")

        if title_tag and link_tag:
            title = title_tag.get_text(strip=True)
            link = "https://www.sanews.gov.za" + link_tag.get("href", "")
            scraped_data.append({"Title": title, "URL": link})

    print(
        f"Successfully scraped {len(scraped_data)} local news headlines.\n"
    )

    for i, item in enumerate(scraped_data[:10], 1):
        print(f"{i}. {item['Title']}\n   Link: {item['URL']}\n")

    with open("local_sa_news.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Title", "URL"])
        writer.writeheader()
        writer.writerows(scraped_data)

    print("Data successfully saved to 'local_sa_news.csv'.")


if __name__ == "__main__":
    scrape_sa_news()