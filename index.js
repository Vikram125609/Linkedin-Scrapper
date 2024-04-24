const { Builder, Browser, By } = require('selenium-webdriver');
const SBR_WEBDRIVER = '';

async function main() {
    console.log('Connecting to Scraping Browser...');
    const driver = await new Builder()
        .forBrowser(Browser.CHROME)
        .usingServer(SBR_WEBDRIVER)
        .build();
    try {
        console.log('Connected! Navigating to https://example.com...');
        await driver.get('https://www.linkedin.com/jobs/search/?f_C=2153&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&position=1&pageNum=0');
        const body = await driver.findElement(By.className('.base-card__full-link'));
        console.log(body); 
        const html = await driver.getPageSource();
    } finally {
        driver.quit();
    }
}

main().catch(err => {
    console.error(err.stack || err);
    process.exit(1);
});