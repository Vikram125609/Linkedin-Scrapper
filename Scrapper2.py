import time
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote, ChromeOptions
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection

companies = [
  { "name": "TEKsystems","link": "https://www.linkedin.com/jobs/search/?f_C=2152&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Brilliant","link": "https://www.linkedin.com/jobs/search/?f_C=6634229&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Richard, Wayne & Roberts","link": "https://www.linkedin.com/jobs/search/?f_C=15842&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Global Employment Solutions","link": "https://www.linkedin.com/jobs/search/?f_C=13702&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Staffmark Holdings","link": "https://www.linkedin.com/jobs/search/?f_C=57195772&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "PEAK Technical Staffing USA","link": "https://www.linkedin.com/jobs/search/?f_C=165423&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "AccruePartners","link": "https://www.linkedin.com/jobs/search/?f_C=41754&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Bartech Group","link": "https://www.linkedin.com/jobs/search/?f_C=18596645&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Planet Pharma","link": "https://www.linkedin.com/jobs/search/?f_C=2474662&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "MATRIX Resources","link": "https://www.linkedin.com/jobs/search/?f_C=2875&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Boly Welch","link": "https://www.linkedin.com/jobs/search/?f_C=66812&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Kimco Staffing Services","link": "https://www.linkedin.com/jobs/search/?f_C=40757&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Abacus Group","link": "https://www.linkedin.com/jobs/search/?f_C=2079141&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Mechanics Hub","link": "https://www.linkedin.com/jobs/search/?f_C=446134&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Rx relief","link": "https://www.linkedin.com/jobs/search/?f_C=121817&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Sparks Group","link": "https://www.linkedin.com/jobs/search/?f_C=685741&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Ultimate Staffing Services","link": "https://www.linkedin.com/jobs/search/?f_C=60076700&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "WSI - Workforce Strategies","link": "https://www.linkedin.com/jobs/search/?f_C=211501&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "AtWork Group","link": "https://www.linkedin.com/jobs/search/?f_C=138649&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Frontline Source Group","link": "https://www.linkedin.com/jobs/search/?f_C=75103&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Software Specialists","link": "https://www.linkedin.com/jobs/search/?f_C=1504696&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Incendia Partners","link": "https://www.linkedin.com/jobs/search/?f_C=145218&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "LC Staffing","link": "https://www.linkedin.com/jobs/search/?f_C=222105&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "FutureStaff","link": "https://www.linkedin.com/jobs/search/?f_C=71320873&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "TriStarr","link": "https://www.linkedin.com/jobs/search/?f_C=267379&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Remedy Intelligent Staffing","link": "https://www.linkedin.com/jobs/search/?f_C=5324&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "MDI Group","link": "https://www.linkedin.com/jobs/search/?f_C=6652&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Parker + Lynch","link": "https://www.linkedin.com/jobs/search/?f_C=93516225&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Kinney Recruiting","link": "https://www.linkedin.com/jobs/search/?f_C=116796&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "The Execu | Search group","link": "https://www.linkedin.com/jobs/search/?f_C=26416&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Harvey Nash","link": "https://www.linkedin.com/jobs/search/?f_C=164131&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Healthcare IT Leaders","link": "https://www.linkedin.com/jobs/search/?f_C=1842435&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Reaction Search International","link": "https://www.linkedin.com/jobs/search/?f_C=444905&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Bradley-Morris","link": "https://www.linkedin.com/jobs/search/?f_C=6296078&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Michael Page International","link": "https://www.linkedin.com/jobs/search/?f_C=22056284&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Hire Counsel","link": "https://www.linkedin.com/jobs/search/?f_C=2086774&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Herk & Associates","link": "https://www.linkedin.com/jobs/search/?f_C=650050&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "RPC Company","link": "https://www.linkedin.com/jobs/search/?f_C=2359322&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Stratacuity","link": "https://www.linkedin.com/jobs/search/?f_C=155764&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Onward Search","link": "https://www.linkedin.com/jobs/search/?f_C=215561&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "American Recruiters","link": "https://www.linkedin.com/jobs/search/?f_C=162428&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Cameron Brooks","link": "https://www.linkedin.com/jobs/search/?f_C=243427&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "The Medicus Firm","link": "https://www.linkedin.com/jobs/search/?f_C=327770&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "VincentBenjamin","link": "https://www.linkedin.com/jobs/search/?f_C=62144545&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Special Counsel","link": "https://www.linkedin.com/jobs/search/?f_C=14353&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Green Key Resources","link": "https://www.linkedin.com/jobs/search/?f_C=90639&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Fast Switch","link": "https://www.linkedin.com/jobs/search/?f_C=58696&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Robert Hess Search Group","link": "https://www.linkedin.com/jobs/search/?f_C=228857&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "KNF&T Staffing Resources","link": "https://www.linkedin.com/jobs/search/?f_C=32876&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Global Recruiters Network","link": "https://www.linkedin.com/jobs/search/?f_C=13373&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
]

driver = webdriver.Chrome()

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