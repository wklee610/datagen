import random
from datetime import datetime
from datapush.maker.dtype import DataType

def _check_column(
    col_info: tuple
) -> str:
    column_name, column_type, is_nullable, key, default, extra = col_info
    if extra == "auto_increment" or default == "CURRENT_TIMESTAMP":
        return None, None
    else:
        return column_name, column_type

def datamaker(
    type: str, 
    count: int
) -> list:
    data = None
    datatype = DataType(count)
    if type.startswith("INT"):
        data = datatype._int()

    elif type.startswith("TINYINT"):
        data = datatype._tinyint(type)

    elif type.startswith("SMALLINT"):
        data = datatype._smallint()

    elif type.startswith("MEDIUMINT"):
        data = datatype._mediumint()

    elif type.startswith("BIGINT"):
        data = datatype._bigint()

    elif type.startswith("FLOAT"):
        data = datatype._float()

    elif type.startswith("DOUBLE"):
        data = datatype._double()

    elif type.startswith("DECIMAL"):
        data = datatype._decimal(type)

    elif type.startswith("NUMERIC"):
        data = datatype._numeric(type)

    elif type.startswith("BIT"):
        data = datatype._bit(type)

    elif type.startswith("DATE"):
        data = datatype._date()

    elif type.startswith("DATETIME"):
        data = datatype._datetime()

    elif type.startswith("TIMESTAMP"):
        data = datatype._timestamp()

    elif type.startswith("TIME"):
        data = datatype._time()

    elif type.startswith("YEAR"):
        data = datatype._year()

    elif type.startswith("CHAR"):
        data = datatype._char(type)

    elif type.startswith("VARCHAR"):
        data = datatype._varchar(type)

    elif type.startswith("TEXT"):
        data = datatype._text()

    elif type.startswith("TINYTEXT"):
        data = datatype._tinytext()

    elif type.startswith("MEDIUMTEXT"):
        data = datatype._mediumtext()

    elif type.startswith("LONGTEXT"):
        data = datatype._longtext()

    elif type.startswith("BLOB"):
        data = datatype._blob()

    elif type.startswith("TINYBLOB"):
        data = datatype._tinyblob()

    elif type.startswith("MEDIUMBLOB"):
        data = datatype._mediumblob()

    elif type.startswith("LONGBLOB"):
        data = datatype._longblob()

    elif type.startswith("ENUM"):
        data = datatype._enum(type)

    elif type.startswith("SET"):
        data = datatype._set(type)

    elif type.startswith("JSON"):
        data = datatype._json()

    elif type.startswith("GEOMETRY"):
        data = datatype._geometry()

    elif type.startswith("POINT"):
        data = datatype._point()

    elif type.startswith("LINESTRING"):
        data = datatype._linestring()

    elif type.startswith("POLYGON"):
        data = datatype._polygon()

    elif type.startswith("MULTIPOINT"):
        data = datatype._multipoint()

    elif type.startswith("MULTILINESTRING"):
        data = datatype._multilinestring()

    elif type.startswith("MULTIPOLYGON"):
        data = datatype._multipolygon()

    elif type.startswith("BOOL"):
        data = datatype._bool()

    elif type.startswith("UUID"):
        data = datatype._uuid()
        
    return data
