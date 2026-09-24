FROM mcr.microsoft.com/playwright/python:v1.63.0-jammy

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "-v", "-s", \
     "--video=retain-on-failure", \
     "--screenshot=only-on-failure", \
     "--output=test-results", \
     "test_main.py"]