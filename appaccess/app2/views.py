from django.contrib.auth.decorators import login_required, user_passes_test
from .permissions import is_in_group_app2


@login_required(login_url='where_to_redirect')
@method_decorator(user_passes_test(is_in_group_app2), name='dispatch')
class LogListView(ListView):
    pass