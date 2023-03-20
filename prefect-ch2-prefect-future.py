import time
from prefect import task, flow

@task
def my_task():
    return 1

@flow
def my_flow():
    result = my_task.submit() # this is not a python object. It's a PrefectFuture object .submit() is a method of PrefectFuture

if __name__ == "__main__":
    my_flow()