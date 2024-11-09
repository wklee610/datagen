from typing import Optional
from datapush.maker import maker
from datapush.maker import unique

class Generator:
    def __init__(self, connection) -> None:
        self.conn = connection
        self.option_config = ["id", "uuid", "ip"]
    
    def generate(
        self,
        table: str,
        count: Optional[int] = 10,
        **option: dict,
    ) -> None:
        """
        Generate test data to MySQL table

        Args:
            - table         (str): The name of the table.
            - count         (int): The number of data you want to generate. (default: 10)
            - **option      (dict): Some specific data for each column  
                            you want to generate (uuid, username, ip, etc...)  
                            ex) user=id, uuid=uuid, ip_address=ip,   
                            ex) column_name=type
        """
        
        try:
            col_names = []
            values = []
            with self.conn.cursor() as cursor:
                cursor.execute(f"DESCRIBE {table}")
                columns = cursor.fetchall()

                for col_info in columns:
                    name, type = maker._check_column(
                        col_info=col_info
                    )
                    if name == None and type == None:
                        continue
                    else:
                        col_names.append(name)
                    if name in option:
                        unique_type = option[name]
                        if unique_type in self.option_config:
                            data = unique._unique_type(
                                unique_type=unique_type,
                                count=count
                            )
                            values.append(data)
                        else:
                            print("unique type doesn't exist!")
                            raise Exception
                    else:
                        data = maker.datamaker(type.upper(), count)
                        values.append(data)

                transformed_values = list(zip(*values))
                query_col_names = ", ".join(col_names)
                placeholders = ", ".join(["%s"] * len(col_names))
                sql_query = f"INSERT INTO {table} ({query_col_names}) VALUES ({placeholders})"
                cursor.executemany(sql_query, transformed_values)
                self.conn.commit()
                print("Data inserted successfully")
                

        except Exception as e:
            print(e)

        finally:
            self.conn.close()


    