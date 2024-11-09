# Datapush

Datapush is a Python package that generate data to MySQL Database directly.

When you need data for MySQL for some reasons (for test), and too lazy to make mock data, here is the answer.  

## Download

```bash
pip install datapush
```

## Usage
```python
# Connect to db
conn = datapush.mysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    database=''
)

# Make generator with connection
generator = datapush.Generator(conn)

# Generate!
generator.generate(
    table='example_table'
)
```

## Extra Option
In generator.generate(), there has several options.

    Args:
        - table         (str): The name of the table.
        - count         (int): The number of data you want to generate. (default: 10)
        - **option      (dict): Some specific data for each column
                        you want to generate (uuid, username, ip, etc...)  
                        ex) user=id, uuid=uuid, ip_address=ip,   
                        ex) column_name=type

## Extra Usage
```python
generator.generate(
    table='example_table',
    count=1000,
    char_col='ip',          # column_name is char_col and make unique ip
    text_col='id',          # column_name is text_col and make unique id
    varchar_col='uuid'      # column_name is varchar_col and make unique uuid
)
```



