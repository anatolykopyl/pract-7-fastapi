FROM python:3.9

WORKDIR /app

COPY ./main.py ./models.py ./

RUN pip install fastapi uvicorn

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
