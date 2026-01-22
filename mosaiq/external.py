# encoding: utf8

# A class for reading External provider from the Mosaiq database.
#
# Authors:
# Ben George
#
# Python 3.6

from .database import Database

from pprint import pprint

class External:
  
  # Returns a single task matching the given database id (PNP_ID) (or None if no match).
  @classmethod
  def find(cls, id):
    instance = None
    row = Database.fetch_one("SELECT * FROM [External] WHERE PNP_ID = '{}'".format(str(id))) # NB: Bracketed table name as External is SQL keyword
    if row != None:
      instance = cls(row)
    return instance

  # Creates a External instance from a external database row.
  def __init__(self, row):
    # Database attributes:
    self.pnp_id = row['PNP_ID']
    self.last_name = row['Last_Name']
    self.first_name = row['First_Name']