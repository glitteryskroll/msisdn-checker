import requests
from ..crud.read import get_random_provider

urls = {
    "get_provider": "http://localhost:8000/def_number/get_provider",
    "def_phone_provider_form": "http://localhost:8000/def_number",
}
response = requests.get(urls["def_phone_provider_form"])
csrftoken = response.cookies.get("csrftoken")
headers = {"X-CSRFToken": csrftoken}
cookies = {"csrftoken": csrftoken}


def test_valid_phone_number_1():
    url = urls["get_provider"]
    ndc = "996"
    sn = "3533111"
    number = ndc + sn
    data = {"number": number}
    response = requests.post(url, data=data, headers=headers, cookies=cookies)
    if response.status_code == 200:
        result = response.json()
        assert int(result["provider"]["ndc"]) == int(ndc)
        assert int(result["provider"]["snA"]) <= int(sn)
        assert int(result["provider"]["snB"]) >= int(sn)
        assert type(result["provider"]["region"]) == str
        assert type(result["provider"]["territory_gar"]) == str
        assert type(result["provider"]["provider"]) == str
        assert result["provider"]["provider"]
        assert result["provider"]["territory_gar"]
        assert result["provider"]["region"]
    else:
        print("DEBUG test_valid_phone_number_1 ERROR: ", response.status_code)
        assert False


def test_valid_phone_number_2():
    url = urls["get_provider"]
    ndc = "900"
    sn = "1"
    number = ndc + sn
    data = {"number": number}
    response = requests.post(url, data=data, headers=headers, cookies=cookies)
    if response.status_code == 200:
        result = response.json()
        assert int(result["provider"]["ndc"]) == int(ndc)
        assert int(result["provider"]["snA"]) <= int(sn)
        assert int(result["provider"]["snB"]) >= int(sn)
        assert type(result["provider"]["region"]) == str
        assert type(result["provider"]["territory_gar"]) == str
        assert type(result["provider"]["provider"]) == str
        assert result["provider"]["provider"]
        assert result["provider"]["territory_gar"]
        assert result["provider"]["region"]
    else:
        print("DEBUG test_valid_phone_number_2 ERROR: ", response.status_code)
        assert False


def test_valid_phone_number_3():
    url = urls["get_provider"]
    cc = "+7"
    ndc = "996"
    sn = "3533111"
    number = cc + ndc + sn
    data = {"number": number}
    response = requests.post(url, data=data, headers=headers, cookies=cookies)
    if response.status_code == 200:
        result = response.json()
        assert int(result["provider"]["ndc"]) == int(ndc)
        assert int(result["provider"]["snA"]) <= int(sn)
        assert int(result["provider"]["snB"]) >= int(sn)
        assert type(result["provider"]["region"]) == str
        assert type(result["provider"]["territory_gar"]) == str
        assert type(result["provider"]["provider"]) == str
        assert result["provider"]["provider"]
        assert result["provider"]["territory_gar"]
        assert result["provider"]["region"]
    else:
        print("DEBUG test_valid_phone_number_3 ERROR: ", response.status_code)
        assert False


def test_valid_phone_number_4():
    url = urls["get_provider"]
    cc = "8"
    ndc = "996"
    sn = "3533111"
    number = cc + ndc + sn
    data = {"number": number}
    response = requests.post(url, data=data, headers=headers, cookies=cookies)
    if response.status_code == 200:
        result = response.json()
        assert int(result["provider"]["ndc"]) == int(ndc)
        assert int(result["provider"]["snA"]) <= int(sn)
        assert int(result["provider"]["snB"]) >= int(sn)
        assert type(result["provider"]["region"]) == str
        assert type(result["provider"]["territory_gar"]) == str
        assert type(result["provider"]["provider"]) == str
        assert result["provider"]["provider"]
        assert result["provider"]["territory_gar"]
        assert result["provider"]["region"]
    else:
        print("DEBUG test_valid_phone_number_4 ERROR: ", response.status_code)
        assert False


def test_valid_phone_provider():
    url = urls["get_provider"]
    random_provider = get_random_provider()
    ndc = random_provider.ndc
    sn = random_provider.snA
    number = str(ndc) + str(sn)
    data = {"number": number}
    response = requests.post(url, data=data, headers=headers, cookies=cookies)
    if response.status_code == 200:
        result = response.json()
        assert int(result["provider"]["ndc"]) == int(ndc)
        assert int(result["provider"]["snA"]) <= int(sn)
        assert int(result["provider"]["snB"]) >= int(sn)
        assert result["provider"]["region"] == random_provider.region
        assert result["provider"]["territory_gar"] == random_provider.territory_gar
        assert result["provider"]["provider"] == random_provider.provider
    else:
        print("DEBUG test_valid_phone_provider ERROR: ", response.status_code)
        assert False


def test_invalid_phone_number_1():
    url = urls["get_provider"]
    data = {"number": "123"}
    response = requests.post(url, data=data, headers=headers, cookies=cookies)

    if response.status_code == 200:
        print("DEBUG test_invalid_phone_number_1 ERROR:", response.status_code)
        assert False
    else:
        assert True


def test_invalid_phone_number_2():
    url = urls["get_provider"]
    data = {"number": "123123jjasd"}
    response = requests.post(url, data=data, headers=headers, cookies=cookies)

    if response.status_code == 200:
        print("DEBUG test_invalid_phone_number_2 ERROR:", response.status_code)
        assert False
    else:
        assert True


def test_invalid_phone_number_3():
    url = urls["get_provider"]
    data = {"number": "889963533111"}
    response = requests.post(url, data=data, headers=headers, cookies=cookies)

    if response.status_code == 200:
        print("DEBUG test_invalid_phone_number_3 ERROR:", response.status_code)
        assert False
    else:
        assert True


def test_invalid_phone_number_4():
    url = urls["get_provider"]
    data = {"number": "/1233"}
    response = requests.post(url, data=data, headers=headers, cookies=cookies)

    if response.status_code == 200:
        print("DEBUG test_invalid_phone_number_4 ERROR:", response.status_code)
        assert False
    else:
        assert True
