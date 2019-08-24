from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from passlib.hash import pbkdf2_sha256

db = SQLAlchemy()


class BaseModel(db.Model):
    """Generates basic columns and contains base functions for all models
    
    Args:
        db.Model (class): A declarative base for declaring models.
    
    """
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def save_to_db(self):
        """Writes data to the database"""
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """Deletes data  from the database"""
        db.session.delete(self)
        db.session.commit()


class UserModel(BaseModel):
    """Generates users table"""
    __tablename__ = 'Users'
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    @staticmethod
    def generate_hash(password):
        """Generates a password hash from raw password"""
        return pbkdf2_sha256.hash(password)

    @staticmethod
    def verify_hash(password, password_hash):
        """Verifies provided password against hashed password"""
        return pbkdf2_sha256.verify(password, password_hash)


class ProjectModel(BaseModel):
    """ Generates projects table"""
    __tablename__ = 'Project'
    name = db.Column(db.String(128), nullable=False)
    device_uuid = db.Column(db.String(128), nullable=False)
    devices = db.relationship('DeviceModel', backref='project', lazy=True)

    def __repr__(self):
        return '<name: {} >'.format(self.name)


class DeviceModel(BaseModel):
    """ Generates device table"""
    __tablename__ = 'Devices'
    name = db.Column(db.String(128), nullable=False)
    device_uuid = db.Column(db.String(128), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('Project.id'), nullable=False)

    def __repr__(self):
        return '<name: {} >'.format(self.name)


class BlacklistedTokens(BaseModel):
    """Generates table for blacklisted auth tokens"""
    __tablename__ = 'JWT_Blacklist'
    token = db.Column(db.String(500), nullable=False, unique=True)

    def __repr__(self):
        return '<id: token: {} >'.format(self.token)

    @staticmethod
    def check_blacklisted_token(auth_token):
        check = BlacklistedTokens.query.filter_by(token=str(auth_token)).first()

        if check:
            return True
        else:
            return False
