# Flask - Celery - Integration

In this very simple application, we will be setting up celery in flask for background tasks.

Additional Software Required along with Flask setup is [Redis](https://redis.io/download).

## More About Redis

Redis is an open source, in-memory data structure store, used as a database, cache, and message broker.

In the application we will be using Redis as a Message Broker initially and later on, we shall use it as a backend(database) to store results of the task performed which acts a cache in certain cases.

While Redis is not the only [option](https://docs.celeryproject.org/en/stable/getting-started/backends-and-brokers/), there are many others that are officially supported like:

* RabbitMQ
* Amazon SQS
* Zookeeper
* SQLAlchemy

Redis and RabbitMQ are the most brokers used. A detailed differences between redis and rabbitmq as a broker can be found [here](https://www.educba.com/rabbitmq-vs-redis/).

It is a very common practice to use RabbitMQ as message broker and Redis as backend.
For simplification of understanding of how celery works, I have chosen Redis as both message broker and backend

To run the application, follow steps:

* install redis and make sure its up and running. A sample installation guide for Ubuntu and MAC can be found [here](https://flaviocopes.com/redis-installation/).
* git clone https://github.com/shruthisagar/flask_celery_redis.git
* git checkout master
* create a virtual environment
* pip install -r requirements.txt
* Run flask app using **python run.py**
* Spawn two terminals and run the two commands:
  * Flower - This is used to monitor Celery

            celery -A celery_worker.celery flower  --address=127.0.0.1 --port=5555 

  * Celery itself

            celery -A celery_worker.celery worker --loglevel=info

* There are two URL end points, run them on a terminal or postman, the curl command for the same is:

        - curl 'http://localhost:5000/add'
        - curl 'http://localhost:5000/sub'

* You can find the response being executed in the terminal where celery is running.
* Please refer to my LinkedIn Blog (URL To be attached upon completion) for detailed explaination on the same.
