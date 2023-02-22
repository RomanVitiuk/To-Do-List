anonymus_menu = [
    {'title': 'About TDL', 'url_name': 'about'},
    {'title': 'Registation', 'url_name': 'register'},
    {'title': 'Login', 'url_name': 'login'},
]

authenticated_menu = [
    {'title': 'TDL', 'url_name': 'index'},
    {'title': 'New Task', 'url_name': 'add_task'},
    {'title': 'Logout', 'url_name': 'logout'},
]


class DataMixin:

    def get_custom_context(self, **kwargs):
        context = kwargs
        context['menu'] = anonymus_menu
        if self.__is_auth_user():
            context['menu'] = authenticated_menu
        return context

    def __is_auth_user(self):
        return self.request.user.is_authenticated
