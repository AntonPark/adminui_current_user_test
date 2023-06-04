1. ставим зависимости requirements.txt
2. запускаем flaskapi.py переходим на корневую страницу и видим, что app.current_user() - выдает нам всю инфу, которую мы сохранили в действии on_login + аватарку с ником в верхнем правом углу
3. запускаем fastapi_start.py (стартуем fastapi через uvicorn) - переходим на главную и видим ошибку в adminui/app.py
```
self.get_header = lambda name, request:request.headers[name] if name in request.headers else None
AttributeError: 'NoneType' object has no attribute 'headers'
```
При этом если закрыть уведомление об ошибке в ерхнем правом углу - мы увидим логин и аватарку,значит система может достать инфу о залогиненом пользователе, просто не через app.current_user()