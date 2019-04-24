FROM python:3.7-alpine

# Base settings. Define early to cache layers
WORKDIR /app
EXPOSE 7888
STOPSIGNAL SIGKILL
CMD ["/app/listener.py"]

# Install app dependencies
RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv install --system --deploy

# Install app
COPY listener.py .
