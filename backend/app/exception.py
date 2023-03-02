from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

def custom_exception_handler(exc, context):
    # Call the default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    print(context,"\n\n\n")
    if response is not None:
        # If the response is already a JSON response, return it unchanged.
        if response.content_type == 'application/json':
            return response

        # Otherwise, convert the response to a JSON response.
        if isinstance(exc, ValidationError):
            data = {
                'errors': exc.detail,
            }
        else:
            data = {
                'error': str(exc)
            }
        return Response(data, status=response.status_code)

    return response
