FROM python:3.9

WORKDIR /app

COPY service /app/service
COPY requirements/prod.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 1234
CMD ["uvicorn", "service.app:app", "--host", "0.0.0.0", "--port", "1234"]
