FROM python:3.7.7

WORKDIR /app

# Set Flask env variables
ENV FLASK_APP=main.py \
    FLASK_DEBUG=1

# By default Flask use port 5000
EXPOSE 5000

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "./main.py"]