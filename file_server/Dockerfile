
FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8080
ENV NAME World
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
