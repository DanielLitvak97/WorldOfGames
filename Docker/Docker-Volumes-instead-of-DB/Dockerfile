FROM python:3

RUN pip install flask

#Can also do this:
#COPY ../../requirements.txt /
#RUN pip install -r /requirements.txt

COPY ../../Python/MainScores.py /

CMD ["python", "MainScores.py"]
