FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /application

WORKDIR /application

COPY poetry.lock pyproject.toml ./
RUN pip install poetry==1.8.0 && poetry config virtualenvs.create false && poetry install --no-dev

COPY . .

CMD ["uvicorn", "src.main:app", "--host", "localhost", "--port", "7777"]
