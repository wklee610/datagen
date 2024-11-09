import re
import os
import uuid
import json
import string
import random
from datetime import datetime, timedelta

class DataType:
    def __init__(self, count) -> None:
        self.data = set()
        self.data_list = []
        self.count = count

    # Numeric Data Types
    def _int(self) -> list:
        for _ in range(self.count):
            self.data_list.append(random.randint(0, 255))
        return self.data_list

    def _tinyint(self, type: str) -> list:
        match = re.search(r'\((\d+)\)', type)
        if match:
            max_value = int(match.group(1))
        else:
            max_value = 8
        for _ in range(self.count):
            self.data_list.append(random.randint(0, max_value))
        return self.data_list
    
    def _smallint(self) -> list:
        for _ in range(self.count):
            self.data_list.append(random.randint(0, 255))
        return self.data_list

    def _mediumint(self) -> list:
        for _ in range(self.count):
            self.data_list.append(random.randint(0, 10000))
        return self.data_list

    def _bigint(self) -> list:
        for _ in range(self.count):
            self.data_list.append(random.randint(0, 10000))
        return self.data_list

    def _float(self) -> list:
        for _ in range(self.count):
            self.data.add(random.uniform(0, 3.402823466E+38))
        return list(self.data)

    def _double(self) -> list:
        for _ in range(self.count):
            self.data.add(random.uniform(0, 1.7976931348623157E+308))
        return list(self.data)

    def _decimal(self, type: str) -> list:
        match = re.search(r'DECIMAL\((\d+), (\d+)\)', type)
        if match:
            precision = int(match.group(1))
            scale = int(match.group(2))
        else:
            precision = 10
            scale = 2

        max_value = 10 ** (precision - scale) - 10 ** (-scale)
        for _ in range(self.count):
            self.data.add(round(random.uniform(0, max_value), scale))
        return list(self.data)
    
    def _numeric(self, type: str) -> list:
        match = re.search(r'NUMERIC\((\d+), (\d+)\)', type)
        if match:
            precision = int(match.group(1))
            scale = int(match.group(2))
        else:
            precision = 10
            scale = 2

        max_value = 10 ** (precision - scale) - 10 ** (-scale)
        for _ in range(self.count):
            self.data.add(round(random.uniform(0, max_value), scale))
        return list(self.data)

    def _bit(self, type) -> list:
        match = re.search(r'\((\d+)\)', type)
        if match:
            max_value = int(match.group(1))
        else:
            max_value = 1
        max_value = 1
        for _ in range(self.count):
            self.data_list.append(int(''.join(random.choice('01') for _ in range(max_value))))
        return self.data_list
    
    # Datetime Data Types
    def _date(self) -> list:
        current_date = datetime.now()
        random_days = random.randint(0, 365)
        random_date = current_date - timedelta(days=random_days)
        for _ in range(self.count):
            self.data_list.append(random_date.strftime('%Y-%m-%d'))
        return self.data_list

    def _datetime(self) -> list:
        current_dt = datetime.now()
        for _ in range(self.count):
            self.data_list.append(current_dt.strftime('%Y-%m-%d %H:%M:%S.%f')[:3])
        return self.data_list

    def _timestamp(self) -> list:
        current_dt = datetime.now()
        for _ in range(self.count):
            self.data_list.append(current_dt.strftime('%Y-%m-%d %H:%M:%S.%f')[:3])
        return self.data_list

    def _time(self) -> list:
        current_dt = datetime.now()
        for _ in range(self.count):
            self.data_list.append(current_dt.strftime('%H:%M:%S'))
        return self.data_list

    def _year(self) -> list:
        current_year = datetime.now().year
        for _ in range(self.count):
            self.data_list.append(current_year)
        return self.data_list
    
    # String Data Types
    def _char(self, type: str) -> list:
        match = re.search(r'\((\d+)\)', type)
        if match:
            max_value = int(match.group(1))
        else:
            max_value = 255
        all_characters = string.ascii_letters + string.digits
        for _ in range(self.count):
            random_string = ''.join(random.choice(all_characters) for _ in range(max_value))
            self.data_list.append(random_string)
        return self.data_list

    def _varchar(self, type: str) -> list:
        match = re.search(r'\((\d+)\)', type)
        if match:
            max_value = int(match.group(1))
        else:
            max_value = 20
        all_characters = string.ascii_letters + string.digits
        for _ in range(self.count):
            random_string = ''.join(random.choice(all_characters) for _ in range(max_value))
            self.data_list.append(random_string)
        return self.data_list

    def _text(self) -> list:
        max_value = 20
        all_characters = string.ascii_letters + string.digits
        for _ in range(self.count):
            random_string = ''.join(random.choice(all_characters) for _ in range(max_value))
            self.data_list.append(random_string)
        return self.data_list

    def _tinytext(self) -> list:
        max_value = 5
        all_characters = string.ascii_letters + string.digits
        for _ in range(self.count):
            random_string = ''.join(random.choice(all_characters) for _ in range(max_value))
            self.data_list.append(random_string)
        return self.data_list

    def _mediumtext(self) -> list:
        max_value = 10
        all_characters = string.ascii_letters + string.digits
        for _ in range(self.count):
            random_string = ''.join(random.choice(all_characters) for _ in range(max_value))
            self.data_list.append(random_string)
        return self.data_list

    def _longtext(self) -> list:
        max_value = 100
        all_characters = string.ascii_letters + string.digits
        for _ in range(self.count):
            random_string = ''.join(random.choice(all_characters) for _ in range(max_value))
            self.data_list.append(random_string)
        return self.data_list

    def _blob(self) -> list:
        size = 64
        for _ in range(self.count):
            self.data_list.append(os.urandom(size))
        return self.data_list

    def _tinyblob(self) -> list:
        size = 64
        for _ in range(self.count):
            self.data_list.append(os.urandom(size))
        return self.data_list

    def _mediumblob(self) -> list:
        size = 128
        for _ in range(self.count):
            self.data_list.append(os.urandom(size))
        return self.data_list

    def _longblob(self) -> list:
        size = 128
        for _ in range(self.count):
            self.data_list.append(os.urandom(size))
        return self.data_list

    def _enum(self, type: str) -> list:
        match = re.search(r"ENUM\((.*)\)", type)
        if match:
            enum_values = [value.strip().strip("'") for value in match.group(1).split(',')]
        else:
            raise ValueError
        for _ in range(self.count):
            self.data_list.append(random.choice(enum_values))
        return self.data_list

    def _set(self, type: str) -> list:
        match = re.search(r"SET\((.*)\)", type)
        if match:
            enum_values = [value.strip().strip("'") for value in match.group(1).split(',')]
        else:
            raise ValueError
        for _ in range(self.count):
            self.data_list.append(random.choice(enum_values))
        return self.data_list

    # Json Data Types
    def _json(self) -> list:
        for _ in range(self.count):
            json_data = {
                "id": ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
                "is_active": random.choice([True, False]),
                "uuid": str(uuid.uuid4()),
                "score": round(random.uniform(0, 100), 2),
            }
            self.data_list.append(json.dumps(json_data))
        return self.data_list

    # Spatial Data Types - TODO
    def _geometry(self) -> list:
        print("Currently Not Support")
        return ValueError
        return list(self.data)

    def _point(self) -> list:
        print("Currently Not Support")
        return ValueError
        return list(self.data)

    def _linestring(self) -> list:
        print("Currently Not Support")
        return ValueError
        return list(self.data)

    def _polygon(self) -> list:
        print("Currently Not Support")
        return ValueError
        return list(self.data)

    def _multipoint(self) -> list:
        print("Currently Not Support")
        return ValueError
        return list(self.data)

    def _multilinestring(self) -> list:
        print("Currently Not Support")
        return ValueError
        return list(self.data)

    def _multipolygon(self) -> list:
        print("Currently Not Support")
        return ValueError
        return list(self.data)

    # Other Data Types
    def _bool(self) -> list:
        for _ in range(self.count):
            self.data_list.append(random.choice([True, False]))
        return self.data_list
    
    def _uuid(self) -> list:
        for _ in range(self.count):
            self.data.add(uuid.uuid4())
        return list(self.data)

    