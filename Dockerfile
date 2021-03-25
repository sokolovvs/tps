FROM python:3.8

COPY . /tps
RUN cd /tps && python -m pip install -r /tps/requirements.txt
EXPOSE 5000
CMD ["python", "/tps/app.py"]
