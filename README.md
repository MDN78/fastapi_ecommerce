
start server:
```commandline
uvicorn app.main:app --reload
```

[main page docs](http://127.0.0.1:8000/docs)

create environment migrations:
```commandline
alembic init app/migrations
```

first migration:
```commandline
alembic revision --autogenerate -m "Initial migration"
```

User name admin 123456