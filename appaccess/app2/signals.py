def populate_models(sender, **kwargs):
    from django.apps import apps
    from .apps import App2Config
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    group_app, created = Group.objects.get_or_create(name=App2Config.name)

    models = apps.all_models[App2Config.name]
    for model in models:
        content_type = ContentType.objects.get(
            app_label=App2Config.name,
            model=model
        )
        permissions = Permission.objects.filter(content_type=content_type)
        group_app.permissions.add(*permissions)