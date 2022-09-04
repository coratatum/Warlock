FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN rm -rf .secrets
# RUN rm -rf .env

CMD [ "python", "main.py" ]