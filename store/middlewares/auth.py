from django.shortcuts import redirect

# One-time configuration and initialization.
#this is used to give authorization or it behave like gate for unknowns
def auth_middleware(get_response):

    # Code to be executed for each request before
    # the view (and later middleware) are called.
    def middleware(request):
        returnUrl=request.META['PATH_INFO']

        if not request.session.get('customer'):
            return redirect(f'login?return_url={returnUrl}')



        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware