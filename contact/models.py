from django.db import models

contact_type = (
    ("cus", "A Customer"),
    ("win", "A Winery")
)

class Contact(models.Model):

    name = models.CharField(max_length=254, null=False, blank=False)
    contact_as = models.CharField(max_length=1024, choices=contact_type,
                                  null=False, blank=False)
    contact_email = models.EmailField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return str(self.name)
