from django.db import models

from scraping.utils import from_cyrillic_to_eng

def default_url():
    return {"work" : "", "rabota": "", "dou":  "", "djinni": ""}


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название населенного пункта", unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)


    class Meta:
        verbose_name = "Города"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)

class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name="Язык программирования", unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = "Языки программирования"
        verbose_name_plural = "Языки программирования"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs): # Переопределение save
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))

        super().save(*args, **kwargs)

class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name="Заголовок вакансии")
    company = models.CharField(max_length=250, verbose_name="Компания")
    description = models.TextField(verbose_name="Описание вакансии")
    city = models.ForeignKey(to=City, on_delete=models.CASCADE, verbose_name="Город")
    language = models.ForeignKey(to=Language, on_delete=models.CASCADE, verbose_name="Язык программирования")
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Вакансии"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.title

class Error(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    data = models.JSONField()

    def __str__(self):
        return f"Дата ошибки: {self.timestamp}"

    class Meta:
        verbose_name = 'Ошибки'
        verbose_name_plural = "Ошибки"

class Url(models.Model):
    city = models.ForeignKey(to=City, on_delete=models.CASCADE, verbose_name="Город")
    language = models.ForeignKey(to=Language, on_delete=models.CASCADE, verbose_name="Язык программирования")
    url_data = models.JSONField(default=default_url())

    def __str__(self):
        return f"Url: {self.city} - {self.language}"

    class Meta:
        unique_together = ("city", "language") # Два уникальных параметра (случайно не добавятся другие данные)
        verbose_name_plural = "Url"