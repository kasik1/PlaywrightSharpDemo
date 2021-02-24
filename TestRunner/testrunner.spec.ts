import {it,describe,expect} from "@playwright/test"


describe("Run basic E2E EA App site test", async () => {

    it("Navigate and Login EA App site", async ({ context }) => {

       
      var page = await context.newPage();
    
      await page.goto('https://customer-ui-hub-dummy-plt-qa.conduent-cap.com/login', {waitUntil: 'networkidle'});
    await page.setDefaultNavigationTimeout(50000);
    
      
      //input[@type="email"]
      await page.fill('//input[@type="email"]',"captestuser011@gmail.com");
      await page.fill('//input[@type="password"]',"Conduent@1");
       // Click button[aria-label="Log In"]
       await Promise.all([
        page.waitForNavigation(/*{ url: 'https://customer-ui-hub-dummy-plt-qa.conduent-cap.com/dashboard' }*/),
        page.click('button[aria-label="Log In"]')
      ]);
    
      await page.click("//div[@class='menu-btn__burger']")
      await page.waitForSelector("//span[contains(text(),'Production Control')]")
      await page.click("//span[contains(text(),'Production Control')]")
      await page.click("//span[@class='user-avatar']");
      await page.waitForTimeout(3000)


      await page.waitForSelector("//span[contains(text(),'Logout')]")
      await page.click("//span[contains(text(),'Logout')]");
      
    
    });

    

});