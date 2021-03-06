from flask import Flask, render_template, request, url_for, redirect

import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors')
def mentors_list():
    mentor_name = request.args.get('mentor-last-name')
    city = request.args.get('city-name')

    cities = data_manager.get_citites()
    if mentor_name:
        mentor_details = data_manager.get_mentors_by_last_name(mentor_name)
    elif city:
        mentor_details = data_manager.get_mentors_by_city(city)
    else:
        mentor_details = data_manager.get_mentors()

    # We get back a list of dictionaries from the data_manager (for details check 'data_manager.py')

    return render_template('mentors.html', mentors=mentor_details, cities=cities)

@app.route('/applicants-phone')
def applicants_phone():
    applicant_name = request.args.get('applicant-name')
    applicant_details = data_manager.get_applicant_data_by_name(applicant_name)
    return render_template('phone.html', applicants=applicant_details, name=applicant_name)

if __name__ == '__main__':
    app.run(debug=True)
