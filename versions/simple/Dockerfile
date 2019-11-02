FROM python:3.7
RUN apt-get update && apt-get install -y supervisor

RUN pip install pipenv

WORKDIR /usr/src/app

ENV AIRFLOW_HOME=/usr/src/app/airflow
ENV AIRFLOW_CONFIG=/usr/src/app/airflow/airflow.cfg

RUN useradd -ms /bin/bash -d /usr/src/app/airflow airflow
RUN chown -R airflow /usr/src/app/airflow

COPY ./airflow.cfg /usr/src/app/airflow

RUN chmod -R +rw /usr/src/app/airflow

COPY ./entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY ./Pipfile .
COPY ./Pipfile.lock .

RUN pipenv install --system

CMD ["/usr/src/app/entrypoint.sh"]
