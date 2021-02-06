# pypi
import airflow
from airflow import DAG

FILE_NAME = __file__.split("/")[-1].split(".")[0]

dag = DAG(
    dag_id=FILE_NAME
)
