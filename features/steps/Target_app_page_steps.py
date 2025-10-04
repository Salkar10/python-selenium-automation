
from behave import given, when, then
from time import sleep


@given('Open Target sign in page')
def open_target_sign_in_page(context):
    context.app.target_app_page.open_target_app()


@when('Store original window')
def store_window(context):
    context.original_window = context.app.page.get_original_window()
    print('Original window: ', context.original_window)


@when('Click Target terms and Conditions link')
def click_terms_conditions(context):
    context.app.target_app_page.click_terms_conditions_link()
    sleep(2)


@when('Switch to newly opened window')
def switch_window(context):
     current_windows = context.driver.window_handles
     print('Current windows after link click: ', current_windows) # [Win1, Win2...]
     new_window = current_windows[1]
     print('New window: ', new_window)
     context.driver.switch_to.window(new_window)
     context.app.page.switch_to_newly_opened_window([context.original_window])


@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.terms_conditions_page.verify_tc_opened()


@then('Close new window')
def close_page(context):
    context.app.page.close()

@then('Return to original window')
def switch_to_original_window(context):

    pass