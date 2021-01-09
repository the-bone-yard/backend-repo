from django.db import models

# Create your models here.

class Park():
    park_info = ''
    def __init__(self, park):
        self.park_info = park
        # import code; code.interact(local=dict(globals(), **locals()))
