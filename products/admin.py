from django.contrib import admin
from .models import LEDProduct, StageProduct, SoundProduct, LightingProduct, AccessoryProduct

@admin.register(LEDProduct)
class LEDProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'led_type', 'pixel_pitch', 'brightness']
    list_filter = ['available', 'led_type']
    search_fields = ['name', 'description']

@admin.register(StageProduct)
class StageProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'stage_type', 'dimensions', 'max_load']
    list_filter = ['available', 'stage_type', 'material']
    search_fields = ['name', 'description']

@admin.register(SoundProduct)
class SoundProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'sound_type', 'power_output']
    list_filter = ['available', 'sound_type']
    search_fields = ['name', 'description']

@admin.register(LightingProduct)
class LightingProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'lighting_type', 'wattage']
    list_filter = ['available', 'lighting_type']
    search_fields = ['name', 'description']

@admin.register(AccessoryProduct)
class AccessoryProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'accessory_type', 'weight']
    list_filter = ['available', 'accessory_type']
    search_fields = ['name', 'description']
