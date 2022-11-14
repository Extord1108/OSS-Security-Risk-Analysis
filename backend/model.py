# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Contributor(db.Model):
    __tablename__ = 'contributors'

    id = db.Column(db.Integer, primary_key=True)
    human_id = db.Column(db.ForeignKey('human.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    package_id = db.Column(db.String(50, 'utf8mb4_bin'), index=True)

    human = db.relationship('Human', primaryjoin='Contributor.human_id == Human.id', backref='contributors')



class Dependency(db.Model):
    __tablename__ = 'dependencies'

    id = db.Column(db.Integer, primary_key=True)
    dependent_id = db.Column(db.String(50, 'utf8mb4_bin'), index=True)
    dependee_id = db.Column(db.String(50, 'utf8mb4_bin'), index=True)
    type = db.Column(db.String(10, 'utf8mb4_bin'))



class Human(db.Model):
    __tablename__ = 'human'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20, 'utf8mb4_bin'))
    email = db.Column(db.String(50, 'utf8mb4_bin'))
    url = db.Column(db.String(255, 'utf8mb4_bin'))
    expired = db.Column(db.Integer)



class Maintainer(db.Model):
    __tablename__ = 'maintainers'

    id = db.Column(db.Integer, primary_key=True)
    human_id = db.Column(db.ForeignKey('human.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    package_id = db.Column(db.String(50, 'utf8mb4_bin'), index=True)

    human = db.relationship('Human', primaryjoin='Maintainer.human_id == Human.id', backref='maintainers')





class Package(db.Model):
    __tablename__ = 'package'

    id = db.Column(db.String(50, 'utf8mb4_bin'), primary_key=True)
    name = db.Column(db.String(50, 'utf8mb4_bin'))
    description = db.Column(db.String(255, 'utf8mb4_bin'))
    license = db.Column(db.String(20, 'utf8mb4_bin'))
    lastest_time = db.Column(db.String(30, 'utf8mb4_bin'))
    version = db.Column(db.String(20, 'utf8mb4_bin'))
    deprecated = db.Column(db.Integer)
    has_install_script = db.Column(db.Integer)
    repository = db.Column(db.String(255, 'utf8mb4_bin'))
    modified_time = db.Column(db.String(30, 'utf8mb4_bin'))
    is_malicious = db.Column(db.Integer)
