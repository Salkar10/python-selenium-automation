from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


#COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")
#SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")
COLOR_OPTIONS = (By.CSS_SELECTOR, '[class="styles_fadeInPicture__X_1Zl styles_animated__7ypei styles_fullWidth__z04mu styles_fullHeight__xxwBI"]')
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")

@given('Open target product A-77568636 page')
def open_target(context):
   #context.driver.get(f'https://www.target.com/p/wranglers-men-39-s-relaxed-fit-straight-jeans/-/A-91269718?preselect=90919011#lnk=sametab')
   context.driver.get(f'https://www.target.com/p/levi-s-men-s-505-regular-fit-straight-jeans/-/A-77568636?preselect=81782319#lnk=sametab')
   sleep(5)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Dark Wash', 'Tan']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2]
    print(colors)

    for c in colors:
        c.click()
        sleep(0.5)

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
