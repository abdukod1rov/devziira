from django.contrib import admin
from .models import Post, Comment, Category, SubRoom


def register_models(models: list):
    """
    :type models: model.Model
    """
    for model in models:
        admin.site.register(model)


admin_models = [Post, Comment, Category, SubRoom]

register_models(admin_models)
