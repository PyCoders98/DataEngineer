FROM python:3.10

WORKDIR /app

COPY . .

VOLUME app/img_volume

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

