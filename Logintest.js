const { chromium } = require('playwright');


(async () => {
  const browser = await chromium.launch({
    headless: false,
   
  });
  const context = await browser.newContext();

  // Open new page
  const page = await context.newPage();

  // Go to http://eaapp.somee.com/
  await page.goto('https://customer-ui-hub-dummy-plt-qa.conduent-cap.com/login',({waitUntil: 'networkidle' }));
  await page.setDefaultNavigationTimeout(50000);
 
   await page.fill('//input[@type="email"]',"captestuser011@gmail.com");
   await page.fill('//input[@type="password"]',"Conduent@1");
     await page.click("//button[@type='submit']")
     await page.waitForSelector("//div[@class='menu-btn__burger']")
     await page.click("//div[@class='menu-btn__burger']")
     await page.waitForSelector("//span[contains(text(),'Production Control')]")
     await page.click("//span[contains(text(),'Production Control')]")
     await page.click("//span[@class='user-avatar']");
     await page.waitForTimeout(3000)


     await page.waitForSelector("//span[contains(text(),'Logout')]")
     await page.click("//span[contains(text(),'Logout')]");
})();