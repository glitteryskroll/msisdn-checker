from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from .crud.read import get_provider_by_number
from .data_classes import PhoneNumber
from django.forms.models import model_to_dict
import logging

logger = logging.getLogger("number_service")

@require_POST
def get_provider(request):
    number = request.POST.get("number", "").replace("+", "")
    if not number.isdigit() or len(number) > 11 or len(number) < 4:
        logger.error(f"get_provider number is not valid:{number}")
        return JsonResponse({"error": "Неправильный номер"}, status=400)
    if len(number) == 11 and (int(number[0]) == 7 or int(number[0]) == 8):
        number = number[1:]
    elif len(number) == 11:
        logger.error(f"get_provider number is not valid:{number}")
        return JsonResponse({"error": "Номер не принадлежит РФ"}, status=400)
    phone_number = PhoneNumber(ndc=number[0:3], sn=number[3:])
    phone_provider = get_provider_by_number(phone_number)
    return JsonResponse(
        {"provider": model_to_dict(phone_provider) if phone_provider else None}
    )


@require_GET
def def_phone_provider_form(request):
    return render(request, "def_phone_form.html")
