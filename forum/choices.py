from django.db import models


class LanguageChoices(models.TextChoices):
    PYTHON = 'py','Python'
    JAVA_SCRIPT = 'js','JavaScript'
    CPP = 'cpp','C++'
    JAVA = 'java','Java'
    OTHER = 'other','Other'

