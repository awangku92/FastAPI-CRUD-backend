from sqlalchemy import Column, String, Integer
from db.db import Base

class User(Base):
	__tablename__='user'

	id = Column(Integer, primary_key=True)
	name  = Column(String(256))
	phoneno = Column(String(15))

	def __init__(self, name, phoneno):
		self.name = name
		self.phoneno = phoneno