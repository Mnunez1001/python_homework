from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pandas as pd
import json

# Configuring Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")


# Starting the browser
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)


# Opening the Durham County Library search page
driver.get(
    "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
)


# Finding all search-result list items
books = driver.find_elements(
    By.CSS_SELECTOR,
    "li.cp-search-result-item"
)


# Printing how many results Selenium found
print(f"Number of books found: {len(books)}")

#empty list to hold book data
results = []

# Extracting and print each title, author(s), and format/year
for book in books:
    # Extracting the title
    title = book.find_element(
        By.CLASS_NAME,
        "title-content"
    ).text

    # Extracting the author(s)
    authors = book.find_elements(
        By.CLASS_NAME,
        "author-link"
    )

    author_names = [author.text for author in authors]
    author_text = "; ".join(author_names)

    # Finding the container that holds the format/year information
    format_container = book.find_element(
        By.CLASS_NAME,
        "manifestation-item-format-info-wrap"
    )

    # Finding the actual format/year text inside that container
    format_year = format_container.find_element(
        By.CLASS_NAME,
        "display-info-primary"
    ).text

    # Appending the book data to the results list
    results.append({
        "title": title,
        "authors": author_text,
        "format_year": format_year
    })


# Converting results into a Pandas DataFrame

books_df = pd.DataFrame(results)

print("\nScraped Book Data:")
print(books_df)

# Write the DataFrame to CSV
books_df.to_csv(
    "get_books.csv",
    index=False
)

# Write the results list to JSON

with open("get_books.json","w",encoding="utf-8") as json_file:
    json.dump(results,json_file,indent=4,ensure_ascii=False )


# Close the browser
driver.quit()


