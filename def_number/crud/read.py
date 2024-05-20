from ..models import PhoneProvider
from ..data_classes import PhoneNumber
import logging

logger = logging.getLogger("number_service")


def get_provider_by_number(number: PhoneNumber) -> PhoneProvider:
    try:
        phone_provider = PhoneProvider.objects.filter(
            ndc=number.ndc,
            snA__lte=number.sn,
            snB__gte=number.sn
        ).first()

        if phone_provider:
            return phone_provider
        else:
            return None

    except Exception as e:
        logger.error(f"get_provider_by_number {e}")
        return None


def get_random_provider() -> PhoneProvider:
    try:
        phone_provider = PhoneProvider.objects.order_by('?').first()

        if phone_provider:
            return phone_provider
        else:
            return None
    except Exception as e:
        logger.error(f"get_random_provider {e}")
        return None
