from flask import render_template, request, redirect, url_for
from app import app
from datetime import datetime

# In-memory database
subjects_db = []
schedules_db = []

class Subject:
    def __init__(self, name, priority):
        self.id = len(subjects_db) + 1
        self.name = name
        self.priority = priority

class Schedule:
    def __init__(self, subject_id, date, time, duration):
        self.id = len(schedules_db) + 1
        self.subject_id = subject_id
        self.date = date
        self.time = time
        self.duration = duration
        self.created_at = datetime.now()

    def get_subject(self):
        return next((s for s in subjects_db if s.id == self.subject_id), None)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html', subjects=subjects_db, schedules=schedules_db)

@app.route('/subjects')
def subjects():
    return render_template('subjects.html', subjects=subjects_db)

@app.route('/add_subject', methods=['GET', 'POST'])
def add_subject():
    if request.method == 'POST':
        subject_name = request.form.get('subject_name')
        priority = request.form.get('priority')
        
        # Create and save new subject
        new_subject = Subject(subject_name, priority)
        subjects_db.append(new_subject)
        
        return redirect(url_for('subjects'))
    return render_template('subjects.html', subjects=subjects_db)

@app.route('/add_schedule', methods=['POST'])
def add_schedule():
    if request.method == 'POST':
        subject_id = int(request.form.get('subject'))
        date = request.form.get('date')
        time = request.form.get('time')
        duration = int(request.form.get('duration'))

        new_schedule = Schedule(subject_id, date, time, duration)
        schedules_db.append(new_schedule)

        return redirect(url_for('schedule'))