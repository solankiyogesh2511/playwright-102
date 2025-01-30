import pytest
from playwright.sync_api import expect, sync_playwright
from helper.logger import LoggerHelper
import json
import os
import urllib
import subprocess
import re

capabilities = {
    'browserName': 'MicrosoftEdge',  # Browsers allowed: `Chrome`, `MicrosoftEdge`, `pw-chromium`, `pw-firefox` and `pw-webkit`
    'browserVersion': 'latest',
    'LT:Options': {
        'platform': os.environ.get("TARGET_OS"),
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
def test_Drag_And_Drop_Sliders(playwright):
    """
    Test to Drag & Drop Sliders on LambdaTest Playground.
    Steps:
    1. Open the https://www.lambdatest.com/selenium-playground page and click "Drag & Drop Sliders".
    2. Select the slider with the default value of 15 and drag the bar to make it 95, validating whether the range value shows 95.
    Args:
    page (playwright.sync_api.Page): The Playwright page object used to interact with the web page.
    Validations:
    - The visibility of the "Drag & Drop Sliders" link.
    - The current value of the slider before and after dragging.
    - The final value of the slider is 95.
    """
    
    playwrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]
    capabilities['LT:Options']['playwrightClientVersion'] = playwrightVersion

    lt_cdp_url = f"wss://cdp.lambdatest.com/playwright?capabilities={urllib.parse.quote(json.dumps(capabilities))}"
    browser = playwright.chromium.connect(lt_cdp_url, timeout=120000)
    page = browser.new_page()
    
    
    #1) Open the https://www.lambdatest.com/selenium-playground page and click“Drag & Drop Sliders”
    LoggerHelper.log_info("Test to Drag & Drop Sliders on LambdaTest Playground")
    page.goto("https://www.lambdatest.com/selenium-playground/")
    LoggerHelper.log_info("Opened the https://www.lambdatest.com/selenium-playground page")
    expect(page.get_by_role("link", name="Drag & Drop Sliders")).to_be_visible()
    LoggerHelper.log_info("Validated the visibility of the Drag & Drop Sliders link")
    page.get_by_role("link", name="Drag & Drop Sliders").click()
    LoggerHelper.log_info("Clicked on the Drag & Drop Sliders link")
    
    #2) Select the slider “Default value 15” and drag the bar to make it 95 by validating whether the range value shows 95.
    slider = page.locator("#slider3").get_by_role("slider")
    LoggerHelper.log_info("Selected the slider 'Default value 15'")
    current_value = int(slider.input_value())
    LoggerHelper.log_info(f"Current value of the slider: {current_value}")
    target_value = 95
    LoggerHelper.log_info(f"Target value of the slider: {target_value}")

    clickOnSlider(slider, current_value, target_value)

    # Verify the final value
    page.get_by_text(str(target_value)).click()
    LoggerHelper.log_info(f"Clicked on the slider value: {target_value}")

    print(f"Slider reached the target value: {target_value}")
    expect(slider).to_have_value(str(target_value))
    LoggerHelper.log_info(f"Validated the slider value: {target_value}")
    
    page.close()
    browser.close()
    
@staticmethod
def clickOnSlider(slider, current_value, target_value):
    # Increment the slider until it reaches the target value
    while current_value < target_value:
        slider.fill(str(current_value + 1))
        LoggerHelper.log_info(f"Updated the slider value to: {current_value + 1}")
        current_value = int(slider.input_value())  # Update the current value
        LoggerHelper.log_info(f"Slider value updated to: {current_value}")
        print(f"Slider value updated to: {current_value}")
        
with sync_playwright() as playwright:
            test_Drag_And_Drop_Sliders(playwright)