from django.db import models

from django.core.validators import MinLengthValidator


class Thing(models.Model):
    name = models.CharField(
            max_length=200,
            help_text='Enter a category (e.g. School)',
            validators=[MinLengthValidator(2, "Thing must be greater than 1 character")]
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Task(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Task must be greater than 1 character")]
    )
    description = models.CharField(max_length=300)
    thing = models.ForeignKey('Thing', on_delete=models.CASCADE, null=False)

    # Shows up in the admin list
    def __str__(self):
        return self.name

