from playwright.sync_api import Playwright, sync_playwright, expect

FIELDS = [
    "Фамилия",
    "Имя",
    "Электронная почта",
    "Город",
    "Учебное заведение",
    "Специальность",
    "Факультет",
    "Дата рождения",
]


def check_field(page, name: str) -> None:
    label = page.get_by_text(f"{name}", exact=True).first
    label.scroll_into_view_if_needed()
    expect(label).to_be_visible()

    input_field = page.locator(f'xpath=//label[normalize-space()="{name}"]/following-sibling::input[1]').first
    expect(input_field).to_be_visible()

    label.click()

    expect(input_field).to_be_focused(timeout=2000) #при нажатии на label {name} кнопка не стала активной


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://career.t1.ru/debut")
    page.wait_for_load_state("networkidle")

    page.get_by_text("Отправить", exact=False).first.scroll_into_view_if_needed()

    for name in FIELDS:
        check_field(page, name)

    context.close()
    browser.close()

