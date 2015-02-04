from __future__ import absolute_import

from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from ds.config import db
from ds.db.types.json import JSONEncodedDict


class Task(db.Model):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    app_id = Column(Integer, ForeignKey('app.id', ondelete="CASCADE"),
                    nullable=False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete="CASCADE"),
                     nullable=False)
    name = Column(String(128), nullable=False, default='deploy')
    ref = Column(String(128), nullable=False)
    sha = Column(String(40), nullable=False)
    environment = Column(String(64), nullable=False, default='production')
    provider = Column(String(64), nullable=False)
    data = Column(JSONEncodedDict)
    date_created = Column(DateTime, default=datetime.utcnow, nullable=False)

    @property
    def provider_config(self):
        return self.data['provider_config']
