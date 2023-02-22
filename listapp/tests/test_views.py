from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase
from django.urls import reverse

from listapp.views import (
    AboutView, LoginUserView, UserRegisterView,
    UserTasksListView, UpdateTaskView, DeleteTaskView,
    UserAddTaskView, TaskView, logout_view, TdlView
)

from listapp.models import Task


class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='Andy',
            email="andy@mail.com",
            password="!12345Asdfg"
        )
        Task.objects.create(
            title="some message",
            description="d;lmsdvlsnvj",
            user=self.user
        )
        Task.objects.create(
            title="some message 2",
            description="d;lmsdvlsnvj",
            user=self.user
        )

    def test_logout_view(self):
        self.client.login(username="Andy", password="!12345Asdfg")
        response = self.client.get(reverse('logout'))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse('about'))

    def test_login_view(self):
        response = self.client.post('/login/', {"username": "Andy", "password": "!12345Asdfg"})
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_is_view_choosing_tak(self):
        self.client.login(username="Andy", password="!12345Asdfg")
        response = self.client.get(reverse('show_task', args=[1]), {"title": "Curent task Page"})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'listapp/task.html')

    def test_add_task_POST(self):
        self.client.login(username="Andy", password="!12345Asdfg")
        response = self.client.post(reverse("add_task"), {
            "title": "try add task",
            "description": "some text",
            "user": self.user
        })
        andy_tasks = Task.objects.filter(user__username="Andy")
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        self.assertEquals(andy_tasks.count(), 3)

    def test_add_task_GET(self):
        self.client.login(username="Andy", password="!12345Asdfg")
        response = self.client.get(reverse("add_task"), {"title": "Add Page"})
        self.assertEquals(response.status_code, 200)

    def test_update_GET(self):
        self.client.login(username="Andy", password="!12345Asdfg")
        response = self.client.get(reverse("update", args=[1]), {"title": "Update Page"})
        self.assertEquals(response.status_code, 200)
