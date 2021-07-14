FROM python:3.9-buster
WORKDIR /code
ADD / /
COPY . .
RUN python -m pip install -r requirements.txt
EXPOSE 5000
CMD [ "python", "./app.py" ]