def context_processor(request):
    from django.conf import settings

    return {
        "dynsite_root": settings.DYNSITE_ROOT,
        "staticsite_root": settings.STATICSITE_ROOT,
        }

