SECRET_KEY = "dev-secret-key"
DEBUG = True
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "plans",
]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "/app/db.sqlite3",
    }
}
TEMPLATES = [{"BACKEND": "django.template.backends.django.DjangoTemplates",
               "DIRS": [], "APP_DIRS": True, "OPTIONS": {"context_processors": []}}]
ROOT_URLCONF = "careplan.urls"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
