routes = {}

def get(path):
    def decorator(func):
        routes[path] = func
        return func
    return decorator


@get("/hello")
def hello():
    return "Hello, decorators!"


@get("/world")
def world():
    return "World, here I am."


# simulate calling the "server"
for path, func in routes.items():
    print(f"{path} -> {func()}")