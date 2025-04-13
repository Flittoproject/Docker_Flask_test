import pandas as pd
from app import create_app
from app.db import db
from app.models import Applicant

app = create_app()
app.app_context().push()

df = pd.read_csv("data/response1.csv")

df = df.fillna('')  # NaN → 빈 문자열로 변환

for _, row in df.iterrows():
    applicant = Applicant(
        timestamp=row.iloc[0] if len(row) > 0 else '',
        full_name=row.iloc[1] if len(row) > 1 else '',
        email=row.iloc[2] if len(row) > 2 else '',
        platform=row.iloc[3] if len(row) > 3 else '',
        native_language=row.iloc[4] if len(row) > 4 else '',
        origin=row.iloc[5] if len(row) > 5 else '',
        language_pairs=row.iloc[6] if len(row) > 6 else '',
        has_advanced_degree=row.iloc[7] if len(row) > 7 else '',
        education_level=row.iloc[8] if len(row) > 8 else '',
        major=row.iloc[9] if len(row) > 9 else '',
        academic_field=row.iloc[10] if len(row) > 10 else '',
        language_proof=row.iloc[11] if len(row) > 11 else '',
        certificate_path=row.iloc[12] if len(row) > 12 else '',
        experience=row.iloc[13] if len(row) > 13 else '',
        domains=row.iloc[14] if len(row) > 14 else '',
        weekly_capacity=row.iloc[15] if len(row) > 15 else '',
        extra1=row.iloc[16] if len(row) > 16 else '',
        extra2=row.iloc[17] if len(row) > 17 else '',
        extra3=row.iloc[18] if len(row) > 18 else '',
        extra4=row.iloc[19] if len(row) > 19 else ''
    )
    db.session.add(applicant)

db.session.commit()
print("✅ CSV data successfully loaded.")
