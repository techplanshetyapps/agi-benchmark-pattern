from .models import GenerationJob, TravelItinerary

def global_empire_context(request):
    return {
        'empire_title': 'Ascendant Agents: Technocratic Empire',
        'system_version': 'ARC-AGI-1 Task Generator Prototype v2.6',
    }

from cloudinary.utils import cloudinary_url

seo_image_url, _ = cloudinary_url("sky", fetch_format="auto", quality="auto")

def cloud_assets(request):
    return {
        'sky_image_url': seo_image_url
    }