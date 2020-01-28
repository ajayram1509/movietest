from django.apps import AppConfig


class MoviesInfoConfig(AppConfig):
    name = 'movies_info'

    def ready(self):
        import movies_info.signals