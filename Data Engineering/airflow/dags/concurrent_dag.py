from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule


import pymongo

# get data according to the collection name
def get_data(mongo_collection):
    mongo_username = "spatikaprusty"
    mongo_password = "xEiSjulggyRHE3MU"
    mongo_cluster = "cluster0"
    mongo_database = "Bootcamp"
 
    mongo_ip = f"mongodb+srv://{mongo_username}:{mongo_password}@{mongo_cluster}.bprftog.mongodb.net/{mongo_database}.{mongo_collection}?retryWrites=true&w=majority"

    client = pymongo.MongoClient(mongo_ip)

    db = client[mongo_database]

    collection = db[mongo_collection]

    data = collection.find()
  
    data_list = [doc for doc in data]

    for doc in data_list:
        doc['_id'] = str(doc['_id'])
        
    return data_list




def check_users_data():
    users_data = get_data("users")    
    # Check each user's fullName attribute
    for user in users_data:
        print(user)
        



def check_policies_data():
    policies_data = get_data("policies")
    for policy in policies_data:
        print(policy)
        


def check_policyholders_data():
    policyholders_data = get_data("policyholders")
    for policyholder in policyholders_data:
        print(policyholder)


concurrent_dag = DAG(
    dag_id='Concurrent_Tasks',
    schedule_interval=None,
    start_date=datetime(2024, 2, 11),
    catchup=False,
    concurrency=5  # Limit concurrency to 5 tasks at a time
)

with concurrent_dag:
    check_users = PythonOperator(
        task_id='check_users',
        python_callable=check_users_data,

    )

    check_policies = PythonOperator(
        task_id='check_policies',
        python_callable=check_policies_data,
    )

    check_policyholders = PythonOperator(
        task_id='check_policyholders',
        python_callable=check_policyholders_data,
        trigger_rule=TriggerRule.ALL_SUCCESS
    )


    check_users >> check_policyholders
    check_policies >> check_policyholders
    # check_users >> check_policyholders

