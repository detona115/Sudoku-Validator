FROM python:3.8

LABEL author="Andy"
LABEL description="Dockerfile for Sudoku Validator"

COPY main.py /code/
COPY test.py /code/

WORKDIR /code/

CMD ["python3", "main.py"]