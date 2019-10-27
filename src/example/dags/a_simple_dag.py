from datetime import datetime
import random

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator, PythonOperator


A_SIMPLE_DAG = DAG(
    dag_id='a_simple_dag',
    start_date=datetime(2019, 10, 1),
    schedule_interval=None,
)


def random_number_generator():
    return random.randrange(-1, 1)


RANDOM_NUMBER_GENERATOR_TASK = PythonOperator(
    task_id='random_number_generator',
    python_callable=random_number_generator,
    dag=A_SIMPLE_DAG
)


def print_number(**context):
    number = context['task_instance'].xcom_pull(task_ids='random_number_generator')
    print(number)

    if number < 0:
        return 'negative_number'

    if number > 0:
        return 'positive_number'

    return 'zero'


PRINT_NUMBER_TASK = BranchPythonOperator(
    task_id='print_number',
    python_callable=print_number,
    provide_context=True,
    dag=A_SIMPLE_DAG
)


NEGATIVE_NUMBER_TASK = DummyOperator(
    task_id='negative_number',
    dag_=A_SIMPLE_DAG
)


POSITIVE_NUMBER_TASK = DummyOperator(
    task_id='positive_number',
    dag_=A_SIMPLE_DAG
)

ZERO_TASK = DummyOperator(
    task_id='zero',
    dag_=A_SIMPLE_DAG
)


RANDOM_NUMBER_GENERATOR_TASK >> PRINT_NUMBER_TASK
PRINT_NUMBER_TASK >> NEGATIVE_NUMBER_TASK
PRINT_NUMBER_TASK >> POSITIVE_NUMBER_TASK
PRINT_NUMBER_TASK >> ZERO_TASK
