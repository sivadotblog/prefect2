from prefect import flow, task
from prefect.tasks import task_input_hash
from datetime import timedelta

@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(minutes=1))
def hello_task(name_input):
    # Doing some work
    print(f"Saying hello {name_input}")
    return "hello " + name_input

@flow
def hello_flow(name_input):
    hello_task(name_input)

# Run the flow
hello_flow(name_input="marvixn")