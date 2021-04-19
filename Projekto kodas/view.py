#!/usr/bin/env python3
import os

import numpy
from flask import Flask, render_template, flash, redirect, url_for, session, request, send_from_directory
from passlib.hash import sha256_crypt
from functools import wraps
import pyperclip
import numpy as np

from flask import Flask, request, render_template, url_for, redirect
from werkzeug.utils import secure_filename
from wtforms import Form, StringField, PasswordField, validators, SelectField, BooleanField
import pandas as pd

from controller import check_login, new_company, check_level, new_employee, check_employees, \
    check_level_person, \
    get_profile_info, get_profile_info_team, get_questions, check_category, check_company_email, \
    get_all_questions, check_login_person, check_login_person_details, check_employees_of_the_team, new_questionaire, \
    check_for_questionaires, check_for_questionaires_all, update_questionaire, check_for_questionaires_manager, \
    check_for_questionaires_manager_detail, update_questionaire_manager, check_for_questionaires_manager_results, \
    check_for_questionaires_e_results, check_for_questionaires_employee_detail, feedback_history, m_feedback_history, \
    check_company_name, check_password_try, change_password_try, check_password_try2, change_password_try2, \
    get_profile_info_admin, change_company_profile, change_employees_company_email, change_company_profile_password,  \
    check_email, change_e_email, change_m_email, check_email_for_manager, check_employees_of_manager, check_if_manager, \
    change_e_m_email, delete_employee, change_employee_profile_password, get_manager_profile_info, check_employees2


ALLOWED_EXTENSIONS = set(['xlsx'])

class RegisterForm(Form):
    company_name = StringField(str('Kompanijos pavadinimas').strip(), [
        validators.Length(min=1, max=250, message='Kompanijos pavadinimas turi susidaryti iš 1-250 simbolių.'),
    ])

    email = StringField('El. paštas', [
        validators.Length(min=1, message='El. paštas yra privalomas laukas. '),
        validators.Length(min=6, max=250,  message='El. pašto adresas turi susidaryti iš 6-50 simbolių. '),
        validators.email( message='El. pašto adresas neatitinka reikiamos struktūros')
    ])
    password = PasswordField('Slaptažodis', [
        validators.Length(min=6, max=50, message='Slaptažodis turi susidaryti iš bent 6 simbolių. '),
        validators.EqualTo('confirm', message='Slaptažodžiai nesutampa.')
    ])
    confirm = PasswordField('Pakartokite slaptažodį', [
        validators.Length(min=6, max=50, message='Slaptažodis turi susidaryti iš bent 6 simbolių.')
    ])

class AdminProfileForm(Form):
        company_name = StringField(str('Kompanijos pavadinimas').strip(), [
            validators.Length(min=1, max=250, message='Kompanijos pavadinimas turi susidaryti iš 1-250 simbolių.'),
        ])

        email = StringField('El. paštas', [
            validators.Length(min=1, message='El. paštas yra privalomas laukas. '),
            validators.Length(min=6, max=250, message='El. pašto adresas turi susidaryti iš 6-50 simbolių. '),
            validators.email(message='El. pašto adresas neatitinka reikiamos struktūros')
        ])


class EmployeeProfileForm(Form):
    first_name = StringField(str('Vardas').strip(), [
        validators.Length(min=1, max=60, message='Vardas turi susidaryti iš 1-60 simbolių.'),
    ])
    last_name = StringField(str('Pavardė').strip(), [
        validators.Length(min=1, max=60, message='Pavardė turi susidaryti iš 1-60 simbolių.'),
    ])

    email = StringField('El. paštas', [
        validators.Length(min=1, message='El. paštas yra privalomas laukas. '),
        validators.Length(min=6, max=250, message='El. pašto adresas turi susidaryti iš 6-50 simbolių. '),
        validators.email(message='El. pašto adresas neatitinka reikiamos struktūros')
    ])
    team = StringField(str('Komanda').strip(), [
        validators.Length(min=1, max=60, message='Komandos pavadinimas turi susidaryti iš 1-60 simbolių.'),
    ])
    manager_email = StringField(str('Vadovo el.paštas').strip(), [
        validators.Length(min=1, message='El. paštas yra privalomas laukas. '),
        validators.Length(min=4, max=250, message='El. pašto adresas turi susidaryti iš 6-50 simbolių. '),
    ])
    start_date = StringField(str('Regitracijos data').strip(), [
        validators.Length(min=1, max=250, message='Registracijos data turi atitikti datos formatą'),
    ])
    end_date = StringField(str('Pabaigos data').strip(), [
    ])


class AdminPasswordForm(Form):
    password = PasswordField(str('Dabartinis slaptažodis').strip(), [
        validators.Length(min=1, message='Dabartinis slaptažodis yra neužpildytas. '),
        validators.Length(min=6, max=50, message='Slaptažodis turi susidaryti iš bent 6 simbolių.')
    ])

    newpassword1 = PasswordField('Naujas slaptažodis', [
        validators.Length(min=1, message='Naujas slaptažodis laukas yra neužpildytas.  '),
        validators.Length(min=6, max=50, message='Slaptažodis turi susidaryti iš bent 6 simbolių.')
    ])

    newpassword2 = PasswordField('Pakartokite naują slaptažodį', [
        validators.Length(min=1, message='Pakartokite naują slaptažodį laukas yra neužpildytas. '),
        validators.Length(min=6, max=50, message='Slaptažodis turi susidaryti iš bent 6 simbolių.')
    ])
class QuestionaireForm(Form):
    colleague = StringField('')
    manager = StringField('')

class QuestionForm(Form):
    trial_true = 0



class QuestionsForm(Form):

    category = StringField('Category', [validators.Length(min=4, max=50)])
    question_from_category = StringField('Question', [validators.Length(min=4, max=500)])



def home():

    return render_template(
        'home.html'
        )



def testimonials():

    return render_template(
        'testimonials.html'
        )

def contact():

    return render_template(
        'contact.html'
        )


def register():
    form = RegisterForm(request.form)
    company_name = form.company_name.data.strip()

    # print(form.validate())
    if request.method == 'POST':
        if company_name == "":
            print("kompanijos vardas:" + company_name)
            error = 'Kompanijos pavadinimas yra privalomas laukas.'
            return render_template('register.html', error=error, form=form)
        else:
            check = check_company_name(company_name)
            #print(check)
            if check:
                error = 'Kompanija su tokiu pavadinimu jau yra užregistruota.'
                return render_template('register.html', error=error, form=form)
    if request.method == 'POST' and form.validate():
        company_name = form.company_name.data.strip()
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))
        result = check_login(email)
        if result != -1:
            error = 'Toks el. paštas jau yra naudojamas.'
            return render_template('register.html', error=error, form=form)
        else:
            new_company(company_name, email, password)
        flash('Užsiregistravote, galite prisijungti', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Prašome prisijungti', 'danger')
            return redirect(url_for('login'))
    return wrap

@is_logged_in
def logout():
    session.clear()
    flash('Sėkmingai atsijungėte', 'success')
    return redirect(url_for('login'))

@is_logged_in
def logout_update():
    session.clear()
    flash('Sėkmingai atnaujinta informacija, prisijunkite iš naujo', 'success')
    return redirect(url_for('login'))

@is_logged_in
def logout_update_password():
    session.clear()
    flash('Slaptažodis sėkmingai pakeistas, prisijunkite iš naujo', 'success')
    return redirect(url_for('login'))

@is_logged_in
def my_home():
    return render_template('my_home.html')

@is_logged_in
def manager_home():
    return render_template('m_home.html')

@is_logged_in
def m_manage_team():
    user = get_profile_info_team(session['username'])
    if user != '()':
        return render_template('m_manage_team.html', users=user)
    else:
        msg = 'Nerasta vartototojo'
        return render_template('m_manage_team.html', msg=msg)

@is_logged_in
def chat():
    questionaire_data = feedback_history(session['username'])
    return render_template('chat.html', qd=questionaire_data)


@is_logged_in
def my_profile():
    user = get_profile_info(session['username'])
    if user != '()':
        return render_template('my_profile.html', users=user)
    else:
        msg = 'Nerasta vartototojo'
        return render_template('my_profile.html', msg=msg)

@is_logged_in
def admin_profile():
    form = AdminProfileForm(request.form)
    user = get_profile_info_admin(session['username'])
    if request.method == 'GET':
        form.company_name.data = user[0]['company_name']
        form.email.data = user[0]['email']
    if request.method == 'POST':
        company_name = form.company_name.data.strip()
        if company_name == "":
            error = 'Kompanijos pavadinimas yra privalomas laukas.'
            return render_template('admin_profile.html',users=user, error=error, form=form)
        else:
            check = check_company_name(company_name)

            if check:
                if check['company_name']==user[0]['company_name']:
                    form.validate()
                else:
                    error = 'Kompanija su tokiu pavadinimu jau yra užregistruota'
                    return render_template('admin_profile.html', error=error, users=user, form=form)
    if request.method == 'POST' and form.validate():
        company_name = form.company_name.data.strip()
        email = form.email.data
        result =  get_profile_info_admin(email)
        if result:
            if result[0]['email'] == user[0]['email']:
                change_company_profile(company_name, user[0]['email'], email)
            else:
                error = 'Toks el. paštas jau yra naudojamas.'
                return render_template('admin_profile.html', users=user,error=error, form=form)
        else:
            change_company_profile(company_name, user[0]['email'], email)
            change_employees_company_email(user[0]['email'], email)
        if user[0]['company_name'] == company_name and user[0]['email'] == email:
                flash('Duomenys išliko tokie pat', 'success')
                return render_template('admin_profile.html', users=user, form=form)
        else:
                flash('Sėkmingai atnaujinta informacija', 'success')
                logout_update();
                return redirect(url_for('login'))
    if user != '()':
        return render_template('admin_profile.html', users=user, form=form)
    else:
        msg = 'Nerasta vartototojo'
        return render_template('admin_profile.html', msg=msg)


@is_logged_in
def admin_profile_password():
    form = AdminPasswordForm(request.form)
    user = get_profile_info_admin(session['username'])
    if request.method == 'GET':
        print('get metodas')

    if request.method == 'POST':
        password = sha256_crypt.encrypt(str(form.password.data))
        newpassword1 = sha256_crypt.encrypt(str(form.newpassword1.data))
        newpassword2 = sha256_crypt.encrypt(str(form.newpassword2.data))

    if request.method == 'POST' and form.validate():
        print('jau cia2')
        result = get_profile_info_admin(user[0]['email'])

        if sha256_crypt.verify(str(form.password.data), result[0]['password']):
            print('slapžodis atitinka')

            if sha256_crypt.verify(str(form.newpassword2.data), newpassword1):
                if sha256_crypt.verify(str(form.password.data), newpassword1):
                    flash('Naujas slaptažodis negali būti toks pat, kaip dabartinis slaptažodžis', 'danger')
                    return render_template('admin_profile_password.html', users=user, form=form)
                else:
                    change_company_profile_password(user[0]['email'], newpassword1)
                    flash('Slaptažodis sėkmingai pakeistas', 'success')
                    logout_update_password();
                    return redirect(url_for('login'))

            else:
                flash('Slaptažodžiai nesutampa', 'danger')
                return render_template('admin_profile_password.html', users=user, form=form)
        else:
            flash('Slaptažodis įvestas neteisingai', 'danger')
            return render_template('admin_profile_password.html', users=user, form=form)


    if user != '()':
        return render_template('admin_profile_password.html', users=user, form=form)
    else:
        msg = 'Nerasta vartototojo'
        return render_template('admin_profile_password.html', msg=msg)

@is_logged_in
def manager_profile_password():
    form = AdminPasswordForm(request.form)
    user = get_profile_info(session['username'])
    if request.method == 'GET':
        print('get metodas')
    if request.method == 'POST':
        password = sha256_crypt.encrypt(str(form.password.data))
        newpassword1 = sha256_crypt.encrypt(str(form.newpassword1.data))
        newpassword2 = sha256_crypt.encrypt(str(form.newpassword2.data))

    if request.method == 'POST' and form.validate():
        print('jau cia2')
        result = get_profile_info(user[0]['email'])

        if sha256_crypt.verify(str(form.password.data), result[0]['password']):
            print('slapžodis atitinka')

            if sha256_crypt.verify(str(form.newpassword2.data), newpassword1):
                if sha256_crypt.verify(str(form.password.data), newpassword1):
                    flash('Naujas slaptažodis negali būti toks pat, kaip dabartinis slaptažodžis', 'danger')
                    return render_template('manager_profile_password.html', users=user, form=form)
                else:
                    change_employee_profile_password(user[0]['email'], newpassword1)
                    flash('Slaptažodis sėkmingai pakeistas', 'success')
                    logout_update_password();
                    return redirect(url_for('login'))
            else:
                flash('Slaptažodžiai nesutampa', 'danger')
                return render_template('manager_profile_password.html', users=user, form=form)
        else:
            flash('Slaptažodis įvestas neteisingai', 'danger')
            return render_template('manager_profile_password.html', users=user, form=form)
    if user != '()':
        return render_template('manager_profile_password.html', users=user, form=form)
    else:
        msg = 'Nerasta vartototojo'
        return render_template('manager_profile_password.html', msg=msg)

@is_logged_in
def employee_profile_password():
    form = AdminPasswordForm(request.form)
    user = get_profile_info(session['username'])
    print(user)
    if request.method == 'GET':
        print('get metodas')

    if request.method == 'POST':
        password = sha256_crypt.encrypt(str(form.password.data))
        newpassword1 = sha256_crypt.encrypt(str(form.newpassword1.data))
        newpassword2 = sha256_crypt.encrypt(str(form.newpassword2.data))

    if request.method == 'POST' and form.validate():
        print('jau cia2')
        result = get_profile_info(user[0]['email'])

        if sha256_crypt.verify(str(form.password.data), result[0]['password']):
            print('slapžodis atitinka')

            if sha256_crypt.verify(str(form.newpassword2.data), newpassword1):
                if sha256_crypt.verify(str(form.password.data), newpassword1):
                    flash('Naujas slaptažodis negali būti toks pat, kaip dabartinis slaptažodžis', 'danger')
                    return render_template('employee_profile_password.html', users=user, form=form)
                else:
                    change_employee_profile_password(user[0]['email'], newpassword1)
                    flash('Slaptažodis sėkmingai pakeistas', 'success')
                    logout_update_password();
                    return redirect(url_for('login'))

            else:
                flash('Slaptažodžiai nesutampa', 'danger')
                return render_template('employee_profile_password.html', users=user, form=form)
        else:
            flash('Slaptažodis įvestas neteisingai', 'danger')
            return render_template('employee_profile_password.html', users=user, form=form)


    if user != '()':
        return render_template('employee_profile_password.html', users=user, form=form)
    else:
        msg = 'Nerasta vartototojo'
        return render_template('employee_profile_password.html', msg=msg)

@is_logged_in
def manager_profile():
    user = get_profile_info(session['username'])
    print(user)
    if user != '()':
        return render_template('m_profile.html', users=user)
    else:
        msg = 'Nerasta vartotojo'
        return render_template('m_profile.html', msg=msg)

@is_logged_in
def manage_feedback_tool():
    form = QuestionForm(request.form)
    if request.method == 'POST':
        if request.form['submit_button'] == 'Psichologinė sauga':
            questions_1 = get_questions("psichologine sauga")
            return render_template('m_feedback_tool.html', form=form, questions_1=questions_1)
        elif request.form['submit_button'] == 'Patikimumas':
            questions_2 = get_questions("patikimumas")
            return render_template('m_feedback_tool.html', form=form, questions_2=questions_2)
        elif request.form['submit_button'] == 'Struktūra ir aiškumas':
            questions_3 = get_questions("struktura ir aiskumas")
            return render_template('m_feedback_tool.html', form=form, questions_3=questions_3)
        elif request.form['submit_button'] == 'Reikšmė':
            questions_4 = get_questions("reiksme")
            return render_template('m_feedback_tool.html', form=form, questions_4=questions_4)
        elif request.form['submit_button'] == 'Poveikis':
            questions_5 = get_questions("poveikis")
            return render_template('m_feedback_tool.html', form=form, questions_5=questions_5)
        elif request.form['submit_button'] == 'Produktyvumas':
            questions_6 = get_questions("produktyvumas")
            return render_template('m_feedback_tool.html', form=form, questions_6=questions_6)
        elif request.form['submit_button'] == 'Tikslų pasiekimas':
            questions_7 = get_questions("tikslu pasiekimas")

            return render_template('m_feedback_tool.html', form=form, questions_7=questions_7)

        elif request.form['submit_button'] == 'Vadovui':
            questions_9 = get_questions("vadovui")
            return render_template('m_feedback_tool.html', form=form, questions_9=questions_9)

        elif request.form['submit_button'] == 'Išsiųsti anketą savo komandai':

            manager_email = session['username']
            results = check_employees_of_the_team(manager_email)
            if str(results) != "()":
                for r in results:
                    new_questionaire(manager_email, r['email'])
                flash('Anketa sėkmingai išsiųsta', 'success')
                return redirect(url_for('manager_home'))
            if str(results) == "()":
                flash('Anketa neišsiųsta, nes jūsų komandoje nėra nei vieno darbuotojo', 'danger')
                return render_template('m_feedback_tool.html', form=form)
        else:
            return render_template('m_feedback_tool.html', form=form)

    return render_template('m_feedback_tool.html', form=form)


@is_logged_in
def manager_team_results():
    questionaire_data = check_for_questionaires_manager_results(session['username'])
    i = 0
    a1_avg = 0
    a2_avg = 0
    a3_avg = 0
    a4_avg = 0
    a5_avg = 0
    b1_avg = 0
    b2_avg = 0
    b1_m_avg = 0
    b2_m_avg = 0

    for q in questionaire_data:
        i=i+1
        a1_avg = a1_avg + q['question_a1']
        a2_avg = a2_avg + q['question_a2']
        a3_avg = a3_avg + q['question_a3']
        a4_avg = a4_avg + q['question_a4']
        a5_avg = a5_avg + q['question_a5']
        b1_avg = b1_avg + q['question_b1']
        b2_avg = b2_avg + q['question_b2']
        b1_m_avg = b1_m_avg + q['question_m1']
        b2_m_avg = b2_m_avg + q['question_m2']

    if a1_avg!=0:
        a1_avg = round((a1_avg / i),2)
        a2_avg = round((a2_avg / i),2)
        a3_avg = round((a3_avg / i),2)
        a4_avg = round((a4_avg / i),2)
        a5_avg = round((a5_avg / i), 2)
        b1_avg = round((b1_avg / i),2)
        b2_avg = round((b2_avg / i),2)
        b1_m_avg = round((b1_m_avg / i), 2)
        b2_m_avg = round((b2_m_avg / i), 2)
    if a1_avg <=2:
        dimention1 = "Skatinkite visą komandą būti atviresniais ir venkite teisti už klaidas."
    elif a1_avg <=4:
        dimention1 = "Skatinkite pavienius komandos narius būti atviresniais ir venkite teisti už klaidas."
    else:
        dimention1 = ""

    if a2_avg <=2 and a2_avg<3:
        dimention2 = "Suorganizuokite susitikimą, kurio metu mokytumėte apie laiko planavimą."
    elif a2_avg <=4 and a2_avg<5:
        dimention2 = "Kalbėkite su pavieniais komandos nariais apie laiko planavimą."
    else:
        dimention2 = ""

    if a3_avg <=2 and a3_avg<3:
        dimention3 = "Suorganizuokite susitikimą visiems apie darbų paskirstymą ir planus, būkite konkretūs."
    elif a3_avg <=4 and a3_avg<5:
        dimention3 = "Kalbėkite su pavieniais komandos nariais apie darbų struktūrą ir planus."
    else:
        dimention3 = ""

    if a4_avg <=2 and a4_avg<3:
        dimention4 = "Padarykite diskusiją su visais komandos nariais, kurioje visi darbuotojai turi sugalvoti, kuo jiems yra svarbus jų darbas."
    elif a4_avg <=4 and a4_avg<5:
        dimention4 = "Kalbėkite su pavieniais komandos nariais apie tai, kuo jiems svarbus jų darbas."
    else:
        dimention4 = ""

    if a5_avg <=2 and a5_avg<3:
        dimention5 = "Suorganizuokite konferenciją visiems komandos nariams, kurios metu kartu visa kamonda sugavotumėte, kuo komandos darbas prisideda prie visuotinio gėrio."
    elif a5_avg <=4 and a5_avg<5:
        dimention5 = "Kalbėkite su pavieniais komandos nariais apie tai, kuo komandos darbas prisideda prie visuotinio gėrio."
    else:
        dimention5 = ""
    manager_email = session['username']
    results = check_employees_of_the_team(manager_email)
    if str(results) == '()':
        flash('Rezultatų nėra, nes jūs esat vienintelis darbuotojas komandoje', 'danger')
        return render_template('m_team_results.html')
    else:
        if str(questionaire_data) == '()':
            flash('Rezultatų nėra, nes nei viena anketa nėra pilnai užpildyta', 'danger')
            return render_template('m_team_results.html')

    print(dimention1)
    return render_template('m_team_results.html', qd=questionaire_data,a1_avg=a1_avg,a2_avg=a2_avg,a3_avg=a3_avg,a4_avg=a4_avg,a5_avg=a5_avg,b1_avg=b1_avg,b2_avg=b2_avg, b1_m_avg=b1_m_avg,b2_m_avg=b2_m_avg, d1=dimention1, d2=dimention2, d3=dimention3, d4=dimention4, d5=dimention5)


@is_logged_in
def admin_results():
    questionaire_data = get_manager_profile_info(session['username'])
    i = 0
    a1_avg = 0
    a2_avg = 0
    a3_avg = 0
    a4_avg = 0
    a5_avg = 0
    b1_avg = 0
    b2_avg = 0
    b1_m_avg = 0
    b2_m_avg = 0


    for q in questionaire_data:
        i = i + 1
        a1_avg = a1_avg + q['question_a1']
        a2_avg = a2_avg + q['question_a2']
        a3_avg = a3_avg + q['question_a3']
        a4_avg = a4_avg + q['question_a4']
        a5_avg = a5_avg + q['question_a5']
        b1_avg = b1_avg + q['question_b1']
        b2_avg = b2_avg + q['question_b2']
        b1_m_avg = b1_m_avg + q['question_m1']
        b2_m_avg = b2_m_avg + q['question_m2']

    if a1_avg != 0:
        a1_avg = round((a1_avg / i), 2)
        a2_avg = round((a2_avg / i), 2)
        a3_avg = round((a3_avg / i), 2)
        a4_avg = round((a4_avg / i), 2)
        a5_avg = round((a5_avg / i), 2)
        b1_avg = round((b1_avg / i), 2)
        b2_avg = round((b2_avg / i), 2)
        b1_m_avg = round((b1_m_avg / i), 2)
        b2_m_avg = round((b2_m_avg / i), 2)
    if a1_avg <=2:
        dimention1 = "Skatinkite visus vadovus būti atviresniais ir mažaiu teisiančiais už darbuotojų klaidas."
    elif a1_avg <=4:
        dimention1 = "Skatinkite pavienius vadovus būti atviresniais ir mažaiu teisiančiais už darbuotojų klaidas."
    else:
        dimention1 = ""

    if a2_avg <=2 and a2_avg<3:
        dimention2 = "Suorganizuokite susitikimą, kurio metu mokytumėte visus vadovus apie laiko planavimą."
    elif a2_avg <=4 and a2_avg<5:
        dimention2 = "Kalbėkite su pavieniais vadovais apie laiko planavimą."
    else:
        dimention2 = ""

    if a3_avg <=2 and a3_avg<3:
        dimention3 = "Suorganizuokite susitikimą visiems vadovams apie darbų paskirstymą ir planus, būkite konkretūs."
    elif a3_avg <=4 and a3_avg<5:
        dimention3 = "Kalbėkite su pavieniais vadovais apie darbų struktūrą ir planus."
    else:
        dimention3 = ""

    if a4_avg <=2 and a4_avg<3:
        dimention4 = "Padarykite diskusiją su visais vadovais, kurioje jie turi sugalvoti, kuo jiems yra svarbus jų komandosdarbas."
    elif a4_avg <=4 and a4_avg<5:
        dimention4 = "Kalbėkite su pavieniais vadovais apie tai, kuo jiems svarbus jų komandos darbas."
    else:
        dimention4 = ""

    if a5_avg <=2 and a5_avg<3:
        dimention5 = "Suorganizuokite konferenciją visiems vadovams, kurios metu kartu sugavotumėte, kuo komandų darbas prisideda prie visuotinio gėrio."
    elif a5_avg <=4 and a5_avg<5:
        dimention5 = "Kalbėkite su pavieniais vadovais apie tai, kuo jų komandų darbas prisideda prie visuotinio gėrio."
    else:
        dimention5 = ""


    print(dimention1)
    print()
    return render_template('admin_results.html', qd=questionaire_data,a1_avg=a1_avg,a2_avg=a2_avg,a3_avg=a3_avg,a4_avg=a4_avg,a5_avg=a5_avg,b1_avg=b1_avg,b2_avg=b2_avg, b1_m_avg=b1_m_avg,b2_m_avg=b2_m_avg, d1=dimention1, d2=dimention2, d3=dimention3, d4=dimention4, d5=dimention5)

@is_logged_in
def manager_questionaire():
    questionaire_data = check_for_questionaires_manager_results(session['username'])
    i = 0
    a1_avg = 0
    a2_avg = 0
    a3_avg = 0
    a4_avg = 0
    a5_avg = 0
    b1_avg = 0
    b2_avg = 0
    b1_m_avg = 0
    b2_m_avg = 0
    name=""
    date=""
    id = request.args.get('id')
    print(id)

    for q in questionaire_data:
        i=i+1
        print(q['id'])
        if str(q['id']) == str(id):

            a1_avg = a1_avg + q['question_a1']
            a2_avg = a2_avg + q['question_a2']
            a3_avg = a3_avg + q['question_a3']
            a4_avg = a4_avg + q['question_a4']
            a5_avg = a5_avg + q['question_a5']
            b1_avg = b1_avg + q['question_b1']
            b2_avg = b2_avg + q['question_b2']
            b1_m_avg = b1_m_avg + q['question_m1']
            b2_m_avg = b2_m_avg + q['question_m2']
            feedback_e = q['question_c2']
            feedback_m = q['question_m3']
            name=q['employee_email']
            date=q['start_date']

    if a1_avg <=4:
        dimention1 = "Skatinkite darbuotoją būti atviresniu ir venkite teisti už klaidas."
    else:
        dimention1 = ""

    if a2_avg <=4:
        dimention2 = "Kalbėkite su darbuotoju apie laiko planavimą."
    else:
        dimention2 = ""

    if a3_avg <=4:
        dimention3 = "Kalbėkite su darbuotoju apie darbų struktūrą ir planus."
    else:
        dimention3 = ""

    if a4_avg <=4:
        dimention4 = "Kalbėkite su darbuotoju apie tai, kuo jam/jai svarbus jo/jos darbas."
    else:
        dimention4 = ""

    if a5_avg <=4:
        dimention5 = "Kalbėkite su darbuotoju apie tai, kuo jo/jos darbas prisideda prie visuotinio gėrio."
    else:
        dimention5 = ""


    return render_template('m_questionaire.html', name=name,date=date,qd=questionaire_data,a1_avg=a1_avg,a2_avg=a2_avg,a3_avg=a3_avg,a4_avg=a4_avg,a5_avg=a5_avg,b1_avg=b1_avg,b2_avg=b2_avg, b1_m_avg=b1_m_avg,b2_m_avg=b2_m_avg, f1=feedback_e, f2=feedback_m,  d1=dimention1, d2=dimention2, d3=dimention3, d4=dimention4, d5=dimention5)


@is_logged_in
def admin_questionaire():
    questionaire_data = get_manager_profile_info(session['username'])
    i = 0
    a1_avg = 0
    a2_avg = 0
    a3_avg = 0
    a4_avg = 0
    a5_avg = 0
    b1_avg = 0
    b2_avg = 0
    b1_m_avg = 0
    b2_m_avg = 0
    name=""
    date=""
    id = request.args.get('id')
    print(id)

    for q in questionaire_data:
        i=i+1
        print(q['id'])
        if str(q['id']) == str(id):

            a1_avg = a1_avg + q['question_a1']
            a2_avg = a2_avg + q['question_a2']
            a3_avg = a3_avg + q['question_a3']
            a4_avg = a4_avg + q['question_a4']
            a5_avg = a5_avg + q['question_a5']
            b1_avg = b1_avg + q['question_b1']
            b2_avg = b2_avg + q['question_b2']
            b1_m_avg = b1_m_avg + q['question_m1']
            b2_m_avg = b2_m_avg + q['question_m2']
            feedback_e = q['question_c2']
            feedback_m = q['question_m3']
            name=q['employee_email']
            date=q['start_date']

    if a1_avg <=4:
        dimention1 = "Skatinkite vadovą buti atviresniais ir mažiau kaltinančiais už darbuotojų klaidas."
    else:
        dimention1 = ""

    if a2_avg <=4:
        dimention2 = "Kalbėkite su vadovu apie laiko planavimą."
    else:
        dimention2 = ""

    if a3_avg <=4:
        dimention3 = "Kalbėkite su vadovu apie būdus, kaip pagerinti darbų struktūrą ir planus."
    else:
        dimention3 = ""

    if a4_avg <=4:
        dimention4 = "Kalbėkite su vadovu apie tai, kuo jiems svarbus jų darbas."
    else:
        dimention4 = ""

    if a5_avg <=4:
        dimention5 = "Kalbėkite su vadovu apie tai, kuo jo/jos komandos darbas prisideda prie visuotinio gėrio."
    else:
        dimention5 = ""


    return render_template('a_questionaire.html', name=name,date=date,qd=questionaire_data,a1_avg=a1_avg,a2_avg=a2_avg,a3_avg=a3_avg,a4_avg=a4_avg,a5_avg=a5_avg,b1_avg=b1_avg,b2_avg=b2_avg, b1_m_avg=b1_m_avg,b2_m_avg=b2_m_avg, f1=feedback_e, f2=feedback_m,  d1=dimention1, d2=dimention2, d3=dimention3, d4=dimention4, d5=dimention5)


@is_logged_in
def employee_questionaire():
    questionaire_data = check_for_questionaires_e_results(session['username'])
    i = 0
    b1_avg = 0
    b2_avg = 0
    b1_m_avg = 0
    b2_m_avg = 0
    feedback_e = ""
    feedback_m = ""
    name=""
    date=""
    id = request.args.get('id')

    for q in questionaire_data:
        i=i+1
        if str(q['id']) == str(id):
            b1_avg = b1_avg + q['question_b1']
            b2_avg = b2_avg + q['question_b2']
            b1_m_avg = b1_m_avg + q['question_m1']
            b2_m_avg = b2_m_avg + q['question_m2']
            feedback_e = q['question_c2']
            feedback_m = q['question_m3']
            name=q['employee_email']
            date=q['start_date']

    return render_template('e_questionaire.html', name=name,date=date,qd=questionaire_data,b1_avg=b1_avg,b2_avg=b2_avg, b1_m_avg=b1_m_avg,b2_m_avg=b2_m_avg, f1=feedback_e, f2=feedback_m)


@is_logged_in
def manager_to_do():
    result = check_for_questionaires_manager(session['username'])
    form = QuestionaireForm(request.form)
    if int(result)> 0:
        questionaire_data = check_for_questionaires_manager_detail(session['username'])
        id = questionaire_data[0]['id']
        how_many_to_fill = len(questionaire_data)


        e_email = questionaire_data[0]['employee_email']
        employee = get_profile_info(e_email)

        a1 = questionaire_data[0]['question_a1']
        a2 = questionaire_data[0]['question_a2']
        a3 = questionaire_data[0]['question_a3']
        a4 = questionaire_data[0]['question_a4']
        a5 = questionaire_data[0]['question_a5']
        b1 = questionaire_data[0]['question_b1']
        b2 = questionaire_data[0]['question_b2']
        c2 = questionaire_data[0]['question_c2']
        name = employee[0]['first_name'] + " " + employee[0]['last_name']
        print(e_email)
        if request.method == 'POST' and form.validate():
            print('register2')
            manager = form.manager.data
            m1 = request.form['m1']
            m2 = request.form['m2']
            id =request.form['id']
            if len(manager)>500:
                flash('Atvirame lauke viršytas simbolių limitas', 'danger')
                return render_template('m_to_do.html', form=form, how_many_to_fill=how_many_to_fill, e_email=e_email,
                                       a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, b1=b1, b2=b2, c2=c2, name=name, id=id)
            update_questionaire_manager(m1,m2, manager, id)
            print('register7')
            flash('Anketa sėkmingai užpildyta', 'success')
            return redirect(url_for('manager_home'))
        return render_template('m_to_do.html', form=form, how_many_to_fill=how_many_to_fill, e_email=e_email,
                               a1=a1, a2=a2, a3=a3,a4=a4, a5=a5,b1=b1, b2=b2, c2=c2, name=name, id=id)
    return render_template('m_to_do_no.html')

@is_logged_in
def manager_chat():
    questionaire_data = m_feedback_history(session['username'])
    return render_template('m_chat.html', qd=questionaire_data)


@is_logged_in
def to_do():
    main_emp = check_login_person_details(session['username'])
    manager_email = main_emp['manager_email']
    result = check_for_questionaires(session['username'])
    results = check_for_questionaires_all(session['username'])
    questionaire_data = check_for_questionaires_employee_detail(session['username'])
    if result>0:
        id = questionaire_data[0]['id']
        print(id)
    print('rezultatas: ')
    print (result)
    print(results)
    total = results + 1
    for x in range((total)):
        if (total - 4) > 0:
            total = total - 4
    print(total)
    if int(result) > 0:
        form = QuestionaireForm(request.form)
        if total == 1:
            questions_a = get_all_questions(1)
        elif total == 2:
            questions_a = get_all_questions(2)
        elif total == 3:
            questions_a = get_all_questions(3)
        elif total == 4:
            questions_a = get_all_questions(4)
        print(questions_a)
        questions_b = get_all_questions(6)
        print(questions_b)
        questions_d = get_all_questions(8)
        print(questions_d)
        result = check_company_email(session['username'])
        company_email = result['company_email']
        employee = check_employees(company_email)
        print(main_emp['team'])
        team_of_employee = main_emp['team']
        manager_of_employee = main_emp['manager_email']
        print(session['username'])
        print(manager_of_employee)

        if request.method == 'POST' and form.validate():
            print('register2')
            colleague = form.colleague.data
            manager = form.manager.data
            manager_email = request.form['manager_1']
            a1 = request.form['a1']
            a2 = request.form['a2']
            a3 = request.form['a3']
            a4 = request.form['a4']
            a5 = request.form['a5']
            b1 = request.form['b1']
            b2 = request.form['b2']
            a1_rev = request.form['a1-rev']
            a2_rev = request.form['a2-rev']
            a3_rev = request.form['a3-rev']
            a4_rev = request.form['a4-rev']
            a5_rev = request.form['a5-rev']
            a11 = "0"
            if a1_rev == 'R':
                if a1 == "1":
                    a11 = "6"
                elif a1 == "2":
                    a11 = "5"
                elif a1 == "3":
                    a11 = "4"
                elif a1 == "4":
                    a11 = "3"
                elif a1 == "5":
                    a11 = "2"
                elif a1 == "6":
                    a11 = "1"
                a1 = a11
            a22 = "0"
            if a2_rev == 'R':
                if a2 == "1":
                    a22 = "6"
                elif a2 == "2":
                    a22 = "5"
                elif a2 == "3":
                    a22 = "4"
                elif a2 == "4":
                    a22 = "3"
                elif a2 == "5":
                    a22 = "2"
                elif a2 == "6":
                    a22 = "1"
                a2 = a22
            a33 = "0"
            if a3_rev == 'R':
                if a3 == "1":
                    a33 = "6"
                elif a3 == "2":
                    a33 = "5"
                elif a3 == "3":
                    a33 = "4"
                elif a3 == "4":
                    a33 = "3"
                elif a3 == "5":
                    a33 = "2"
                elif a3 == "6":
                    a33 = "1"
                a3 = a33
            a44 = "0"
            if a4_rev == 'R':
                if a4 == "1":
                    a44 = "6"
                elif a4 == "2":
                    a44 = "5"
                elif a4 == "3":
                    a44 = "4"
                elif a4 == "4":
                    a44 = "3"
                elif a4 == "5":
                    a44 = "2"
                elif a4 == "6":
                    a44 = "1"
                a4 = a44
            a55 = "0"
            if a5_rev == 'R':
                if a5 == "1":
                    a55 = "6"
                elif a5 == "2":
                    a55 = "5"
                elif a5 == "3":
                    a55 = "4"
                elif a5 == "4":
                    a55 = "3"
                elif a5 == "5":
                    a55 = "2"
                elif a5 == "6":
                    a55 = "1"
                a5 = a55

            employee_email = session['username']
            print(a1)
            print(a2)
            print(employee_email)
            print('cia??')
            print(manager)
            if len(manager)>500:
                flash('Atvirame lauke viršytas simbolių limitas', 'danger')
                return render_template('to_do.html', form=form, questions_a=questions_a, questions_b=questions_b,
                              questions_d=questions_d,  main_emp=main_emp)

            update_questionaire(employee_email, manager_email,  int(a1), int(a2), int(a3), int(a4), int(a5),int(b1), int(b2), manager, id)
            print('register7')

            flash('Anketa sėkmingai užpildyta', 'success')
            return redirect(url_for('my_home'))
        return render_template('to_do.html', form=form, questions_a=questions_a, questions_b=questions_b,
                              questions_d=questions_d,  main_emp=main_emp)
    else:
        return render_template('to_do_no.html')
    return render_template('to_do_no.html')

@is_logged_in
def results():
    questionaire_data = check_for_questionaires_e_results(session['username'])
    i = 0
    b1_avg = 0
    b2_avg = 0
    b1_m_avg = 0
    b2_m_avg = 0

    for q in questionaire_data:
        i = i + 1
        b1_avg = b1_avg + q['question_b1']
        b2_avg = b2_avg + q['question_b2']
        b1_m_avg = b1_m_avg + q['question_m1']
        b2_m_avg = b2_m_avg + q['question_m2']
    if b1_avg != 0:
        b1_avg = round((b1_avg / i), 2)
        b2_avg = round((b2_avg / i), 2)
        b1_m_avg = round((b1_m_avg / i), 2)
        b2_m_avg = round((b2_m_avg / i), 2)

    return render_template('my_results.html', qd=questionaire_data, b1_avg=b1_avg, b2_avg=b2_avg, b1_m_avg=b1_m_avg, b2_m_avg=b2_m_avg)


@is_logged_in
def settings():
    return render_template('settings.html')

@is_logged_in
def download_template():
    print('ddddddd1')
    if request.method == 'GET':
        print('dddd ddd')
        return send_from_directory(directory='templates', filename='kompanijos_darbuotojai.xlsx',
                                   as_attachment=True)
    return render_template('settings.html')





def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@is_logged_in
def upload_file():
    if request.method == 'POST':
        UPLOAD_FOLDER = 'templates/uploads'
        if 'file' not in request.files:
            flash('Nerasta failo' , 'danger')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash(' „Įkelti failą“ yra privalomas laukas' , 'danger')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            flash('Failas įkeltas', 'success')
            file_name ="templates/kompanijos_darbuotojai.xlsx" + filename
            df = pd.read_excel(
                r'templates/uploads/'+filename)
            first_name_array = []
            last_name_array = []
            email_array = []
            team_array = []
            manager_email_array = []
            for x in range(len(df)-5):
                first_name_array.append(df.iloc[5+x, 1])
                last_name_array.append(df.iloc[5 + x, 2])
                email_array.append(df.iloc[5 + x, 3])
                team_array.append(df.iloc[5 + x, 4])
                manager_email_array.append(df.iloc[5 + x, 5])
            company_email = session['username']
            for x in range(len(df)-5):
                if  first_name_array[x] is not np.nan and last_name_array[x]  is not np.nan and  email_array[x]  is not np.nan and team_array[x] is not np.nan:
                    result = check_login_person(email_array[x])

                    if result == -1:
                        new_employee(first_name_array[x], last_name_array[x], email_array[x], team_array[x], manager_email_array[x], company_email)
                    else:
                        print('toks darbuotojas jau užregistruotas')
            return redirect('/admin/employees')
        else:
            flash('Netinkamas failo formatas', 'danger')

        print('cia 8')

        return render_template('settings.html')
    else:
        return render_template('settings.html')

@is_logged_in
def employee_list():
  theuser = ''
  id = request.args.get('id')
  print(id)
  company_email = session['username']
  users = check_employees2(company_email)
  i = 0
  for user in users:
    i = i + 1
    print(user)
    if str(i) == id:
        print('uzfiksuotas')
        theuser = user
  company_email = session['username']
  result = check_employees2(company_email)
  print('cia cia cia:')
  print(result)
  employee_table = ""
  i =0
  if not result:
      print('daugiau')
  else:
    for r in result:
        i=i+1
        print(r)
        employee_table = employee_table + """ <tr> """ + """   <th scope="row"> """ + str(
            i) + """</th>""" + """ <td> """ + str(r['first_name']) + """</td> """ + """ <td>""" + str(
            r['last_name']) + """</td> """ + """ <td> """ + str(r['email']) + """</td> """ + """  <td>""" + str(
            r['team']) + """</td>""" + """ <td>""" + str(r['manager_email']) + """</td>""" + """<td>""" + str(
            r['start_date']) + """</td>""" + """<td>""" + str(r[
                                                                  'end_date']) + """</td>""" + """ <td> <a href="/admin/employees/edit?id=""" +  str(i) + """"" class="btn btn-warning btn-xs" >CHANGE</a> </td>  <td> <a href="/admin/employees?id=""" +  str(i) + """"" class="btn btn-danger btn-xs" >DELETE</a></td> </tr> """

  filename = '.\\templates\\admin_employee_list.html'
  f = open(filename, 'w')


  body_first = """ {% extends 'layout-admin.html' %}

 {% block body %}
   <a class="list-group-item list-group-item-action list-group-item-info">
    <h1 align="center"><span class="label label-info">Darbuotojai </span></h1>
<br>
	 </a>
<br>

  {% if theuser %}
  <form class="modal-content" method="GET" action="">
    <div class="container bg-danger text-white">
      <h1>Ištrinti darbuotoją {{theuser.first_name}} {{theuser.last_name}}</h1>
      <p>Ar tikrai norite ištrinti darbuotoją {{theuser.first_name}} {{theuser.last_name}}?</p>

      <div class="clearfix">
        
        <a href="/admin/employees" class="btn btn-light btn-xs" >Atšaukti</a>
        <a href="/admin/employees?delete={{theuser.email}}" class="btn btn-light btn-xs" >Taip</a>
        
      </div>
    </div>
    <br>
  </form>
{% endif %}
<br>
  """

  body_third = """
    </form>
    </tbody>
</table>

  {% endblock %}"""
  body_second = """  <table class="table table-hover table-dark">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Vardas</th>
      <th scope="col">Pavarde</th>
      <th scope="col">El. pastas</th>
      <th scope="col">Komanda</th>
      <th scope="col">Vadovo el. pastas</th>
      <th scope="col">Registracijos data</th>
      <th scope="col">Pabaigos data</th>
      	  
    </tr>
  </thead>
  <tbody>
  <form method="POST" action="">
 """ + employee_table
  wrapper = """%s %s %s"""
  if not result:
      body_second = """ <h3 align = 'center'> Nėra nei vieno darbuotojo </h3>"""
      whole = wrapper % (body_first, body_second, body_third)
  else:
      whole = wrapper % (body_first, body_second, body_third)

  with open(filename, "w", encoding="utf-8") as f:
      f.write(whole)
  f.close()

  if request.method == 'POST':
      if request.form['submit_button'] == 'Do Something':
          flash('do something', "success")
          return render_template('admin_e_update.html')

  id = request.args.get('id')
  if id:
      return render_template('admin_employee_list.html', theuser=theuser)

  delete = request.args.get('delete')
  if delete:
      rr = check_employees_of_manager(delete)
      if rr:
          flash('Darbuotojas turi pavaldinių, todėl jo negalima ištrinti', 'danger')
          return render_template('admin_employee_list.html')
      else:
          delete_employee(delete)
          flash('Darbuotojas sėkmingai ištrintas', 'success')
          return redirect(url_for('employee_list'))

  return render_template('admin_employee_list.html')

@is_logged_in
def admin_epmloyees_update():
    form = EmployeeProfileForm(request.form)
    theuser=''
    id = request.args.get('id')
    print(id)
    company_email = session['username']
    users = check_employees(company_email)
    i = 0
    for user in users:
        i = i + 1
        print(user)
        if str(i) == id:
            theuser = user

            print('cia')
    if request.method == 'GET':
        form.first_name.data = theuser['first_name']
        form.last_name.data = theuser['last_name']
        form.email.data = theuser['email']
        form.team.data = theuser['team']
        form.manager_email.data = theuser['manager_email']
        form.start_date.data = theuser['start_date']
        form.end_date.data = theuser['end_date']
    if request.method == 'POST' and form.validate():
        first_name_e = form.first_name.data
        last_name_e = form.last_name.data
        email_e = form.email.data
        team_e = form.team.data
        manager_email_e = form.manager_email.data
        start_date_e = form.start_date.data
        end_date_e = form.end_date.data
        tikrinimui_e = 0
        tikrinimui_m = 0
        if email_e == theuser['email']:
            print('darbuotojo paštas išlieka toks pat')
        else:
            res = check_email(email_e)
            if not res:
                tikrinimui_e = 1
            else:
                flash('Toks el. paštas jau yra naudojamas', 'danger')
                return render_template('admin_e_update.html', form=form, theuser=theuser)
        if manager_email_e == theuser['manager_email']:
        else:
            if manager_email_e != 'none':
                res = check_email_for_manager(manager_email_e)
                if not res:
                    flash('Nėra vadovo su nurodytu el. pašto adresu', 'danger')
                    return render_template('admin_e_update.html', form=form, theuser=theuser)
                else:
                    tikrinimui_m = 1
            else:
                    tikrinimui_m = 1
            if theuser['manager_email'] == 'none':
                rr = check_employees_of_manager(theuser['email'])
                print(rr)
                if rr:
                    tikrinimui_m = 0
                    flash('Darbuotojas turi pavaldinių, todėl vadovo el. pašto negalima pakeisti', 'danger')
                    return render_template('admin_e_update.html', form=form, theuser=theuser)
                else:
                    print('pakeist manager_email3')
                    tikrinimui_m = 1

        if tikrinimui_e == 1:
            change_e_email(theuser['email'], email_e)
            if theuser['manager_email'] == 'none':
                change_e_m_email(theuser['email'],email_e)
        if tikrinimui_m == 1:
          change_m_email(theuser['email'], manager_email_e)

        flash('Sėkmingai atnaujinta informacija', 'success')

        return redirect(url_for('employee_list'))

    return render_template('admin_e_update.html', form=form, theuser=theuser)

@is_logged_in
def admin_home():
    return render_template('admin_home.html')

def login():
    if request.method == 'POST':
        from controller import check_login
        username = request.form['username']
        password_candidate = request.form['password']
        error = ''
        if username == '' or password_candidate == '':
            if username == '':
                error = error + ' El. paštas laukas yra neužpildytas.'

            if password_candidate == '':
                error = error + ' Slaptažodis laukas yra neužpildytas.'
            return render_template('login-company.html', error=error)
        result = check_login(username);

        if result == -1:
            result2 = check_login_person(username);
            if result2 != -1:

                password_try = check_password_try2(username)
                if (password_try < 5):
                    password = result2
                    if sha256_crypt.verify(password_candidate, password):
                        # Passed
                        change_password_try2(username, 0)
                        session['logged_in'] = True
                        session['username'] = username
                        flash('Jūs prisijungėte', 'success')
                        level = check_level_person(username)
                        if level['level'] == 1:
                            return redirect(url_for('admin_home'))
                        elif level['level'] == 2:
                            return redirect(url_for('manager_home'))
                        elif level['level'] == 3:
                            return redirect(url_for('my_home'))
                        elif level['level'] == 4:
                            return redirect(url_for('my_home'))


                    else:
                        error = 'Neteisingas prisijungimas'
                        password_try_new = password_try + 1
                        change_password_try2(username, password_try_new)
                        if password_try_new == 5:
                            error = 'Per daug kartų suklydote vesdami slaptažodį'
                            return render_template('help.html', error=error)
                        return render_template('login-company.html', error=error)
                else:
                    error = 'Jūsų paskyra užsaldyta'
                    return render_template('help.html', error=error)

            else:
                error = 'Neteisingas vartotojo vardas'
                return render_template('login-company.html', error=error)

        if result != -1:
            password_try = check_password_try(username)
            if (password_try<5):
                password = result
                if sha256_crypt.verify(password_candidate, password):
                    change_password_try(username, 0)
                    session['logged_in'] = True
                    session['username'] = username
                    flash('Jūs prisijungėte', 'success')
                    return redirect(url_for('admin_home'))

                else:
                    error = 'Neteisingas prisijungimas'
                    password_try_new = password_try +1
                    change_password_try(username, password_try_new)
                    if password_try_new==5:
                        error = 'Per daug kartų suklydote vesdami slaptažodį'
                        return render_template('help.html', error=error)
                    return render_template('login-company.html', error=error)
            else:
                error = 'Jūsų paskyra užsaldyta'
                return render_template('help.html', error=error)

        else:
            error = 'Neteisingas vartotojo vardas'
            return render_template('login-company.html', error=error)
    return render_template('login-company.html')