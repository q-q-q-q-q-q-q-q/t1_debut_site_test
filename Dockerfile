FROM ubuntu:latest
LABEL authors="Roman"
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


CMD ["pytest"]

ENTRYPOINT ["top", "-b"]