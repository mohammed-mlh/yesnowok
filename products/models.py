from django.db import models

class BaseProduct(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True)
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class LEDProduct(BaseProduct):
    led_type = models.CharField(max_length=100)
    pixel_pitch = models.FloatField(help_text="Pixel pitch in mm")
    brightness = models.IntegerField(help_text="Brightness in nits")
    panel_size = models.CharField(max_length=100)

    class Meta:
        verbose_name = "LED Display"
        verbose_name_plural = "LED Displays"

class StageProduct(BaseProduct):
    stage_type = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=100)
    max_load = models.FloatField(help_text="Maximum load capacity in kg")
    material = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Stage Equipment"
        verbose_name_plural = "Stage Equipment"

class SoundProduct(BaseProduct):
    sound_type = models.CharField(max_length=100)
    power_output = models.IntegerField(help_text="Power output in watts")
    frequency_response = models.CharField(max_length=100)
    connectivity = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Sound Equipment"
        verbose_name_plural = "Sound Equipment"

class LightingProduct(BaseProduct):
    lighting_type = models.CharField(max_length=100)
    wattage = models.IntegerField(help_text="Power consumption in watts")
    beam_angle = models.CharField(max_length=100)
    color_temperature = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Lighting Equipment"
        verbose_name_plural = "Lighting Equipment"

class AccessoryProduct(BaseProduct):
    accessory_type = models.CharField(max_length=100)
    compatibility = models.TextField(help_text="Compatible equipment")
    dimensions = models.CharField(max_length=100, blank=True)
    weight = models.FloatField(help_text="Weight in kg", null=True, blank=True)

    class Meta:
        verbose_name = "Accessory"
        verbose_name_plural = "Accessories"
