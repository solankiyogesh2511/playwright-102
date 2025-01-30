import pytest
from playwright.sync_api import expect, sync_playwright
from helper.logger import LoggerHelper
import json
import os
import urllib
import subprocess
import re

capabilities = {
    'browserName': 'pw-webkit',  # Browsers allowed: `Chrome`, `MicrosoftEdge`, `pw-chromium`, `pw-firefox` and `pw-webkit`
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

def test_simple_form_demo(playwright):
    """
    Test to validate interaction with Simple Form Demo on LambdaTest Playground.
    Steps:
    1. Open LambdaTest’s Selenium Playground.
    2. Click on "Simple Form Demo" link.
    3. Validate that the URL contains "simple-form-demo".
    4. Create a variable for a string value (e.g., "Welcome to LambdaTest").
    5. Enter the variable value in the "Enter Message" text box.
    6. Click on "Get Checked Value" button.
    7. Validate that the same text message is displayed in the right-hand panel under the "Your Message:" section.
    Args:
        page: The Playwright page object used to interact with the browser.
    """
    playwrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]
    capabilities['LT:Options']['playwrightClientVersion'] = playwrightVersion

    lt_cdp_url = f"wss://cdp.lambdatest.com/playwright?capabilities={urllib.parse.quote(json.dumps(capabilities))}"
    browser = playwright.chromium.connect(lt_cdp_url, timeout=120000)
    page = browser.new_page()
    
    #1) Open LambdaTest’s Selenium Playground from
    LoggerHelper.log_info("Test to validate interaction with Simple Form Demo on LambdaTest Playground.")
    page.goto("https://www.lambdatest.com/selenium-playground/")
    LoggerHelper.log_info("Opened the https://www.lambdatest.com/selenium-playground page")
    
    #2)  Click“Simple Form Demo”
    page.get_by_role("link", name="Simple Form Demo").click()
    LoggerHelper.log_info("Clicked on the Simple Form Demo link")
    
    #3) Validate that the URL contains “simple-form-demo”
    page.wait_for_url(re.compile(".*simple-form-demo.*"))   
    expect(page).to_have_url(re.compile(".*simple-form-demo.*"))
    LoggerHelper.log_info("Validated that the URL contains 'simple-form-demo'")
    
    #4) Create a variable for a string value e.g.: “Welcome to LambdaTest”
    message = "Welcome to LambdaTest"
    
    #5) Use this variable to enter values in the “Enter Message” text box.
    page.get_by_placeholder("Please enter your Message").fill(message)
    LoggerHelper.log_info(f"Entered the message: {message}")
    
    #6)Click“Get Checked Value”
    page.get_by_role("button", name="Get Checked Value").click()
    LoggerHelper.log_info("Clicked on the Get Checked Value button")
    
    #7) Validate whether the same text message is displayed in the right-hand panel under the “Your Message:” section.
    expect(page.get_by_text(message)).to_be_visible()
    LoggerHelper.log_info(f"Validated the message '{message}' in the Your Message section") 
    
    page.close()
    browser.close()
    
with sync_playwright() as playwright:
            test_simple_form_demo(playwright) 
