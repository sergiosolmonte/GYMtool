from flask import render_template, redirect, flash, url_for, json, make_response
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import logout_user, current_user, login_user, login_required
from app.models import User, Exercise, Category, Training, Program, Interest,UserInterest
from flask import request
from flask import jsonify, json
from json import dumps
from datetime import datetime


def calculate_age(born):
    today = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():

    return render_template('index.html')


@app.route('/test', methods=['GET', 'POST'])
# @login_required
def test():
    if request.method == "POST":
        result = request.get_json(force=True)
        print(result[0]['title'])

        for i in range(1, len(result)):
            ex_id = result[i]['exercise']
            set = result[i]['set']
            rep = result[i]['rep']
            time = result[i]['time']
            day = result[i]['day']
            exNum = result[i]['exNum']
            print(ex_id, set, rep, time, day, exNum)

        print("User id:" + str(current_user.id))

        program = Program(user_id=current_user.id, share=True, name=result[0]['title'])
        db.session.add(program)
        db.session.flush()

        print("program id: " + str(program.id) + " user id: " + str(program.user_id)+ "program name: "+program.name)

        print(len(result))

        for i in range(1, len(result)):
            ex_id = result[i]['exercise']
            set = result[i]['set']
            rep = result[i]['rep']
            time = result[i]['time']
            day = result[i]['day']
            exNum = result[i]['exNum']
            train = Training(exercise_id=ex_id, program_id=program.id, set=set,
                             reps=rep, time=time, day=day, exNum=exNum)
            db.session.add(train)
            db.session.flush()
            # db.session.commit()
            print("exercise_id: " + str(train.exercise_id) + "program_id: " + str(train.program_id) + " set: " + str(
                train.set) + " reps: " + train.reps + " time: " + train.time + " day: " + str(
                train.day) + " exNum: " + str(
                train.exNum))

        db.session.commit()

        print("train id: " + str(train.id))


        return jsonify({'text': 'Salvataggio Effettuato'})


@app.route('/editor', methods=['GET','POST'])
@login_required
def editor():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    exercise = Exercise.query.all()
    category = Category.query.all()
    join = db.session.query(Category, Exercise).join(Exercise, Exercise.category == Category.id)

    return render_template('editor.html', exercise=exercise, category=category, join=join)


@app.route('/gruppiMuscolari', methods=['GET', 'POST'])
@login_required
def gruppiMuscolari():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    if request.method == 'POST':
        id = request.get_data().decode("utf-8").strip()
        descr = Exercise.query.filter_by(id=""+id).all()
        return make_response(dumps(descr[0].description))

    exercise = Exercise.query.all()
    category = Category.query.all()
    join = db.session.query(Category, Exercise).join(Exercise, Exercise.category == Category.id)

    return render_template('gruppiMuscolari.html', exercise=exercise, category=category, join=join)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('profile', username=user.username))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, username=form.username.data,
                    email=form.email.data, birthdate=form.birthdate.data)
        user.set_password(form.password.data)
        print("Name: " + user.firstname + " Lastname: " + user.lastname + " Username: " + user.username + " Email: "
              + user.email + " Data di Nascita: " + str(user.birthdate))
        db.session.add(user)
        db.session.commit()
        print('Congratulations, you are now a registered user!')
        return redirect(url_for('login', user=user))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html',title='User', user=user)


@app.route('/user/<username>/profile', methods=['GET', 'POST'])
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    join = UserInterest.query.join(Interest).filter(UserInterest.user_id == user.id).with_entities(Interest.name)

    return render_template('profile.html', user=user, join=join)



@app.route('/user/<username>/archivio/viewProgram/<program_id>', methods=['GET','POST'])
@login_required
def viewProgram(username, program_id):
    print("username"+username,program_id)
    p = Program.query.filter_by(id=program_id).all()
    program = p[0]
    qry = None
    if request.method == "POST":
        result = request.get_data().decode("utf-8").strip()
        # print(result)
        prog_id = result
        qry = Training.query.join(Exercise)\
            .filter(Training.program_id == prog_id)\
            .with_entities(Exercise.name, Training.set, Training.reps, Training.time, Training.day, Training.exNum).all()
        array_query = []
        for j in qry:
            json_array = {
                'name': j.name,
                'set': j.set,
                'rep': j.reps,
                'time': j.time,
                'exNum': j.exNum,
                'day': j.day
            }
            array_query.append(json_array)

        return make_response(dumps(array_query))

    return render_template('viewProgram.html', user=user, program_id=program_id, program=program, query=qry)



@app.route('/user/<username>/archivio', methods=['GET','POST'])
@login_required
def archivio(username):
    user = User.query.filter_by(username=username).first_or_404()
    programs = Program.query.filter_by(user_id=user.id)


    return render_template('archivio.html', user=user, programs=programs)


@app.route('/user/<username>/tool', methods=['GET','POST'])
@login_required
def tool(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('tool.html', user=user)


@app.route('/user/<username>/messaggi')
@login_required
def messaggi(username):
    user = current_user
    return render_template('messaggi.html', user=user)


@app.route('/user/<username>/tool/bmiApp',methods=['GET','POST'])
@login_required
def bmiApp(username):
    user = User.query.filter_by(username=username).first_or_404()
    age = calculate_age(user.birthdate)
    print(age)
    return render_template('bmi.html', user=user, age=age)


@app.route('/user/<username>/tool/idealWeight',methods=['GET','POST'])
@login_required
def idealWeight(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('idealWeight.html', user=user)


@app.route('/user/<username>/tool/macros',methods=['GET','POST'])
@login_required
def macros(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('macros.html', user=user)


@app.route('/user/<username>/tool/body-fat',methods=['GET','POST'])
@login_required
def bodyfat(username):
    user = User.query.filter_by(username=username).first_or_404()
    age = calculate_age(user.birthdate)
    return render_template('bodyfat.html', user=user, age=age)


@app.route('/user/<username>/tool/kcal', methods=['GET','POST'])
@login_required
def kcal(username):
    user = User.query.filter_by(username=username).first_or_404()
    age = calculate_age(user.birthdate)
    return render_template('kcal.html', user=user, age=age)


@app.route('/user/<username>/editProfile', methods=['GET','POST'])
def editProfile(username):
    if request.method == "POST":
        res = request.get_json(force=True)


        user = User.query.filter_by(username=username).first_or_404()

        if res['firstname'] != "":
            user.firstname = res['firstname']
        if res['lastname'] != "":
            user.lastname = res['lastname']
        if res['birthdate'] != "":
            print(res['birthdate'])
            string = res['birthdate']
            fmt = '%Y-%m-%d %H:%M:%S'
            date = datetime.strptime(string, fmt)
            user.birthdate = date
        if res['weight'] != "":
            user.weight = res['weight']
        if res['height'] != "":
            user.height = res['height']
        if res['waist'] != "":
            user.waist = res['waist']
        if res['neck'] != "":
            user.neck = res['neck']

        db.session.add(user)
        db.session.commit()

        return make_response(dumps(res))

