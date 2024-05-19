from data_classes import PhoneProvider
from .settings import connect_to_db


def add_providers(providers: list[PhoneProvider]):
    conn = connect_to_db()
    with conn.cursor() as cursor:
        for provider in providers:
            try:
                query = (
                    """INSERT INTO phone_providers(ndc, "snA", "snB", capacity, provider, region, territory_gar, inn) VALUES (%s, %s, %s, %s, '%s', '%s', '%s', %s) ON CONFLICT (ndc, "snA", "snB") DO NOTHING;"""
                    % (
                        provider.ndc,
                        provider.snA,
                        provider.snB,
                        provider.capacity,
                        provider.provider,
                        provider.region,
                        provider.territory_gar,
                        provider.inn,
                    )
                )
                cursor.execute(str(query))
            except Exception as e:
                conn.rollback()
                print("DEBUG ERROR: add_providers:", e)
                conn.close()
                return False

    conn.commit()
    cursor.close()
    conn.close()
