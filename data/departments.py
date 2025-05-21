import sqlalchemy as sa
from sqlalchemy.orm import relationship
from data.users import User
from data.db_session import SqlAlchemyBase


class Department(SqlAlchemyBase):
    __tablename__ = 'departments'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String, nullable=False)
    chief = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    members = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, unique=True, nullable=False)

    chief_user = relationship('User', backref='departments_chief', foreign_keys=[chief])