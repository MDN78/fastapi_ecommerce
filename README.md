## FastApi E-commerce  

### Create project  
```commandline
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── routers
│   │   ├── __init__.py
│   │   ├── category.py
│   │   └── products.py
```
### Create routers  
1. file `category`  use class from FastApi - `APIRoute` create several functions-templates  
- Get all categories  
- Create category  
- Update category   
- Delete category  

class `APIRoute` can use several parameters:  
```python
APIRouter(*, prefix='', tags=None, dependencies=None, default_response_class=Default(JSONResponse), 
          responses=None, callbacks=None, routes=None, redirect_slashes=True, default=None, 
          dependency_overrides_provider=None, route_class=APIRoute, on_startup=None, on_shutdown=None, 
          lifespan=None, deprecated=None, include_in_schema=True, 
          generate_unique_id_function=Default(generate_unique_id))
```  
2. Transfer routers to main file:
- create method `include_router()` to `main.py`  

3. start server and check result. Use command:
```commandline
uvicorn app.main:app --reload
```
[link to documentation](http://127.0.0.1:8000/docs)  

### Create products  
create templates in file `products.py`  
Methods:
- get all items
- create item
- get by category
- get product detail
- update and delete product   

re-start server and check result. Use command:
```commandline
uvicorn app.main:app --reload
```
### Create models for project  
