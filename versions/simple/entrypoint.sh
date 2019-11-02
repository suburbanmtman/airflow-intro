#!/bin/bash

airflow initdb
chown -R airflow /usr/src/app/airflow

/usr/bin/supervisord
