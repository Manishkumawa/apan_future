from flask import Flask ,render_template,jsonify ,request
from jinja2 import Environment ,FileSystemLoader
app = Flask(__name__)
from database import *

def intcomma(value):
    return format(value ,',')

env = Environment(loader=FileSystemLoader('templates'))
env.filters['intcomma'] = intcomma
app.jinja_env = env

JOBS = load_jobs()
@app.route("/")
def index():
    JOBS = load_jobs()

    return render_template('home.html',jobs = JOBS)


@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

@app.route('/job/<int:id>')
def show_job(id):
    job = load_job_id(id)

    if not job:
        return 'Not found',404

    return render_template('jobpage.html', job =job)

@app.route("/job/<int:id>/apply",methods =['POST'])
def apply_to_job(id):

    job = load_job_id(id)

    data = request.form
    add_application_to_db(id ,data)

    return render_template('application_submit.html',application = data ,job = job )





if __name__ =="__main__":
    app.run(debug =True)