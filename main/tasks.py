from core.celery import app
from time import sleep


@app.task
def high_latency_task():
    sleep(10)
    open('generated_file.txt', 'w').close()


@app.task
def repeating_task():
    file = open('generated_file.txt', 'a')
    file.write('this is added from repeating task')
    file.close()
