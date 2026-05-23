FROM python:3.12

WORKDIR /framework

COPY . .

RUN pip install -r requirements.txt

CMD ["pytest","-v"]