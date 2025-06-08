FROM python:3.13-slim

WORKDIR /taf

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget gnupg curl unzip \
        fonts-liberation libu2f-udev libvulkan1 \
        && rm -rf /var/lib/apt/lists/*

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" \
        > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -q

COPY . .

ENV PYTHONUNBUFFERED=1 \
    CHROME_BIN=/usr/bin/google-chrome \
    CHROMEDRIVER_BIN=/usr/local/bin/chromedriver \
    CHROME_OPTS="--headless=new --no-sandbox --disable-dev-shm-usage --window-size=1920,1080"

CMD ["pytest", "-o", "chrome_options=$CHROME_OPTS", "--alluredir=allure-results"]
