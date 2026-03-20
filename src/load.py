from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from db_init import Domain, University, WebPage, engine


class UniversityLoader:
    """Responsavel por transformar listas de dicionarios em dados persistidos no banco."""

    def __init__(self, db_engine=engine) -> None:
        self.db_engine = db_engine

    def load(self, universities: list[dict]) -> int:
        """Persiste universidades no banco e retorna a quantidade inserida."""
        inserted = 0

        with Session(self.db_engine) as session:
            for uni in universities:
                existing = session.scalar(
                    select(University).where(
                        University.name == uni.get("name"),
                        University.country == uni.get("country"),
                    )
                )
                if existing:
                    continue

                university = University(
                    name=uni.get("name"),
                    country=uni.get("country"),
                    state_province=uni.get("state-province"),
                    alpha_two_code=uni.get("alpha_two_code"),
                )
                session.add(university)
                session.flush()

                for domain in uni.get("domains", []):
                    session.add(Domain(university_id=university.id, domain=domain))
                for web_page in uni.get("web_pages", []):
                    session.add(WebPage(university_id=university.id, web_page=web_page))

                inserted += 1

            session.commit()

        return inserted
