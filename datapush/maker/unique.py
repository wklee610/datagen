import random
import string
import uuid

def _unique_type(
    unique_type: str,
    count: int
) -> list:
    if unique_type == "id":
        data = _generate_unique_ids(count)
    elif unique_type == "uuid":
        data = _generate_unique_uuids(count)
    elif unique_type == "ip":
        data = _generate_unique_ips(count)
    return data

def _generate_unique_ids(count: int, length=10):
    characters = string.ascii_lowercase + string.digits
    unique_ids = set()

    for _ in range(count):
        random_id = ''.join(random.choices(characters, k=length))
        unique_ids.add(random_id)
    
    return list(unique_ids)

def _generate_unique_uuids(count) -> list:
    unique_uuids = set()
    for _ in range(count):
        unique_uuids.add(uuid.uuid4())
    return list(unique_uuids)

def _generate_unique_ips(count) -> list:
    unique_ips = set()

    for _ in range(count):
        first_octet = random.randint(1, 254)
        second_octet = random.randint(0, 255)
        third_octet = random.randint(0, 255)
        fourth_octet = random.randint(1, 254)

        ip = f'{first_octet}.{second_octet}.{third_octet}.{fourth_octet}'
        unique_ips.add(ip)
    
    return list(unique_ips)
