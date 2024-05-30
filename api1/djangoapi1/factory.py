import factory
from factory.faker import faker

from .models import Poll

FAKE = faker.Faker()

class PollFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Poll

    question =factory.Faker('sentence', nb_words=10)
    slug = factory.Faker('slug')