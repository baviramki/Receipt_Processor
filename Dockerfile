FROM python:3.6.4-alpine

RUN pip install --upgrade pip
RUN pip install Flask
RUN pip install uuid
RUN pip install marshmallow

EXPOSE 5000

WORKDIR /app


COPY . .

CMD ["python3","-m" , "flask", "run", "--host","0.0.0.0"]