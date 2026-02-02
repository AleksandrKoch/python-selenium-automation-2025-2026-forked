from behave import when, then


@when("User clicks Account button")
def click_account_button(context):
    context.app.header.click_account()


@when("Account menu is opened")
def verify_account_menu_opened(context):
    context.app.account_menu.wait_until_opened()


@then("User clicks Sign in button")
def click_sign_in_button(context):
    context.app.account_menu.click_sign_in()


@then("Sign in page opened")
def verify_sign_in_page_opened(context):
    context.app.sign_in_page.verify_opened()
