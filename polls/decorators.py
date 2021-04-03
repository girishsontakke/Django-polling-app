from django.shortcuts import redirect


def no_user_required(view_func):
    def decorator(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("polls:index")
        return view_func(request, *args, **kwargs)
    return decorator
