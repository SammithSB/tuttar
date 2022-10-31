# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request, redirect

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template(template_name_or_list='index.html')


@app.route('/cloud', methods=['GET', 'POST'])
def cloud():
    if request.method == 'POST':
        user_name = request.form['user_name']
        return render_template(template_name_or_list='cloud.html', user_name=user_name)
    else:
        return redirect('/')


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
