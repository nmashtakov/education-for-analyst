from django.db import models

class Lesson(models.Model):
    lesson_name = models.CharField(max_length=256, blank=False)
    content = models.TextField(blank=True)
    block = models.ForeignKey('Block', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.lesson_name

class Block(models.Model):
    block_name = models.CharField(max_length=64, blank=False)

    def __str__(self):
        return self.block_name
