from django.db import models

from django.core.validators import MinLengthValidator


class Thing(models.Model):
    name = models.CharField(
            max_length=200,
            help_text='Enter a category (e.g. School)',
            validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name
