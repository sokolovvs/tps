FROM python:3.7-alpine

COPY . /tps
RUN cd /tps && python -m pip install -r /tps/requirements.txt
RUN ls -lah /tps
EXPOSE 5000
CMD ["python", "/tps/app.py"]