import pytest
from playwright.sync_api import expect, sync_playwright
from helper.logger import LoggerHelper
import json
import os
import urllib
import subprocess
import re
    
capabilities = {
    'browserName': 'Chrome',  # Browsers allowed: `Chrome`, `MicrosoftEdge`, `pw-chromium`, `pw-firefox` and `pw-webkit`
    'browserVersion': 'latest',
    'LT:Options': {
        'platform': 'Windows 10',
        'build': 'Playwright Python Build',
        'name': 'Playwright Test',
        'user': os.getenv('LT_USERNAME'),
        'accessKey': os.getenv('LT_ACCESS_KEY'),
        'network': True,
        'video': True,
        'console': True,
        'tunnel': False,  # Add tunnel configuration if testing locally hosted webpage
        'tunnelName': '',  # Optional
        'geoLocation': '', # country code can be fetched from https://www.lambdatest.com/capabilities-generator/
    }
}
    
def test_Input_Form_Submit(playwright):
    """
    Test to validate Input Form Submit on LambdaTest Playground.
    Steps:
    1. Open the https://www.lambdatest.com/selenium-playground page and click "Input Form Submit".
    2. Click "Submit" without filling in any information in the form.
    3. Assert "Please fill in the fields" error message.
    4. Fill in Name, Email, and other fields.
    5. From the Country drop-down, select "United States" using the text property.
    6. Fill in all fields and click "Submit".
    7. Once submitted, validate the success message "Thanks for contacting us, we will get back to you shortly." on the screen.
    """
    # Initialize page object
    playwrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]
    capabilities['LT:Options']['playwrightClientVersion'] = playwrightVersion

    lt_cdp_url = f"wss://cdp.lambdatest.com/playwright?capabilities={urllib.parse.quote(json.dumps(capabilities))}"
    browser = playwright.chromium.connect(lt_cdp_url, timeout=120000)
    page = browser.new_page()
    
    #1) Open the https://www.lambdatest.com/selenium-playground page and click“Input Form Submit”
    LoggerHelper.log_info("Test to validate Input Form Submit on LambdaTest Playground")
    page.goto("https://www.lambdatest.com/selenium-playground/")
    LoggerHelper.log_info("Opened the https://www.lambdatest.com/selenium-playground page")
    page.get_by_role("link", name="Input Form Submit").click()
    LoggerHelper.log_info("Clicked on the Input Form Submit link")
    
    #2) Click“Submit” without filling in any information in the form.
    page.get_by_role("button", name="Submit").click()
    LoggerHelper.log_info("Clicked on the Submit button")
    
    #3) Assert “Please fill in the fields” error message.
    page.locator('input#name[required]').is_visible()
    expect(page.locator('input#name[required]')).to_have_js_property('validationMessage', 'Please fill out this field.')
    LoggerHelper.log_info("Validated the error message 'Please fill out this field.'")

    #4) Fill in Name, Email, and other fields.
    page.get_by_placeholder("Name", exact=True).fill("Rob")
    LoggerHelper.log_info("Filled in the Name field")
    page.get_by_placeholder("Email", exact=True).fill("rob@mailinator.com")
    LoggerHelper.log_info("Filled in the Email field")
    page.get_by_placeholder("Password").fill("Rob@123")
    LoggerHelper.log_info("Filled in the Password field")
    page.get_by_placeholder("Company").fill("Testing")
    LoggerHelper.log_info("Filled in the Company field")
    page.get_by_placeholder("Website").fill("www.test.com")
    LoggerHelper.log_info("Filled in the Website field")
    
    #5) From the Country drop-down, select “United States” using the text property.
    page.get_by_role("combobox").select_option("United States")
    LoggerHelper.log_info("Selected 'United States' from the Country drop-down")
    page.get_by_placeholder("City").fill("Jersey City")
    LoggerHelper.log_info("Filled in the City field")
    page.get_by_placeholder("Address 1").fill("ABC")
    LoggerHelper.log_info("Filled in the Address 1 field")
    page.get_by_placeholder("Address 2").fill("DEF")
    LoggerHelper.log_info("Filled in the Address 2 field")
    page.get_by_placeholder("State").fill("New Jersey")
    LoggerHelper.log_info("Filled in the State field")
    page.get_by_placeholder("Zip code").fill("07302")
    LoggerHelper.log_info("Filled in the Zip code field")
    
    #6) Fill in all fields and click “Submit”
    page.get_by_role("button", name="Submit").click()
    LoggerHelper.log_info("Clicked on the Submit button")
    
    #7) Once submitted, validate the success message “Thanks for contact, we will get back to you shortly." on the screen.
    page.wait_for_selector('text="Thanks for contacting us, we will get back to you shortly."')
    expect(page.locator('text="Thanks for contacting us, we will get back to you shortly."')).to_be_visible()
    LoggerHelper.log_info("Validated the success message 'Thanks for contacting us, we will get back to you shortly.'")  
    
    page.close()
    browser.close()
    
with sync_playwright() as playwright:
        test_Input_Form_Submit(playwright)
