import hashlib


class Model:
    def __init__(self, display_name: str, display_fields: list, query_fields: dict, mutation_fields: dict = None):
        self.database = dict()
        self.display_name = display_name
        self.query_fields = query_fields
        self.display_fields = display_fields
        self.mutation_fields = mutation_fields

    def add(self, data: dict):
        if data:
            # calculate a hash for the vault3
            hash_str = ''
            for field in self.display_fields:
                hash_str += data.get(field).lower()
            data_hash = hashlib.sha256(hash_str.encode('utf-8')).hexdigest()

            # check if that hash already exists in database, if not then add
            if data_hash not in self.database:
                self.database.setdefault(data_hash, data)

    def query(self, filter_params: dict = None, include_hash: bool = False) -> list:
        # TODO: maybe a better algorithm for filtering?
        if filter_params:
            filtered_data = self.database.values()
            for param in filter_params:
                filtered_data = self.filter_data((param, filter_params.get(param)), filtered_data)
            return filtered_data

        if include_hash:
            return list(self.database)
        else:
            return list(self.database.values())

    def len(self):
        return {self.display_name: len(self.database)}

    def filter_data(self, filter_param, data_set) -> list:
        filtered_data = list()
        for record in data_set:
            if filter_param[1] == record.get(filter_param[0]):
                filtered_data.append(record)
        return filtered_data
