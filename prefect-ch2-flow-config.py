import datetime
from prefect import flow, task

@task(name="My Example Task", 
      description="An example task for a tutorial.",
      task_run_name="hello-{name}-on-{date:%A}")
def my_task(name, date):
    pass

@flow
def my_flow():
    # creates a run with a name like "hello-marvin-on-Thursday"
    my_task(name="marvin", date=datetime.datetime.utcnow())


# Run the flow
my_flow()