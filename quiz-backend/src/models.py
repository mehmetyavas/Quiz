from django.db import models


# Create your models here.


class Questions(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Answers(models.Model):
    question = models.ForeignKey(Questions,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 related_name='answers',
                                 blank=True
                                 )
    answer = models.CharField(max_length=120, null=True, blank=True)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.question} cevap {self.answer} ____ {self.correct}'
