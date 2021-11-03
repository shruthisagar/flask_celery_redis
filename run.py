from app import create_app
import app

# Run Flower 
# celery -A celery_worker.celery flower  --address=127.0.0.1 --port=5555
# run celery 
# celery -A celery_worker.celery worker --loglevel=info
if __name__ == "__main__":
    app = create_app(celery=app.celery)
    app.run()
