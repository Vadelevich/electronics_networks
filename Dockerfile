FROM python:3.11

WORKDIR / code
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .
RUN python3 manage.py makemigrations

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]