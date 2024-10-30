FROM python:3.12

RUN pip install -U pip
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . .
ENTRYPOINT [ "python", "app.py" ]