FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# cloud run上
# CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]

#本地測試
CMD [ "python", "app.py"]