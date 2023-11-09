from selenium import webdriver
from selenium.webdriver.edge.options import Options  # Make sure to import Edge Options
from selenium.webdriver.common.by import By  # Import By for selecting elements
import time

def setup_driver(download_path):
    options = Options()
    # options.use_chromium = True  # This line is optional and can be removed if causing issues
    options.add_experimental_option("prefs", {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,  # To disable the download prompt
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    driver = webdriver.Edge(options=options)  # Ensure the Edge driver executable is in your PATH or specify its path
    return driver

def download_with_selenium(driver, url, download_link_css_selector):
    driver.get(url)
    download_button = driver.find_element(By.CSS_SELECTOR, download_link_css_selector)  # Use the updated method
    download_button.click()
    # Wait for download to start (you'll need to tune this)
    time.sleep(10)

def main():
    url = 'https://download.cms.gov/nppes/NPI_Files.html'
    download_link_css_selector = '#DDSMTH\\.ZIP\\.D231009'  # Replace with the actual selector, escape the period
    download_path = r'C:\Users\sghal\Desktop\Download_NPI'  # Replace with your desired path

    driver = setup_driver(download_path)
    download_with_selenium(driver, url, download_link_css_selector)
    # Make sure to close the driver
    driver.quit()

if __name__ == "__main__":
    main()

