FROM python:3.11.4-slim-buster

COPY entrypoint.sh entrypoint-simple.sh
RUN chmod +x entrypoint-simple.sh

ENTRYPOINT ["bash", "./entrypoint-simple.sh"]