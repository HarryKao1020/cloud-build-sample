FROM python:3.10-slim-buster

WORKDIR /app

# 安裝 Chrome 和相依的套件
RUN apt-get update && apt-get install -y wget unzip gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update && apt-get install -y google-chrome-stable

# 下載並安裝 Chrome WebDriver
RUN wget https://chromedriver.storage.googleapis.com/LATEST_RELEASE -O /tmp/chromedriver_latest \
    && wget https://chromedriver.storage.googleapis.com/$(cat /tmp/chromedriver_latest)/chromedriver_linux64.zip -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && chmod +x /usr/local/bin/chromedriver \
    && rm /tmp/chromedriver_latest /tmp/chromedriver.zip

# 複製所有程式碼到工作目錄
COPY . .

# 安裝所需 Python 套件
RUN pip install --no-cache-dir -r requirements.txt

# 在這裡執行你的 Python 程式
CMD [ "python", "web_crawler.py" ]
