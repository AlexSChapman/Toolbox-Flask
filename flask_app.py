from flask import Flask
from flask import request
from flask import render_template
from flask import redirect

app = Flask(__name__)
students = ['kian raissan', 'peter seger', 'nathan lepore', 'sean szymanski',
            'alex chapman', 'anil patel', 'aurora bunten']


@app.route('/')
def my_form():
    return render_template("welcome_page.html")


@app.route('/login', methods=['POST'])
def my_form_post():
    full_name = request.form['fullname']
    age = request.form['age']
    ninja = request.form['ninja']
    if '' in[full_name, age, ninja]:
        return render_template("error.html")
    elif full_name.lower() in students:
        print('Fullname:', full_name)
        print('Age:', age)
        print('Ninja:', ninja)
        return 'Full Name:'+full_name+'\n'+'Age:'+age+'\n'+'Favorite Ninja:'+'Patrick Huston'
    else:
        return render_template("error.html")


def go_to_FB():
    return redirect("https://www.facebook.com/phuston2", code=302)


if __name__ == '__main__':
    app.run()
