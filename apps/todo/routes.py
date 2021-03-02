def includeme(config):
    config.add_route('info', '/api/v1/')
    config.add_route('register', '/api/v1/accounts')
    config.add_route('profile_detail', '/api/v1/accounts/{username}')
    config.add_route('login', '/api/v1/accounts/login')
    config.add_route('logout', '/api/v1/accounts/logout')
    config.add_route('tasks', '/api/v1/accounts/{username}/tasks')
    config.add_route('task_detail', '/api/v1/accounts/{username}/tasks/{id}')
