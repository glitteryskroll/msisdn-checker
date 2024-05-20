from ..models import PhoneProvider
from ..data_classes import PhoneProvider as PhoneProviderData
import logging

logger = logging.getLogger("number_service")

def add_providers(providers: list[PhoneProviderData]):
    try:
        providers_to_create = [
            PhoneProvider(
                ndc=provider.ndc,
                snA=provider.snA,
                snB=provider.snB,
                capacity=provider.capacity,
                provider=provider.provider,
                region=provider.region,
                territory_gar=provider.territory_gar,
                inn=provider.inn
            )
            for provider in providers
        ]

        PhoneProvider.objects.bulk_create(providers_to_create, ignore_conflicts=True)
    except Exception as e:
        logger.error(f"add_providers {e}")
        return False
    return True
