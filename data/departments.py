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

    @property
    def members_list(self):
        if not self.members:
            return []
        from data.db_session import create_session
        session = create_session()
        ids = [int(i) for i in self.members.split(',') if i.strip().isdigit()]
        return session.query(User).filter(User.id.in_(ids)).all()

    def __repr__(self):
        return f'<Department> {self.id} {self.title}'
