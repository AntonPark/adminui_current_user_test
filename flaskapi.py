from adminui import *

app = AdminApp()

@app.login()
def on_login(username, password):
    if username=='user' and password=='123456':
        return LoggedInUser("Alice",auth=['user'],user_info='test')
    else:
        return LoginFailed()

@app.page('/', 'Logged In', auth_needed='user')
def form_page():
    return [
        Card('Logged In', [
            Header(f'You are logged in as {app.current_user()}')
        ])
    ]

app.run()
