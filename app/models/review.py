from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, func
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship

from app.backend.db import Base
from app.models.user import User


class Review(Base):
    __tablename__ = "reviews"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    comment = Column(String, nullable=True)
    comment_data = Column(DateTime, default=func.now())
    grade = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)

    # user = relationship("User", back_populates="reviews")
    # product = relationship("Product", back_populates="reviews")

# from sqlalchemy.schema import CreateTable
# print(CreateTable(Review.__table__))

# if __name__ == '__main__':
#     from sqlalchemy.schema import CreateTable
#     print(CreateTable(Review.__table__))
