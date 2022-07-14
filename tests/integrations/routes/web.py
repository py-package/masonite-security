from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@show").middleware("protect"),
    Route.get("/welcome", "WelcomeController@show"),
]
