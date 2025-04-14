from flask import Blueprint, request, redirect, render_template
from .models import Applicant, Test
from .db import db


bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_ids = request.form.getlist('selected')

        for applicant_id in selected_ids:
            applicant = Applicant.query.get(int(applicant_id))
            if applicant:
                test_entry = Test(
                    full_name=applicant.full_name,
                    language_pairs=applicant.language_pairs
                )
                db.session.add(test_entry)

        db.session.commit()
        return redirect('/')

    applicants = Applicant.query.all()
    return render_template('index.html', applicants=applicants)
