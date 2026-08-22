from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pandas as pd

# Configuring Selenium

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)

# Opening the OWASP Top 10 page

url = "https://owasp.org/Top10/2025/#top-102025-list"

driver.get(url)

# Finding the Top 10 vulnerability links

vulnerability_elements = driver.find_elements(
    By.XPATH,
    "//h3[@id='top-102025-list']/following-sibling::ol[1]/li/a"
)


print(f"Number of vulnerabilities found: {len(vulnerability_elements)}")

# Extracting title and link

results = []

for element in vulnerability_elements:

    title = element.text
    link = element.get_attribute("href")

    vulnerability = {
        "Title": title,
        "Link": link
    }

    results.append(vulnerability)


# Printing results

print("\nOWASP Top 10 Vulnerabilities:")

for vulnerability in results:
    print(vulnerability)

# Converting to DataFrame

owasp_df = pd.DataFrame(results)

print("\nOWASP Top 10 DataFrame:")
print(owasp_df)


# Writing results to CSV

owasp_df.to_csv(
    "owasp_top_10.csv",
    index=False
)

# Closing browser

driver.quit()
