from . import models
import factory

class UserFactory(factory.Factory):
    class Meta:
        model = models.Requests  # Equivalent to ``model = myapp.models.User``
        django_get_or_create = ('username',)

    username = 'john'