from fastapi import FastAPI, HTTPException
from redis import Redis
from rq import Queue, Retry
from rq.job import Job
from rq.exceptions import NoSuchJobError

import settings as s
from helpers import exist_data_files
from tasks import calculate_sums

app = FastAPI()

redis_conn = Redis(host=s.REDIS_HOST, port=s.REDIS_PORT, db=s.REDIS_DB)


@app.get('/calculate/{name}')
def run_calculate(name: str):
    """Запускает вычисление сумм файла"""
    if name not in exist_data_files():
        raise HTTPException(status_code=404, detail="File doesn't exist")

    q = Queue(connection=redis_conn)
    job = q.enqueue(calculate_sums, name,
                    result_ttl=-1,
                    job_timeout=s.MAX_JOB_TIMEOUT,
                    retry=Retry(max=s.MAX_RETRY, interval=s.RETRY_INTERVAL))
    return {
        'job_id': job.id
    }


@app.get('/running/')
def running():
    """Возвращает количество запущенных задач (в очереди + на выполнении + запланированные)"""
    q = Queue(connection=redis_conn)
    started_jobs_count = len(q.started_job_registry.get_job_ids())
    scheduled_jobs_count = len(q.scheduled_job_registry.get_job_ids())
    return {
        'running_jobs': q.count + started_jobs_count + scheduled_jobs_count
    }


@app.get('/result/{job_id}/')
def result(job_id: str):
    """Возвращает результат работы задачи"""
    try:
        job = Job.fetch(job_id, connection=redis_conn)
    except NoSuchJobError:
        raise HTTPException(status_code=404, detail="Job doesn't exist")
    return job.result
