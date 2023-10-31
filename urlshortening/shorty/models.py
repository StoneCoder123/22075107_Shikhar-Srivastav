from django.db import models
import random
import string


class ModelData(models.Model):
    long_url = models.URLField(max_length=300)
    short_url = models.URLField(max_length=10, unique=True)

    def __str__(self) -> str:
        return self.long_url

    @classmethod
    def shorten(self, long_url):
        CHARs = string.ascii_letters + string.digits
        Length = 10
        self.long_url = long_url
        short_url = ''
        while True:
            short_url = ''.join(random.choice(CHARs) for _ in range(Length))
            uniqueness = ModelData.objects.filter(short_url=short_url).exists()
            if not uniqueness:
                self.short_url = short_url
                break
        try:
            obj = self.objects.create(long_url=long_url, short_url=short_url)
        except:
            obj = self.objects.get(long_url=long_url)
        return obj
