from .apps import App1Config

def is_in_group_app1(user):
    return user.groups.filter(name=App1Config.name).exists() 