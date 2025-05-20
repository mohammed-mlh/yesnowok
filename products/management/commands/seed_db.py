from django.core.management.base import BaseCommand
from products.models import LEDProduct, StageProduct, SoundProduct, LightingProduct, AccessoryProduct

class Command(BaseCommand):
    help = 'Seed the database with sample products'

    def handle(self, *args, **kwargs):
        # Clear existing data
        LEDProduct.objects.all().delete()
        StageProduct.objects.all().delete()
        SoundProduct.objects.all().delete()
        LightingProduct.objects.all().delete()
        AccessoryProduct.objects.all().delete()

        # Create LED Products
        led_products = [
            {
                "name": "P3.91 Indoor LED Panel",
                "description": "High-resolution indoor LED display panel",
                "price": 599.99,
                "stock": 50,
                "led_type": "SMD",
                "pixel_pitch": 3.91,
                "brightness": 1200,
                "panel_size": "500x500mm"
            },
            {
                "name": "P2.5 Ultra HD LED Wall",
                "description": "Ultra high definition LED wall for indoor use",
                "price": 899.99,
                "stock": 30,
                "led_type": "SMD 2121",
                "pixel_pitch": 2.5,
                "brightness": 1500,
                "panel_size": "600x600mm"
            },
            {
                "name": "P5 Outdoor LED Screen",
                "description": "Weatherproof outdoor LED display",
                "price": 799.99,
                "stock": 25,
                "led_type": "SMD 3535",
                "pixel_pitch": 5.0,
                "brightness": 5500,
                "panel_size": "960x960mm"
            }
        ]

        # Create Stage Products
        stage_products = [
            {
                "name": "Aluminum Stage Platform",
                "description": "Professional stage platform for events",
                "price": 299.99,
                "stock": 20,
                "stage_type": "Platform",
                "dimensions": "2m x 1m",
                "max_load": 750.0,
                "material": "Aluminum"
            },
            {
                "name": "Mobile Stage System",
                "description": "Complete mobile stage with roof",
                "price": 5999.99,
                "stock": 5,
                "stage_type": "Mobile Stage",
                "dimensions": "6m x 4m",
                "max_load": 2000.0,
                "material": "Steel/Aluminum"
            },
            {
                "name": "Stage Riser",
                "description": "Adjustable height stage riser",
                "price": 199.99,
                "stock": 40,
                "stage_type": "Riser",
                "dimensions": "1m x 1m",
                "max_load": 500.0,
                "material": "Steel"
            }
        ]

        # Create Sound Products
        sound_products = [
            {
                "name": "Professional PA Speaker",
                "description": "High-power PA speaker system",
                "price": 899.99,
                "stock": 15,
                "sound_type": "PA Speaker",
                "power_output": 1000,
                "frequency_response": "45Hz-20kHz",
                "connectivity": "XLR, TRS"
            },
            {
                "name": "Digital Mixer",
                "description": "32-channel digital mixing console",
                "price": 2499.99,
                "stock": 10,
                "sound_type": "Mixer",
                "power_output": 100,
                "frequency_response": "20Hz-20kHz",
                "connectivity": "XLR, USB, MIDI"
            },
            {
                "name": "Subwoofer System",
                "description": "18-inch powered subwoofer",
                "price": 1299.99,
                "stock": 12,
                "sound_type": "Subwoofer",
                "power_output": 2000,
                "frequency_response": "30Hz-150Hz",
                "connectivity": "XLR, PowerCON"
            }
        ]

        # Create Lighting Products
        lighting_products = [
            {
                "name": "LED Par Light",
                "description": "RGB LED Par light for stage lighting",
                "price": 149.99,
                "stock": 30,
                "lighting_type": "Par Light",
                "wattage": 200,
                "beam_angle": "25°",
                "color_temperature": "RGB"
            },
            {
                "name": "Moving Head Beam",
                "description": "Professional moving head beam light",
                "price": 899.99,
                "stock": 20,
                "lighting_type": "Moving Head",
                "wattage": 280,
                "beam_angle": "3°",
                "color_temperature": "RGB+W"
            },
            {
                "name": "LED Strip Light",
                "description": "Flexible LED strip for ambient lighting",
                "price": 79.99,
                "stock": 50,
                "lighting_type": "Strip Light",
                "wattage": 50,
                "beam_angle": "120°",
                "color_temperature": "RGB"
            }
        ]

        # Create Accessory Products
        accessory_products = [
            {
                "name": "XLR Cable",
                "description": "Professional balanced XLR cable",
                "price": 29.99,
                "stock": 100,
                "accessory_type": "Cable",
                "compatibility": "All professional audio equipment",
                "dimensions": "10m length",
                "weight": 0.5
            },
            {
                "name": "Power Distribution Box",
                "description": "Professional power distribution system",
                "price": 299.99,
                "stock": 15,
                "accessory_type": "Power",
                "compatibility": "All stage equipment",
                "dimensions": "48.3cm x 15.2cm",
                "weight": 4.5
            },
            {
                "name": "Equipment Case",
                "description": "Heavy-duty road case",
                "price": 199.99,
                "stock": 25,
                "accessory_type": "Case",
                "compatibility": "Various equipment sizes",
                "dimensions": "100cm x 50cm x 50cm",
                "weight": 8.0
            }
        ]

        # Bulk create products
        for products, model in [
            (led_products, LEDProduct),
            (stage_products, StageProduct),
            (sound_products, SoundProduct),
            (lighting_products, LightingProduct),
            (accessory_products, AccessoryProduct)
        ]:
            for product in products:
                model.objects.create(**product)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with multiple products'))