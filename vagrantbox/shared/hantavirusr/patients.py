from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from hantavirusr.auth import login_required
from hantavirusr.db import get_db

bp = Blueprint('patients', __name__)

# Index:
@bp.route('/')
@login_required
def index():
    db = get_db()
    patients = db.execute('SELECT * FROM Patients ORDER BY Date_of_Admission DESC').fetchall()
    return render_template('auth/login.html', patients=patients)


# Create:
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age = request.form['age']
        date_of_admission = request.form['date_of_admission']
        infection_status = request.form['infection_status']
        error = None

        if not firstname or not lastname:
            error = 'Patient name fields are required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO Patients (Firstname, Lastname, Age, Date_of_Admission, Infection_Status)'
                ' VALUES (?, ?, ?, ?, ?)',
                (firstname, lastname, age, date_of_admission, infection_status)
            )
            db.commit()
            return redirect(url_for('patients.index'))

    return render_template('patients/create.html')


def get_patient(id):
    patient = get_db().execute(
        'SELECT id, Firstname, Lastname, Age, Date_of_Admission, Infection_Status'
        ' FROM Patients'
        ' WHERE id = ?',
        (id,)
    ).fetchone()

    if patient is None:
        abort(404, f"Patient id {id} doesn't exist.")

    return patient


@bp.route('/')
def home():
    return render_template('base.html')

# Update:
@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    patient = get_patient(id)

    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age = request.form['age']
        date_of_admission = request.form['date_of_admission']
        infection_status = request.form['infection_status']
        error = None

        if not firstname or not lastname:
            error = 'Patient name fields are required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE Patients SET Firstname = ?, Lastname = ?, Age = ?, Date_of_Admission = ?, Infection_Status = ?'
                ' WHERE id = ?',
                (firstname, lastname, age, date_of_admission, infection_status, id)
            )
            db.commit()
            return redirect(url_for('patients.index'))

    return render_template('patients/update.html', patient=patient)


# Delete:
@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_patient(id) 
    db = get_db()
    db.execute('DELETE FROM Patients WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('patients.index'))