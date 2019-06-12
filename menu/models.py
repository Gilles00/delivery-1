from django.db import models
from django.core.validators import MinValueValidator

# TODO actual img
DEFAULT_ITEM_IMG = 'menu_items/default.png'


class MenuItem(models.Model):
    name = models.CharField(max_length=64, unique=True)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    # TODO - height and width fields
    image = models.ImageField(
        upload_to='menu_items/',
        default=DEFAULT_ITEM_IMG)

    def __str__(self):
        return self.name
