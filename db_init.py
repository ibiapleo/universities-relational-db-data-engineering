from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import uuid

Base = declarative_base()

class University(Base):
    __tablename__ = 'universities'
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    state_province = Column(String)
    alpha_two_code = Column(String)
    domains = relationship("Domain", back_populates="university")
    web_pages = relationship("WebPage", back_populates="university")

class Domain(Base):
    __tablename__ = 'university_domains'
    id = Column(Integer, primary_key=True)
    university_id = Column(Integer, ForeignKey('universities.id'))
    domain = Column(String)
    university = relationship("University", back_populates="domains")

class WebPage(Base):
    __tablename__ = 'university_webpages'
    id = Column(Integer, primary_key=True)
    university_id = Column(Integer, ForeignKey('universities.id'))
    web_page = Column(String)
    university = relationship("University", back_populates="web_pages")

engine = create_engine('sqlite:///unis.db')
Base.metadata.create_all(engine)