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
    #    если смотреть через пайчарм - хватит этого
    #    browser = playwright.chromium.launch(headless=False,)
    #    context = browser.new_context()
    #
    #    за все что ниже - извините, очень хотелось в докер красивенько все залить
    browser = playwright.chromium.launch(
        headless=True,
        args=[
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
            "--disable-dev-shm-usage",
        ],
    )

    context = browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        locale="ru-RU",
        timezone_id="Europe/Moscow",
        viewport={"width": 1920, "height": 1080},
    )

    context.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
        Object.defineProperty(navigator, 'languages', { get: () => ['ru-RU', 'ru', 'en-US'] });
        Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5] });
        window.chrome = { runtime: {} };
    """)



    page = context.new_page()

    page.goto("https://career.t1.ru/debut")
    page.wait_for_load_state("networkidle")

    page.get_by_text("Отправить", exact=False).first.scroll_into_view_if_needed()

    for name in FIELDS:
        check_field(page, name)

    context.close()
    browser.close()

