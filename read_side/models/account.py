from sqlalchemy import Column, Integer, String
from read_side.database.base import Base

class AccountReadModel(Base):
    __tablename__ = "account_read_model"

    account_id = Column(String, primary_key=True, index=True)
    balance = Column(Integer, nullable=False)
