from app import celery


@celery.task()
def add_2_digits(a, b):
    print(a + b)


@celery.task()
def sub_2_digits(a, b):
    print(a - b)
