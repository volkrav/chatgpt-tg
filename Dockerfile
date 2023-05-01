FROM python:3.11

RUN mkdir /app

WORKDIR /app

COPY . .

RUN apt update && apt install ffmpeg -y

RUN pip install pipenv

RUN pipenv install --system --deploy --ignore-pipfile

RUN pip freeze

CMD [ "pipenv", "run", "python", "main.py" ]
