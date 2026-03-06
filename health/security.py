from functools import wraps
from django.http import JsonResponse
from django.conf import settings

def health_check_auth(view_func):
    @wraps(view_func)
    async def _wrapped_view(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        secret_token = getattr(settings, 'HEALTH_CHECK_TOKEN', None)

        if not auth_header or auth_header != f"Bearer {secret_token}":
            return JsonResponse(
                {"status": "forbidden", "error": "Invalid token"},
                status=403
            )
        return await view_func(request, *args, **kwargs)
    return _wrapped_view
