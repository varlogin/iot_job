# Путь до каталога с csv файлами
DATA_PATH = '/data'

# ######### Redis
REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_DB = 0

# ######### RQ
REDIS_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
QUEUES = ['default']

# Максимальное время выполнения задачи (сек)
MAX_JOB_TIMEOUT = 600

# Максимальное количество попыток выполнения
MAX_RETRY = 3

# Интервал между попытками (сек)
RETRY_INTERVAL = [10, 30, 60]
