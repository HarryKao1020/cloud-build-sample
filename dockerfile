FROM python:3.10-slim-buster

WORKDIR /app



# 安裝 Chrome 和相依的套件
RUN apt-get update && apt-get install -y wget gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update && apt-get install -y google-chrome-stable

# 下載並安裝 Chrome WebDriver
RUN wget https://chromedriver.storage.googleapis.com/LATEST_RELEASE -O /tmp/chromedriver_latest \
    && wget https://chromedriver.storage.googleapis.com/$(cat /tmp/chromedriver_latest)/chromedriver_linux64.zip -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && chmod +x /usr/local/bin/chromedriver \
    && rm /tmp/chromedriver_latest /tmp/chromedriver.zip

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# cloud run上
# CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]

#本地測試
CMD [ "python", "app.py"]