from masonite.middleware import Middleware


class SecurityMiddleware(Middleware):
    def before(self, request, response):
        """Return the request."""
        print("i am called...")
        return request.app.make("security").secure(request)

    def after(self, request, response):
        """Return the response."""
        return response
