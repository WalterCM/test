from django.db import models

class Exam(models.Model):
    exam_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.exam_name

class Question(models.Model):
    exam = models.ManyToManyField(Exam)
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=0)
    def __str__(self):
        return self.choice_text
    def is_correct(self):
        return bool(self.correct)

class Tag(models.Model):
    question = models.ManyToManyField(Question)
    tag_text = models.CharField(max_length=200)
    def __str__(self):
        return self.tag_text
