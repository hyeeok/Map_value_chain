from sqlalchemy import JSON, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class Domain(Base):
    __tablename__ = "domain"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), nullable=False)
    name = Column(String(100), nullable=False)

    industry_classes = relationship("IndustryClass", back_populates="domain")


class IndustryClass(Base):
    __tablename__ = "industry_class"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), nullable=False)
    name = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)
    domain_id = Column(
        Integer, ForeignKey("domain.id", ondelete="CASCADE"), nullable=False
    )

    domain = relationship("Domain", back_populates="industry_classes")
    flowmap = relationship("Flowmap", back_populates="industry_classes")


class Flowmap(Base):
    __tablename__ = "flowmap"

    id = Column(Integer, primary_key=True, index=True)
    node = Column(JSON, nullable=False)
    edge = Column(JSON, nullable=False)
    industry_class_id = Column(Integer, ForeignKey("industry_class.id"))

    industry_classes = relationship("IndustryClass", back_populates="flowmap")
