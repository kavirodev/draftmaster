
from datetime import datetime

from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    drafts: Mapped[list["Draft"]] = relationship(back_populates="user")


class Hero(Base):
    __tablename__ = "heroes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    localized_name: Mapped[str | None] = mapped_column(String(100))
    primary_attribute: Mapped[str | None] = mapped_column(String(20))
    attack_type: Mapped[str | None] = mapped_column(String(20))
    roles: Mapped[str | None] = mapped_column(String(100))
    image_url: Mapped[str | None] = mapped_column(String(255))

    picks: Mapped[list["DraftPick"]] = relationship(back_populates="hero")


class Draft(Base):
    __tablename__ = "drafts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    title: Mapped[str | None] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    user: Mapped["User"] = relationship(back_populates="drafts")
    picks: Mapped[list["DraftPick"]] = relationship(
        back_populates="draft",
        cascade="all, delete-orphan"
    )


class DraftPick(Base):
    __tablename__ = "draft_picks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    draft_id: Mapped[int] = mapped_column(ForeignKey("drafts.id"), nullable=False)
    hero_id: Mapped[int] = mapped_column(ForeignKey("heroes.id"), nullable=False)
    team: Mapped[str] = mapped_column(String(10), nullable=False)
    role: Mapped[str | None] = mapped_column(String(30))
    pick_order: Mapped[int] = mapped_column(Integer, nullable=False)

    draft: Mapped["Draft"] = relationship(back_populates="picks")
    hero: Mapped["Hero"] = relationship(back_populates="picks")
