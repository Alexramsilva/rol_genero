
FROM python:3.7.8-slim

# remember to expose the port your app'll be exposed on.
EXPOSE 8080

# Ultimate versions

RUN pip install -U pip

COPY requirements.txt app/requirements.txt

# -r: Es una opción que indica a pip que lea los requisitos de instalación desde un archivo de requisitos.

RUN pip install -r app/requirements.txt

# copy into a directory of its own (so it isn't in the toplevel dir)

COPY . /app

WORKDIR /app

# run it!
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]