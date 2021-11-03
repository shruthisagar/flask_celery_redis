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
