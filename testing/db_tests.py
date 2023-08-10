from database.db import Database
from core.utils import dict_factory


def test_init_db(db: Database = None) -> tuple:
    """
    Tests that the database is initialized correctly.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/store_records.db") if db is None else db

    if db.database_path != "database/store_records.db":
        error = f"Error in test_init_db: Database path is not correct.\n  - Actual: {db.database_path}"
        return False, error
    else:
        return True, "Database path is correct."


def test_get_inventory_exists(db: Database = None) -> tuple:
    """
    Tests that the inventory is not empty.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/store_records.db") if db is None else db
    full_inventory = db.get_full_inventory()

    if len(full_inventory) == 0:
        error = f"Error in test_get_full_inventory: Full inventory is empty.\n  - Actual: {len(full_inventory)}"
        return False, error
    else:
        return True, "Full inventory is not empty."


def test_dict_factory_link(db: Database = None) -> tuple:
    """
    Tests that the row factory is linked to dict_factory.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string,
    """
    db = Database("database/store_records.db") if db is None else db
    row_factory = db.connection.row_factory

    if row_factory != dict_factory:
        error = f"Error in test_dict_factory_link: Row factory is not linked to dict_factory.\n  - Expected: {dict_factory}\n  - Actual: {row_factory}"
        return False, error
    else:
        return True, "Row factory is linked to dict_factory."


def test_check_connection_threaded(db: Database = None) -> tuple:
    """
    Tests that the database connection is not single threaded.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string,
    """

    db = Database("database/store_records.db") if db is None else db
    connection_is_threaded = db.connection.isolation_level is None

    if connection_is_threaded:
        error = f"Error in test_check_connection_single_thread: Connection is single threaded.\n  - Actual: {connection_is_threaded}"
        return False, error
    else:
        return True, "Connection is not single threaded."

def test_latte_description(db: Database = None) -> tuple:
    """
    Tests that the description of latte is correct.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string,
    """
    
    expected_description ="Our dark, rich espresso balanced with steamed milk and a light layer of foam."
    db = Database("database/store_records.db") if db is None else db

    latte = [item for item in db.get_full_inventory() if item["item_name"] == "Latte"][0]
    actual = latte["info"]
    if latte["info"] != expected_description:
        error = f"Error in test_latte_description: descrition does not match.\n  - Actual: {actual}"
        return False, error
    else:
        return True, "descriptions match."

def test_cappuccino_description(db: Database = None) -> tuple:
    """
    Tests that the description of cappuccino  rum is correct.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string,
    """
    
    expected_description ="Dark, rich espresso lies in wait under a smoothed and stretched layer of thick milk foam."
    db = Database("database/store_records.db") if db is None else db

    cappuccino = [item for item in db.get_full_inventory() if item["item_name"] == "Cappuccino"][0]
    actual = cappuccino["info"]
    if cappuccino["info"] != expected_description:
        error = f"Error in test_cappuccino_description: descrition does not match.\n  - Actual: {actual}"
        return False, error
    else:
        return True, "description match."
    
def test_macchiato_description(db: Database = None) -> tuple:
    """
    Tests that the description of macchiato is correct.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string,
    """
    
    expected_description ="Our rich espresso marked with dollop of steamed milk and foam."
    db = Database("database/store_records.db") if db is None else db

    macchiato = [item for item in db.get_full_inventory() if item["item_name"] == "Macchiato"][0]
    actual = macchiato["info"]
    if macchiato["info"] != expected_description:
        error = f"Error in test_macchiato_description: descrition does not match.\n  - Actual: {actual}"
        return False, error
    else:
        return True, "description match."

def test_caramel_latte_description(db: Database = None) -> tuple:
    """
    Tests that the description of caramel Latte is correct.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string,
    """
    
    expected_description ="Rich espresso with caramel flavor."
    db = Database("database/store_records.db") if db is None else db

    caramel_latte = [item for item in db.get_full_inventory() if item["item_name"] == "Caramel Latte"][0]
    actual = caramel_latte["info"]
    if caramel_latte["info"] != expected_description:
        error = f"Error in test_caramel_latte_description: descrition does not match.\n  - Actual: {actual}"
        return False, error
    else:
        return True, "description match."

def test_espresso_shot_description(db: Database = None) -> tuple:
    """
    Tests that the description of Espresso Shot is correct.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string,
    """
    
    expected_description ="Strong and concentrated coffee."
    db = Database("database/store_records.db") if db is None else db

    espresso_shot = [item for item in db.get_full_inventory() if item["item_name"] == "Espresso Shot"][0]
    actual = espresso_shot["info"]
    if espresso_shot["info"] != expected_description:
        error = f"Error in test_espresso_shot_description: descrition does not match.\n  - Actual: {actual}"
        return False, error
    else:
        return True, "descriptions match."    
