from .apps import App2Config

def is_in_group_app2(user):
    return user.groups.filter(name=App2Config.name).exists() 