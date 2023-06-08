FROM python:latest

WORKDIR /in_a_bottle

COPY . .

CMD ["python", "main.py"]

EXPOSE 8080