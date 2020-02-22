FROM python:3
COPY MainScores.py /
COPY Scores.txt /
RUN pip install flask
CMD ["python", "MainScores.py"]
