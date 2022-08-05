from pysondb import db
from pysondb.errors.db_errors import IdNotFoundError
from typing import Dict, List, Any

class PysonDB:
    def __init__(self, db_name: str) -> None:
        if not db_name.endswith(".json"):
            db_name += ".json"
        self.__db = db.getDb(db_name)

    def add(self, new_data: Dict[str, Any]):
        self.__db.add(new_data)
    
    def add_many(self, data: List[Dict[str, Any]]):
        self.__db.addMany(data)

    def get_all(self)-> List[Dict]:
        return self.__db.getAll()
    
    def get(self):
        return self.__db.get()

    def get_by_query(self, query: Dict[str, str])-> List[Dict]:
        return self.__db.getByQuery(query)

    def get_by_id(self, pk):
        try:
            return self.__db.getById(pk)
        except IdNotFoundError:
            return None

    def delete(self, pk):
        try:
            self.__db.deleteById(pk)
        except IdNotFoundError:
            pass


category_db = PysonDB("categories.json")
expense_db = PysonDB("expenses.json")
