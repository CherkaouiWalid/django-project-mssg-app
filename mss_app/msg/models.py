from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.
class Msg(models.Model):
    sender=models.ForeignKey(User, on_delete=models.CASCADE , related_name='sender')
    receiver=models.ForeignKey(User, on_delete=models.CASCADE , related_name='receiver')
    title =models.CharField(max_length=50)
    content = models.TextField()
    datetime = models.DateField()

    def __str__(self):
        return self.title

class MsgForm(ModelForm):
    class Meta:
        model = Msg
        fields = ['receiver', 'title', 'content']