from django.contrib.auth.models import User

from django.test import TestCase
from listapp.models import Task


class TestModels(TestCase):
    def setUp(self):
        self.andy = User.objects.create_user(
            username="Andy",
            email="andy@mail.com",
            password="!!2345Asdfg"
        )
        self.rose = User.objects.create_user(
            username="Rose",
            email="rose@mail.com",
            password="!!2345Asdfg"
        )

    def test_create_task(self):
        Task.objects.create(
            title="test message",
            description="some text",
            user=self.andy
        )
        Task.objects.create(
            title="test message 2",
            description="some text",
            user=self.andy
        )
        Task.objects.create(
            title="test message",
            description="some text",
            user=self.rose
        )
        andy_tasks = Task.objects.filter(user__username="Andy")
        rose_tasks = Task.objects.filter(user__username="Rose")
        task_obj = Task.objects.get(user=self.rose)
        self.assertEquals(andy_tasks.count(), 2)
        self.assertEquals(rose_tasks.count(), 1)
        self.assertNotEqual(andy_tasks.count(), rose_tasks.count())
        self.assertEquals(str(rose_tasks[0]), task_obj.title)

    def test_delete_task(self):
        Task.objects.create(
            title="test message",
            description="some text",
            user=self.rose
        )
        tasks_obj = Task.objects.all()
        self.assertEquals(tasks_obj.count(), 1)
        tasks_obj.delete()
        self.assertEquals(tasks_obj.count(), 0)

    def test_update_task(self):
        Task.objects.create(
            title="test message",
            description="some text",
            user=self.andy
        )
        andy_task = Task.objects.get(pk=1)
        self.assertEquals(andy_task.title, "test message")
        Task.objects.filter(pk=1).update(title="updated task")
        # refresh db to update title for new text
        andy_task.refresh_from_db()
        # compare is new title text was updated
        self.assertEquals(andy_task.title, "updated task")
