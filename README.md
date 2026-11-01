
Автотест, воспроизводящий баг на странице [career.t1.ru/debut](https://career.t1.ru/debut): при клике по тексту (label) поле ввода не получает фокус. Оформлен как воспроизводимый баг-репорт с Playwright + Pytest + Allure, упакован в Docker.

[![Docker Pulls](https://img.shields.io/docker/pulls/spiddi/t1-debut-tests)](https://hub.docker.com/r/spiddi/t1-debut-tests)
[![Python](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/playwright-1.63-green)](https://playwright.dev/)
[![Allure](https://img.shields.io/badge/allure-pytest-orange)](https://allurereport.org/)


| | |
|---|---|
| **Заголовок** | В разделе с заявкой на рассылку о наборах на стажировку не открываются формы с вводом текста |
| **URL** | https://career.t1.ru/debut |
| **Приоритет** | `P2` |
| **Статус** | `New` _(хотя вряд ли это не заметили)_ |
| **Окружение** | Opera GX `134.0.5954.67` · Windows 10 64-bit · Chromium `150.0.7871.187` · 1920×1080, 15.6", fullscreen |
| **Вложение** | 🎥 [Видео бага](https://vkvideo.ru/video-240173600_456239018?list=ln-gT23VJrRYBqNs9wOjo) |

### Шаги воспроизведения
1. Пролистать до поля «Фамилия» (или любого другого поля с вводом текста).
2. Кликнуть по тексту (label) «Фамилия» (или по label любого другого поля).

### Ожидаемый результат
Поле ввода становится активным (получает фокус).

### Фактический результат
Поле ввода становится активным **только если кликнуть сбоку от текста** — клик по самому `<label>` фокус не передаёт.

---

## Как запустить?

```bash
docker run --rm -it spiddi/t1-debut-tests
