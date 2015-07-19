from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index_page():
    # Return this as a strange
    return '<html><body>This is the homepage.</body></html>'

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route('/application', methods=['POST'])
def application():
	first_name = request.form.get('first')
	last_name = request.form.get('last')
	job_title = request.form.get('job')
	salary_req = request.form.get('salary')


	return render_template('templates/response.html', 
        first=first_name, 
        last=last_name, 
        job=job_title, 
        salary=salary_req)

if __name__ == "__main__":
    app.run(debug=True)