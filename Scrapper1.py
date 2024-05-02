from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection

import time
import json
import requests

# SBR_WEBDRIVER = 'https://brd-customer-hl_d791b343-zone-c2c_linkedin_scraper:q6z3dfujuzo6@brd.superproxy.io:9515'

companies = [
    {'name': 'Apex Systems','link': 'https://www.linkedin.com/jobs/search/?f_C=4787&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Insight Global','link': 'https://www.linkedin.com/jobs/search/?f_C=11056&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Allegis Group','link': 'https://www.linkedin.com/jobs/search/?f_C=2153&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'ResourceMFG','link': 'https://www.linkedin.com/jobs/search/?f_C=841184&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'PDS Tech','link': 'https://www.linkedin.com/jobs/search/?f_C=7161&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Synergy Staffing','link': 'https://www.linkedin.com/jobs/search/?f_C=795177&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'TRC Staffing Services','link': 'https://www.linkedin.com/jobs/search/?f_C=7886&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'PrideStaff','link': 'https://www.linkedin.com/jobs/search/?f_C=17987&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Experis','link': 'https://www.linkedin.com/jobs/search/?f_C=2203697&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Robert Half','link': 'https://www.linkedin.com/jobs/search/?f_C=1681&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Aeropres','link': 'https://www.linkedin.com/jobs/search/?f_C=4242524&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'BelFlex Staffing Network','link': 'https://www.linkedin.com/jobs/search/?f_C=3571908&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Adecco','link': 'https://www.linkedin.com/jobs/search/?f_C=1104359&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Solomon Page','link': 'https://www.linkedin.com/jobs/search/?f_C=14352&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Genuent','link': 'https://www.linkedin.com/jobs/search/?f_C=61577701&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Aston Carter','link': 'https://www.linkedin.com/jobs/search/?f_C=13153&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Pro Staff','link': 'https://www.linkedin.com/jobs/search/?f_C=6636&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'TEKsystems Global Services','link': 'https://www.linkedin.com/jobs/search/?f_C=80818388&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Ajilon','link': 'https://www.linkedin.com/jobs/search/?f_C=24875&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'SNI Companies','link': 'https://www.linkedin.com/jobs/search/?f_C=971273&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Synergis','link': 'https://www.linkedin.com/jobs/search/?f_C=260295&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Addison Group','link': 'https://www.linkedin.com/jobs/search/?f_C=18043&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Brooksource','link': 'https://www.linkedin.com/jobs/search/?f_C=18476&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'The Select Group','link': 'https://www.linkedin.com/jobs/search/?f_C=28526&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Accountemps','link': 'https://www.linkedin.com/jobs/search/?f_C=40762747&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'RemX','link': 'https://www.linkedin.com/jobs/search/?f_C=2471868&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Diversant','link': 'https://www.linkedin.com/jobs/search/?f_C=918331&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Ettain Group','link': 'https://www.linkedin.com/jobs/search/?f_C=12773&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Beacon Hill Staffing Group','link': 'https://www.linkedin.com/jobs/search/?f_C=22456&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Manpower','link': 'https://www.linkedin.com/jobs/search/?f_C=2312083&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Randstad','link': 'https://www.linkedin.com/jobs/search/?f_C=2327&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'TEKsystems Global Services','link': 'https://www.linkedin.com/jobs/search/?f_C=80818388&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Hays','link': 'https://www.linkedin.com/jobs/search/?f_C=3486&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Kforce','link': 'https://www.linkedin.com/jobs/search/?f_C=3076&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Volt','link': 'https://www.linkedin.com/jobs/search/?f_C=19071211&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Spherion','link': 'https://www.linkedin.com/jobs/search/?f_C=2266&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'DISYS','link': 'https://www.linkedin.com/jobs/search/?f_C=15228&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Express Employment Professionals','link': 'https://www.linkedin.com/jobs/search/?f_C=1907001&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Collabera','link': 'https://www.linkedin.com/jobs/search/?f_C=24440&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Vaco','link': 'https://www.linkedin.com/jobs/search/?f_C=11229&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Modis','link': 'https://www.linkedin.com/jobs/search/?f_C=224006&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Signature Consultants','link': 'https://www.linkedin.com/jobs/search/?f_C=9687&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Aerotek','link': 'https://www.linkedin.com/jobs/search/?f_C=2889&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Yoh','link': 'https://www.linkedin.com/jobs/search/?f_C=6044&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'Lucas Group','link': 'https://www.linkedin.com/jobs/search/?f_C=6488&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'CyberCoders','link': 'https://www.linkedin.com/jobs/search/?f_C=21836&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
    {'name': 'On Assignment','link': 'https://www.linkedin.com/jobs/search/?f_C=8720&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0'},
]

driver = webdriver.Chrome()

# sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')  
#     with Remote(sbr_connection, options=ChromeOptions()) as driver:  
#         print('Connected! Navigating...')  


def sendData(company_name, links):
    urls = []
    for link in links:
        urls.append(link.get_attribute('href'))

    url = "https://c2cjobs.org/api/v1/general/linkedInJobs"

    payload = json.dumps({
        "company_name": company_name,
        "urls": urls
    })
    print(company_name,len(urls))

    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code == 200:
            print('Data sent successfully to c2cjobs.org API')
        else:
            print('Failed to send data to c2cjobs.org API. Status code:',
                  response.status_code)
    except requests.RequestException as e:
        print('An error occurred while sending data to c2cjobs.org API:', e)

def getData(company_name, original_url):
    count = 0
    window_height = 0
    reachedTillEnd = False
    # sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')  
    # with Remote(sbr_connection, options=ChromeOptions()) as driver:  
    #     print('Connected! Navigating...')  
    while True:
        try:
            driver.get(original_url)
            print('Page loaded successfully')
            while True:
                if driver.current_url != original_url:
                    print('Redirect detected. Navigating back to original URL...')
                    try:
                        driver.get(original_url)
                    except requests.HTTPError as e:
                        driver.get(original_url)
                try:
                    for i in range(20):
                        driver.execute_script('window.scrollBy(0, 100);')
                        time.sleep(0.2)
                    print(count)
                    if window_height != driver.execute_script('return window.innerHeight'):
                        window_height = driver.execute_script(
                            'return window.innerHeight')
                    else:
                        count += 1
                        if count == 25:
                            links = driver.find_elements(
                                By.CSS_SELECTOR, '.base-card__full-link')
                            sendData(company_name, links)
                            reachedTillEnd = True
                            break
                except NoSuchElementException:
                    print('No Such Element Found')
        except requests.HTTPError as e:
            if e.response.status_code == 429:
                driver.get(original_url)
            else:
                driver.get(original_url)
        except WebDriverException:
            print('Page load failed. Retrying...')
        if reachedTillEnd:
            return


while True:
    for company in companies:
        original_url = company['link']
        company_name = company['name']
        getData(company_name, original_url)
        print('Done for ' + company['name'])