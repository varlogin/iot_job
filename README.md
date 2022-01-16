## Тестовое задание для ИОТ

Запуск сервиса с 3мя инстансами бэкенда:

```console
docker-compose up -d --scale backend=3
```

Просмотр количества задач на вычислении (в очереди + на выполнении + запланированные):

http://127.0.0.1:8000/running/

Запуск подсчета сумм каждого 10ого столбца в файле:

http://127.0.0.1:8000/calculate/{file_name}/

Просмотр результата выполнения задачи:

http://127.0.0.1:8000/result/{job_id}/

**Сгенерировать тестовые данные можно так:**
```console
python3 data_generator.py data.csv 50 3000000
```

## Комментарий к решению:

Не понял, что за фишка с кучей двойных кавычек в data.csv. Выглядит как баг. Не стал с этим ничего делать. Работаю с файлом как если бы в нем не было никаких кавычек.

По AWS делать ничего не стал, так как опыта работы с ним нет и ради тестового разбираться с этим не хочется.

Можно было бы использовать связку Django Rest Framework + Celery + RabbitMQ, как на моем текущем стеке, но я решил поковырять что-нибудь совсем новое для меня и легковесное, раз подвернулась такая возможность. Взял FastAPI + RQ + Redis.

Масштабирование сервиса идет за счет запуска новых docker контейнеров с воркером RQ. При необходимости можно было бы запустить несколько воркеров RQ в одном контейнере с помощью Supervisor. Сервис API и Redis думаю масштабировать не нужно. А если вдруг нужно, то Redis масштабируется. А перед несколькими инстансами API я бы поставил Nginx.

Для нестабильного подключения настроил 3 попытки выполнения задачи.