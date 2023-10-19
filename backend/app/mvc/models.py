from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base


class Domain(Base):
    __tablename__ = "domain"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)


class Industry(Base):
    __tablename__ = "industry"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    domain_id = Column(Integer, ForeignKey("domain.id"), nullable=False)

    domain = relationship("Domain", back_populates="industry")
