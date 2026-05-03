from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'applicant_etl_dag',  # DAG name
    default_args=default_args,
    description='A simple ETL DAG',
    schedule_interval=timedelta(minutes=5),
    start_date=datetime(2026, 5, 2),
    catchup=False,
)

run_etl = BashOperator(
    task_id='run_etl',
    bash_command='bash /home/srinivasan/wrapper_script1.sh ',# don't forge to give a space after the path
    dag=dag,
)
