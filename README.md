Celery_example
==============

Example of using celery with sqlite3

Tutorial:

1. Install celery and rabbitmq

2. start rabbitmq

3. create db (python create_db.py)

4. start celery (celery multi start 2 -Q:1 nivel1 -Q:2 nivel2 -c:1 5 -c:2 5 -l info -c1 --pidfile=%n.pid)

5. insert task (python launch_task.py)

6. view result (python view_result.py id_return_launch_task)
