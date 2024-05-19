import psycopg2
from .settings import connect_to_db
from ..data_classes import PhoneNumber, PhoneProvider
from psycopg2.extras import DictCursor


def get_provider_by_number(number: PhoneNumber) -> PhoneProvider:
    try:
        conn = connect_to_db()
        with conn.cursor(cursor_factory=DictCursor) as cursor:
            cursor.execute(
                f""" 
                SELECT *
                FROM phone_providers
                WHERE ndc = {number.ndc}
                AND {number.sn} BETWEEN "snA" AND "snB";
            """
            )
            data = cursor.fetchone()
            if data:
                phone_provider = PhoneProvider(
                    ndc=data["ndc"],
                    snA=data["snA"],
                    snB=data["snB"],
                    capacity=data["capacity"],
                    provider=data["provider"],
                    region=data["region"],
                    territory_gar=data["territory_gar"],
                    inn=data["inn"],
                )
                return phone_provider
            else:
                return None

    except psycopg2.Error as e:
        print("DEBUG ERROR: get_provider_by_number:", e)
        return None


def get_random_provider() -> PhoneProvider:
    try:
        conn = connect_to_db()
        with conn.cursor(cursor_factory=DictCursor) as cursor:
            cursor.execute("SELECT * FROM phone_providers ORDER BY RANDOM() LIMIT 1")
            data = cursor.fetchone()
            if data:
                phone_provider = PhoneProvider(
                    ndc=data["ndc"],
                    snA=data["snA"],
                    snB=data["snB"],
                    capacity=data["capacity"],
                    provider=data["provider"],
                    region=data["region"],
                    territory_gar=data["territory_gar"],
                    inn=data["inn"],
                )
                return phone_provider
            else:
                return None
    except psycopg2.Error as e:
        print("DEBUG ERROR: get_random_provider:", e)
        return None
