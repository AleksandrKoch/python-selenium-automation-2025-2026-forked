from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Target main page')
def open_target_main_page(context):
    context.app.main_page.open_main_page()



