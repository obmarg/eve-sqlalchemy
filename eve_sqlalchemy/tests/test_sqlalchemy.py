from eve_sqlalchemy import db
from eve_sqlalchemy.tests import test_sql_tables, TestBaseSQL


class TestSqlalchemy(TestBaseSQL):
    def test_default_works(self):
        person = test_sql_tables.People(firstname="James")
        db.session.add(person)
        db.session.flush()
        assert person._created is not None
        assert person.title == 'Mr.'
