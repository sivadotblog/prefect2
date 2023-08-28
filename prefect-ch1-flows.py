from prefect import flow

@flow
def my_favorite_function(name="getting_started"): # name is optional. if not provided, a random name will be generated
    print("What is your favorite number?")
    return 42

print(my_favorite_function())

#testflow