## Fast API e-commerce shop

### Technology

- SQLAlchemy
- Alembic
- logging with Middleware
- 


### Local run:  
1. Download project
2. install requirements
3. add dates to `alembic.ini` and `db.py`
4. start migrations:

```commandline
alembic init -t async app/migrations
```

```commandline
alembic revision --autogenerate -m "Initial migration"
```

```commandline
alembic upgrade head
```
5. check tables

6. start server:
```commandline
uvicorn app.main:app --reload
```

[main page docs](http://127.0.0.1:8000/docs)

7. Create users (examples):

- User name admin 123456

- Slava - customer 123456

- Semen customer2 111111

8. Docker  
- close containers 
```commandline
docker-compose down -v
```
- build containers
```commandline
docker-compose up -d --build
```
- start migrations command
```commandline
docker-compose exec web alembic upgrade head
```
