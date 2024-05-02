import time
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote, ChromeOptions
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection

companies = [
  { "name": "CSI Executive Search","link": "https://www.linkedin.com/jobs/search/?f_C=500554&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "ABA Search","link": "https://www.linkedin.com/jobs/search/?f_C=2560259&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Creative Financial Staffing","link": "https://www.linkedin.com/jobs/search/?f_C=248184&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Prestige Staffing","link": "https://www.linkedin.com/jobs/search/?f_C=19256&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Solomon Page Group","link": "https://www.linkedin.com/jobs/search/?f_C=58329238&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Kelly Services","link": "https://www.linkedin.com/jobs/search/?f_C=2307&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Creative Circle","link": "https://www.linkedin.com/jobs/search/?f_C=163253&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "TeamBradley","link": "https://www.linkedin.com/jobs/search/?f_C=1636943&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "elite personnel","link": "https://www.linkedin.com/jobs/search/?f_C=18863351&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Snelling","link": "https://www.linkedin.com/jobs/search/?f_C=166021&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "HR Answers","link": "https://www.linkedin.com/jobs/search/?f_C=102499&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Mitchell Martin","link": "https://www.linkedin.com/jobs/search/?f_C=488281&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Contemporary Staffing Solutions","link": "https://www.linkedin.com/jobs/search/?f_C=33218&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Infinity Consulting Solutions","link": "https://www.linkedin.com/jobs/search/?f_C=91692689&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Govig & Associates","link": "https://www.linkedin.com/jobs/search/?f_C=27605&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Gainor Staffing","link": "https://www.linkedin.com/jobs/search/?f_C=233922&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "FPC National","link": "https://www.linkedin.com/jobs/search/?f_C=100753&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "CliftonLarsonAllen","link": "https://www.linkedin.com/jobs/search/?f_C=2437248&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Sterling Engineering","link": "https://www.linkedin.com/jobs/search/?f_C=24211&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "AppleOne","link": "https://www.linkedin.com/jobs/search/?f_C=6088&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Access Staffing","link": "https://www.linkedin.com/jobs/search/?f_C=22219&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "MedicalSolutions","link": "https://www.linkedin.com/jobs/search/?f_C=839245&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Adams & Martin Group","link": "https://www.linkedin.com/jobs/search/?f_C=31439&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Gotham Technology Group","link": "https://www.linkedin.com/jobs/search/?f_C=21485&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Heitmeyer Consulting","link": "https://www.linkedin.com/jobs/search/?f_C=5221388&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Human Edge","link": "https://www.linkedin.com/jobs/search/?f_C=15160097&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "TriCom Technical Services","link": "https://www.linkedin.com/jobs/search/?f_C=43470&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Russ Hadick & Associates","link": "https://www.linkedin.com/jobs/search/?f_C=375118&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Kent Daniels & Associates","link": "https://www.linkedin.com/jobs/search/?f_C=856947&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Talon","link": "https://www.linkedin.com/jobs/search/?f_C=10393857&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Prolink Staffing","link": "https://www.linkedin.com/jobs/search/?f_C=1667385&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "AP Professionals","link": "https://www.linkedin.com/jobs/search/?f_C=570739&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "The Bachrach Group","link": "https://www.linkedin.com/jobs/search/?f_C=38117&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "CPS","link": "https://www.linkedin.com/jobs/search/?f_C=427392&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "WorldBridge Partners","link": "https://www.linkedin.com/jobs/search/?f_C=19902&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Whitridge Associates","link": "https://www.linkedin.com/jobs/search/?f_C=41509&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Thompson Technologies","link": "https://www.linkedin.com/jobs/search/?f_C=21537&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Inceed","link": "https://www.linkedin.com/jobs/search/?f_C=40783&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "The Bowdoin Group","link": "https://www.linkedin.com/jobs/search/?f_C=208135&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "West Coast Careers","link": "https://www.linkedin.com/jobs/search/?f_C=96577&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Verigent","link": "https://www.linkedin.com/jobs/search/?f_C=127588&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Innovative Career Resources","link": "https://www.linkedin.com/jobs/search/?f_C=3524132&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Kineticom","link": "https://www.linkedin.com/jobs/search/?f_C=21033&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "In-Flight Crew Connections","link": "https://www.linkedin.com/jobs/search/?f_C=693360&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "IT Works Recruitment","link": "https://www.linkedin.com/jobs/search/?f_C=132938&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Preferred Healthcare Staffing","link": "https://www.linkedin.com/jobs/search/?f_C=896883&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Insight Recruiting","link": "https://www.linkedin.com/jobs/search/?f_C=510951&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "4 Corner Resources","link": "https://www.linkedin.com/jobs/search/?f_C=685780&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "SyllogisTeks","link": "https://www.linkedin.com/jobs/search/?f_C=32563&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "LRS Consulting Services","link": "https://www.linkedin.com/jobs/search/?f_C=94197416&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
  { "name": "Staff Smart","link": "https://www.linkedin.com/jobs/search/?f_C=381097&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0" },
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