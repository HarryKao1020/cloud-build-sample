FROM python:3.10-slim-buster

WORKDIR /app

# 安裝 Edge 和相依的套件
# RUN apt-get update -y && \
#     apt-get install -y wget unzip && \
#     wget https://msedgedriver.azureedge.net/latest/edgedriver_linux64.zip && \
#     unzip edgedriver_linux64.zip -d /usr/bin && \
#     rm edgedriver_linux64.zip && \
#     apt-get remove -y wget unzip

# 複製所有程式碼到工作目錄
COPY . .

# 複製 msedgedriver_linux 到/app/webdriver
COPY webdriver/msedgedriver_linux /app/webdriver/msedgedriver_linux

# 設定 msedgedriver_linux 的執行權限
RUN chmod +x /app/webdriver/msedgedriver_linux

# 安裝所需 Python 套件
RUN pip install --no-cache-dir -r requirements.txt



# 在這裡執行你的 Python 程式
CMD [ "python", "app.py" ]
