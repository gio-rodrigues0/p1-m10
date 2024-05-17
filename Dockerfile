# Base Image 
FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

RUN python main.py create_db

ENTRYPOINT ["python"]
CMD ["main.py"]