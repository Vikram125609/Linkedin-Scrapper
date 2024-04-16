# # from selenium import webdriver
# # from selenium.common.exceptions import WebDriverException
# # import time

# # driver = webdriver.Chrome()

# # while True:
# #     try:
# #         driver.get("https://www.linkedin.com/jobs/search/?f_TPR=r86400&geoId=102713980&keywords=Backend%20Developer&location=India&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true&original_referer=&position=1&pageNum=0")
# #         print('Page loaded successfully')
# #         time.sleep(100)
# #         break
# #     except WebDriverException:
# #         print("Page load failed. Retrying...")
# #         time.sleep(5)

# #         infinite-scroller__show-more-button


# from selenium import webdriver
# from selenium.common.exceptions import WebDriverException, NoSuchElementException
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome()

# while True:
#     try:
#         driver.get("https://www.linkedin.com/jobs/search/?f_TPR=r86400&geoId=102713980&keywords=Backend%20Developer&location=India&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true&original_referer=&position=1&pageNum=0")
#         print('Page loaded successfully')
#         while True:
#             try:
#                 for i in range(10):
#                     driver.execute_script("window.scrollBy(0, 100);")
#                     time.sleep(0.1)
#                 if (driver.find_element(By.CSS_SELECTOR, ".infinite-scroller__show-more-button")):
#                     print("Found 'Show more' button. Clicking...")
#                     show_more_button = driver.find_element(By.CSS_SELECTOR, ".infinite-scroller__show-more-button")
#                     show_more_button.click()
#                 else:
#                     time.sleep(5)
#             except NoSuchElementException:
#                 print("No more 'Show more' button found. End of page reached.")
#     except WebDriverException:
#         print("Page load failed. Retrying...")
#         time.sleep(5)


# from selenium import webdriver
# from selenium.common.exceptions import WebDriverException, NoSuchElementException
# from selenium.webdriver.common.by import By
# import time

# original_url = "https://www.linkedin.com/jobs/search/?f_TPR=r86400&geoId=102713980&keywords=Backend%20Developer&location=India&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true&original_referer=&position=1&pageNum=0"

# driver = webdriver.Chrome()

# while True:
#     try:
#         driver.get(original_url)
#         print('Page loaded successfully')
#         while True:
#             try:
#                 for i in range(10):
#                     driver.execute_script("window.scrollBy(0, 100);")
#                     time.sleep(0.1)
#                 if (driver.find_element(By.CSS_SELECTOR, ".infinite-scroller__show-more-button")):
#                     print("Found 'Show more' button. Clicking...")
#                     show_more_button = driver.find_element(By.CSS_SELECTOR, ".infinite-scroller__show-more-button")
#                     show_more_button.click()
#                 else:
#                     time.sleep(5)
#             except NoSuchElementException:
#                 print("No more 'Show more' button found. End of page reached.")
#             if driver.current_url != original_url:
#                 print("Redirect detected. Navigating back to original URL...")
#                 driver.get(original_url)

#     except WebDriverException:
#         print("Page load failed. Retrying...")
#         time.sleep(5)


# from selenium import webdriver
# from selenium.common.exceptions import WebDriverException, NoSuchElementException
# from selenium.webdriver.common.by import By
# import time
# import requests

# original_url = "https://www.linkedin.com/jobs/search/?f_TPR=r86400&geoId=102713980&keywords=Backend%20Developer&location=India&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true&original_referer=&position=1&pageNum=0"

# driver = webdriver.Chrome()

# while True:
#     try:
#         driver.get(original_url)
#         print('Page loaded successfully')
#         while True:
#             try:
#                 for i in range(10):
#                     driver.execute_script("window.scrollBy(0, 100);")
#                     time.sleep(0.1)
#                 if (driver.find_element(By.CSS_SELECTOR, ".infinite-scroller__show-more-button")):
#                     print("Found 'Show more' button. Clicking...")
#                     show_more_button = driver.find_element(By.CSS_SELECTOR, ".infinite-scroller__show-more-button")
#                     show_more_button.click()
#                 else:
#                     time.sleep(5)
#             except NoSuchElementException:
#                 print("No more 'Show more' button found. End of page reached.")
#             if driver.current_url != original_url:
#                 print("Redirect detected. Navigating back to original URL...")
#                 driver.get(original_url)

#     except WebDriverException:
#         print("Page load failed. Retrying...")
#         time.sleep(5)

#     except requests.HTTPError as e:
#         if e.response.status_code == 429:
#             print("Too many requests. Retrying...")
#             time.sleep(60)
#         else:
#             raise e


from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
import requests

companies = [
    {'name': 'Allegis Group', 'link': 'https://www.linkedin.com/jobs/search/?f_C=2153&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Randstad', 'link': 'https://www.linkedin.com/jobs/search/?f_C=2327&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Adecco', 'link': 'https://www.linkedin.com/jobs/search/?f_C=1104359&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Manpower', 'link': 'https://www.linkedin.com/jobs/search/?f_C=2312083&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Robert Half', 'link': 'https://www.linkedin.com/jobs/search/?f_C=1681&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true'},
]

window_height = 0
count = 0
reachedTillEnd = False

driver = webdriver.Chrome()


async def printLinks(driver, links):
    print(links)

while True:
    try:
        driver.get(original_url)
        while True:
            if driver.current_url != original_url:
                print("Redirect detected. Navigating back to original URL...")
                try:
                    driver.get(original_url)
                except requests.HTTPError as e:
                    print("First 429 error. Retrying...")
            try:
                for i in range(10):
                    driver.execute_script("window.scrollBy(0, 100);")
                    time.sleep(0.2)
                if (driver.find_element(By.CSS_SELECTOR, ".inline-notification__text")):
                    element = driver.find_element(By.CSS_SELECTOR, ".inline-notification__text")
                    if element.text == "You've viewed all jobs for this search":
                        print(
                            "No more 'Show more' button found. End of page reached.")
                        break
                if window_height != driver.execute_script("return window.innerHeight"):
                    window_height = driver.execute_script("return window.innerHeight")
                else:
                    count += 1
                    if count == 25:
                        links = driver.find_elements(
                            By.CSS_SELECTOR, ".base-card__full-link")
                        for link in links:
                            print(link.get_attribute("href"))
                        if (driver.find_element(By.CSS_SELECTOR, ".infinite-scroller__show-more-button")):
                            print("Found 'Show more' button. Clicking...")
                            element = driver.find_element(
                                By.CSS_SELECTOR, ".infinite-scroller__show-more-button")
                            if element:
                                element.click()
                            count = 0
                        else:
                            break

                # Check if the "Show more" button is visible in the viewport
                # show_more_button = driver.find_element(By.CSS_SELECTOR, ".infinite-scroller__show-more-button")
                # driver.execute_script("arguments[0].scrollIntoView();", show_more_button)
                # time.sleep(1)  # Wait for scroll animation to complete
                # button_location = show_more_button.location_once_scrolled_into_view
                # if button_location['y'] >= 0 and button_location['y'] <= driver.execute_script("return window.innerHeight"):
                #     print("Found 'Show more' button. Clicking...")
                #     show_more_button.click()
                # else:
                #     print("'Show more' button is not visible in the viewport. Skipping...")

            except NoSuchElementException:
                print("No Such Element Found")

    except requests.HTTPError as e:
        if e.response.status_code == 429:
            print("First 429 error. Retrying...")
        else:
            raise e

    except WebDriverException:
        print("Page load failed. Retrying...")

    if reachedTillEnd:
        print("Reached Till End. Breaking...")
