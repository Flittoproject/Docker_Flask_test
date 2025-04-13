from .db import db

class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String)
    full_name = db.Column(db.String)
    email = db.Column(db.String)
    platform = db.Column(db.String)
    native_language = db.Column(db.String)
    origin = db.Column(db.String)
    language_pairs = db.Column(db.String)
    has_advanced_degree = db.Column(db.String)
    education_level = db.Column(db.String)
    major = db.Column(db.String)
    academic_field = db.Column(db.String)
    language_proof = db.Column(db.String)
    certificate_path = db.Column(db.String)
    experience = db.Column(db.String)
    domains = db.Column(db.String)
    weekly_capacity = db.Column(db.String)
    extra1 = db.Column(db.String)  # 열 17
    extra2 = db.Column(db.String)  # 열 18
    extra3 = db.Column(db.String)  # 열 19
    extra4 = db.Column(db.String)  # 열 20

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String)
    language_pairs = db.Column(db.String)