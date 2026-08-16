from .models import GenerationJob, TravelItinerary

def global_empire_context(request):
    return {
        'empire_title': 'Ascendant Agents: Technocratic Empire',
        'system_version': 'ARC-AGI-1 Task Generator Prototype v2.6',
    }