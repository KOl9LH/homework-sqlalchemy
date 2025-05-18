import sqlalchemy as s
import datetime
from sqlalchemy.orm import relationship
from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'
    id = s.Column(s.Integer, primary_key=True, autoincrement=True)
    team_leader = s.Column(s.Integer, s.ForeignKey('users.id'))
    job = s.Column(s.String)
    work_size = s.Column(s.Integer)
    collaborators = s.Column(s.String)
    start_date = s.Column(s.DateTime, default=datetime.datetime.now)
    end_date = s.Column(s.DateTime, default=datetime.datetime.now)
    is_finished = s.Column(s.Boolean, default=False)

    user = relationship("User", backref="jobs")
