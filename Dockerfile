
FROM python:3.11-slim

RUN pip install poetry

COPY . .

RUN poetry install

# Run server.py when the container launches
CMD ["poetry", "run", "python", "-m", "server"]

# Expose the port that the application listens on
EXPOSE 3000
