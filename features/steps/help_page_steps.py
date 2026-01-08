from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

QUESTION_HEADER = (By.XPATH, "//h2[normalize-space(text())='Have a question?']")
QUESTION_SUBHEADER = (By.XPATH, "//p[normalize-space(text())='We will help you find answers.']")
HELP_BUTTON = (By.XPATH, "//button[normalize-space()='Browse all help']")
SEARCH_BAR = (By.ID, "helpSearch")
SEARCH_BUTTON = (By.CSS_SELECTOR, "button[class*='styles_bare']")
HELP_HEADING = (By.XPATH, "//h2[normalize-space()='What would you like help with?']")
CARD_LIST = (By.CSS_SELECTOR, "div[class*='NavCard_navCardWrapper'] a")
POPULAR_PAGES_WRAPPER = (By.CSS_SELECTOR, "div[class*='LinkCard_contentCard']")
POPULAR_PAGES_HEADER = (By.CSS_SELECTOR, "div[class*='LinkCard_titleCard']")


@given('Open Target Help page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/help')
    sleep(1)


@then('Verify main header is shown')
def verify_main_header(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == 'Help', \
        "h1 does not show Help copy"

@then('Verify elements shown in Search section') # 5 elements here to verify
def verify_search_section(context):
    assert len(context.driver.find_elements(*QUESTION_HEADER)) == 1, \
        "'Have a question?' not found"
    assert len(context.driver.find_elements(*QUESTION_SUBHEADER)) == 1, \
        "'We will help you find answers.' not found"
    assert len(context.driver.find_elements(*HELP_BUTTON)) == 1, \
        "'Browse all help' not found"
    assert len(context.driver.find_elements(*SEARCH_BAR)) == 1, \
        "'Help search' not found"
    assert len(context.driver.find_elements(*SEARCH_BUTTON)) == 1, \
        "Search button not found"


@then('Verify What would you like help with heading is present')
def verify_search_heading(context):
    assert len(context.driver.find_elements(*HELP_HEADING)) == 1, \
        "Help heading not found"


@then('Verify list of {number_of_cards} cards is present')
def verify_list_cards(context, number_of_cards):
    number_of_cards = int(number_of_cards)
    assert len(context.driver.find_elements(*CARD_LIST)) == number_of_cards, \
        "'Number of cards' list does not match"


@then('Verify Popular pages header is present')
def verify_popular_pages_header(context):
    assert len(context.driver.find_elements(*POPULAR_PAGES_HEADER)), \
        "'Popular pages' header not present"


@then('Verify Popular pages container is present')
def verify_link_card_container(context):
    assert len(context.driver.find_elements(*POPULAR_PAGES_WRAPPER)) == 1, \
        "'Popular pages' container not present"