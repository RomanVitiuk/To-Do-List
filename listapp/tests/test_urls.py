from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from listapp.views import (
    AboutView, LoginUserView, UserRegisterView,
    UserTasksListView, UpdateTaskView, DeleteTaskView,
    UserAddTaskView, TaskView, logout_view, TdlView
)


class TestUrls(TestCase):
    def setUp(self):
        User.objects.create_user(
            username="Andy",
            email="andy@mail.com",
            password="!12345Asdfg"
        )

    def test_about_url(self):
        response = self.client.get('')
        url = reverse('about')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(resolve(url).func.view_class, AboutView)

    def test_tdl_url(self):
        self.client.login(username="Andy", password="!12345Asdfg")
        response = self.client.get('/tdl/')
        url = reverse('index')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(resolve(url).func.view_class, UserTasksListView)

    def test_login_url(self):
        response = self.client.get('/login/')
        url = reverse('login')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(resolve(url).func.view_class, LoginUserView)

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_view)

    def test_register_url(self):
        response = self.client.get('/register/')
        url = reverse('register')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(resolve(url).func.view_class, UserRegisterView)

    def test_tasks_list_url(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func.view_class, UserTasksListView)

    def test_update_url(self):
        url = reverse('update', args=[1])
        self.assertEquals(resolve(url).func.view_class, UpdateTaskView)

    def test_delete_url(self):
        url = reverse('delete', args=[5])
        self.assertEquals(resolve(url).func.view_class, DeleteTaskView)

    def test_add_task_url(self):
        url = reverse('add_task')
        self.assertEquals(resolve(url).func.view_class, UserAddTaskView)

    def test_task_info_url(self):
        url = reverse('show_task', args=[12])
        self.assertEquals(resolve(url).func.view_class, TaskView)
