#!/usr/bin/env python3
from model import connectToDB, get_cursor, create, fetch_one, read, read_level, create_employee, read_all_employees, \
    read_person, read_e, \
    read_company_email, create_category, read_category, read_all_questions, read_person_details, \
    read_all_employees_email, create_questionaire, read_questionaires, update_questionaire_model, \
    read_questionaires_manager, read_questionaires_manager_detail, update_questionaire_model_manager, create_kudos, \
    read_questionaires_employee_detail, feedback_history_db, m_feedback_history_db, read_company_name, read_password_try, \
    change_password_tried, change_company_profile_m, change_employee_company_email_m, change_company_profile_password_m,  \
    check_for_email, change_e_email_e, check_for_email_m, delete_e,  questionairs_for_admin, read_all_employees2

def feedback_history(e_email):
    table_title = 'pkp_questionaires'
    list = ['employee_email', 'manager_done']
    values = [e_email, 'yes']
    result = feedback_history_db(table_title, list, values)
    return result;
def m_feedback_history(m_email):
    table_title = 'pkp_questionaires'
    list = ['manager_email','manager_done']
    values = [m_email, 'yes']
    result = m_feedback_history_db(table_title, list, values)
    return result;


def check_login(email):
    table_title = 'pkp_companies'
    list = ['email']
    values = [email]
    result = read(table_title, list, values)
    return result



def check_login_e(email):
    table_title = 'pkp_employees'
    list = ['email']
    values = [email]
    result = read_e(table_title, list, values)
    return result


def check_password_try(email):
    table_title = 'pkp_companies'
    list = ['email']
    values = [email]
    result = read_password_try(table_title, list, values)

    return result

def check_password_try2(email):
    table_title = 'pkp_employees'
    list = ['email']
    values = [email]
    result = read_password_try(table_title, list, values)

    return result


def change_password_try(email, password_try):
    table_title = 'pkp_companies'
    list = ['email', 'password_try']
    values = [email, password_try]
    result = change_password_tried(table_title, list, values)
    return result

def change_password_try2(email, password_try):
    table_title = 'pkp_employees'
    list = ['email', 'password_try']
    values = [email, password_try]
    result = change_password_tried(table_title, list, values)
    return result


def check_category(category, company_email):
    table_title = 'pkp_questions'
    list = ['title', 'level', 'belongs_to']
    values = [category, 10, company_email]
    result = read_category(table_title, list, values)
    return result

def check_login_person(email):
    table_title = 'pkp_employees'
    list = ['email']
    values = [email]
    result = read_person(table_title, list, values)
    return result

def check_login_person_details(email):
    table_title = 'pkp_employees'
    list = ['email']
    values = [email]
    result = read_person_details(table_title, list, values)
    return result

def check_level(email):
    table_title = 'pkp_companies'
    list = ['email']
    values = [email]
    result = read_level(table_title, list, values)
    return result;

def check_level_person(email):
    table_title = 'pkp_employees'
    list = ['email']
    values = [email]
    result = read_level(table_title, list, values)
    return result;

def check_company_email(email):
    table_title = 'pkp_employees'
    list = ['email']
    values = [email]
    result = read_company_email(table_title, list, values)
    return result;


def check_company_name(company_name):
    table_title = 'pkp_companies'
    list = ['company_name']
    values = [company_name]
    result = read_company_name(table_title, list, values)
    return result;


def change_company_profile(company_name, old_email, new_email):
    table_title = 'pkp_companies'
    list = ['company_name', 'email', 'email']
    values = [company_name, old_email, new_email]
    result = change_company_profile_m(table_title, list, values)
    return result;

def change_company_profile_password(email, new_password):
    table_title = 'pkp_companies'
    list = ['email', 'password']
    values = [email, new_password]
    result = change_company_profile_password_m(table_title, list, values)
    return result;

def change_employee_profile_password(email, new_password):
    table_title = 'pkp_employees'
    list = ['email', 'password']
    values = [email, new_password]
    result = change_company_profile_password_m(table_title, list, values)
    return result;

def change_employees_company_email(old_email, new_email):
    table_title = 'pkp_employees'
    list = ['company_email', 'company_email']
    values = [old_email, new_email]
    result = change_employee_company_email_m(table_title, list, values)
    return result;

def check_employees(company_email):
    table_title = 'pkp_employees'
    list = ['company_email']
    values = [company_email]
    result = read_all_employees2(table_title, list, values)
    return result;
def check_employees2(company_email):
    table_title = 'pkp_employees'
    list = ['company_email']
    values = [company_email]
    result = read_all_employees2(table_title, list, values)
    return result;


def check_email(email):
    table_title = 'pkp_employees'
    list = ['email']
    values = [email]
    result = check_for_email(table_title, list, values)
    return result;

def check_email_for_manager(email):
    table_title = 'pkp_employees'
    list = ['email', 'manager_email']
    values = [email, 'none']
    result = check_for_email_m(table_title, list, values)
    return result;

def check_employees_of_manager(email):
    table_title = 'pkp_employees'
    list = ['manager_email']
    values = [email]
    result = check_for_email(table_title, list, values)
    return result;

def change_e_email(old_email, new_email):
    table_title = 'pkp_employees'
    list = ['email', 'email']
    values = [old_email, new_email]
    result = change_e_email_e(table_title, list, values)
    return result;

def delete_employee(email):
    table_title = 'pkp_employees'
    list = ['email']
    values = [email]
    result = delete_e(table_title, list, values)
    return result;

def change_e_m_email(old_email, new_email):
    table_title = 'pkp_employees'
    list = ['manager_email', 'manager_email']
    values = [old_email, new_email]
    result = change_e_email_e(table_title, list, values)
    return result;

def check_if_manager(email):
    table_title = 'pkp_employees'
    list = ['email', 'manager_email']
    values = [email, 'none']
    result = check_for_email_m(table_title, list, values)
    return result;

def change_m_email(e_email, m_email):
    table_title = 'pkp_employees'
    list = ['email', 'manager_email']
    values = [e_email, m_email]
    result = change_e_email_e(table_title, list, values)
    return result;

def get_profile_info(email):
    table_title = 'pkp_employees'
    list = ['email']
    values = [email]
    result = read_all_employees2(table_title, list, values)
    return result;

def get_manager_profile_info(email):
    table_title = 'pkp_employees'
    list = ['company_email', 'manager_email']
    values = [email, 'none']
    result = questionairs_for_admin(table_title, list, values)
    return result;

def get_profile_info_admin(email):
    table_title = 'pkp_companies'
    list = ['email']
    values = [email]
    result = read_all_employees2(table_title, list, values)
    return result;

def get_profile_info_team(email):
    table_title = 'pkp_employees'
    list = ['manager_email']
    values = [email]
    result = read_all_employees2(table_title, list, values)
    return result;

def get_questions(title):
    table_title = 'pkp_questions'
    list = ['title']
    values = [title]
    result = read_all_employees2(table_title, list, values)
    return result;

def get_all_questions(num):
    table_title = 'pkp_questions'
    list = ['belongs_to']
    values = [num]
    result = read_all_questions(table_title, list, values)
    return result;

def new_company(company_name, email, password):
    success = 0
    table_title = 'pkp_companies'
    list = ['company_name', 'email', 'password', 'password_try']
    values = [company_name, email, password, 0]
    create(table_title, list, values)
    return success

def new_employee(first_name_array, last_name_array, email_array, team_array, manager_email_array, company_email):
    success = 0
    table_title = 'pkp_employees'
    list = ['first_name', 'last_name', 'email', 'team', 'manager_email', 'company_email', 'level']
    if manager_email_array == 'none':
        level = 2
    else:
        level = 3
    values = [first_name_array, last_name_array, email_array, team_array, manager_email_array, company_email, level]
    create_employee(table_title, list, values)

    return success

def new_questionaire(manager_email, e_email):
    success = 0
    table_title = 'pkp_questionaires'
    list = ['manager_email', 'employee_email', 'employee_done', 'manager_done']
    values = [manager_email, e_email, "no", "no"]
    create_questionaire(table_title, list, values)
    return success

def check_employees_of_the_team(manager_email):
    table_title = 'pkp_employees'
    list = ['manager_email']
    values = [manager_email]
    result = read_all_employees_email(table_title, list, values)
    return result;

def check_for_questionaires(e_email):
    table_title = 'pkp_questionaires'
    list = ['employee_email', 'employee_done']
    values = [e_email, 'no']
    result = read_questionaires(table_title, list, values)
    return result;

def check_for_questionaires_manager(e_email):
    table_title = 'pkp_questionaires'
    list = ['manager_email', 'employee_done', 'manager_done']
    values = [e_email, 'yes', 'no']
    result = read_questionaires_manager(table_title, list, values)
    return result;

def check_for_questionaires_manager_detail(e_email):
    table_title = 'pkp_questionaires'
    list = ['manager_email', 'employee_done', 'manager_done', 'start_date']
    values = [e_email, 'yes', 'no', '']
    result = read_questionaires_manager_detail(table_title, list, values)
    return result;

def check_for_questionaires_employee_detail(e_email):
    table_title = 'pkp_questionaires'
    list = ['employee_email', 'employee_done', 'manager_done']
    values = [e_email, 'no', 'no']
    result = read_questionaires_employee_detail(table_title, list, values)
    return result;

def check_for_questionaires_manager_results(e_email):
    table_title = 'pkp_questionaires'
    list = ['manager_email', 'employee_done', 'manager_done', 'start_date']
    values = [e_email, 'yes', 'yes', 'DATEADD(month,1,CURRENT_TIMESTAMP)']
    result = read_questionaires_manager_detail(table_title, list, values)
    return result;

def check_for_questionaires_e_results(e_email):
    table_title = 'pkp_questionaires'
    list = ['employee_email', 'employee_done', 'manager_done', 'start_date']
    values = [e_email, 'yes', 'yes', '']
    result = read_questionaires_manager_detail(table_title, list, values)
    return result;

def check_for_questionaires_all(e_email):
    table_title = 'pkp_questionaires'
    list = ['employee_email', 'employee_done']
    values = [e_email, 'yes']
    result = read_questionaires(table_title, list, values)
    return result;

def update_questionaire(employee_email, manager_email, a1, a2, a3, a4, a5,b1, b2,  manager, id):
    success = 0
    table_title = 'pkp_questionaires'
    list = ['employee_email','manager_email', 'question_a1', 'question_a2', 'question_a3',
             'question_a4', 'question_a5', 'question_b1', 'question_b2', 'question_c2', 'employee_done', 'id']
    values = [employee_email, manager_email, a1, a2, a3, a4,a5, b1, b2,  manager, "yes", "no", id]
    update_questionaire_model(table_title, list, values)
    return success

def update_questionaire_manager(m1,m2, manager, id):
    success = 0
    table_title = 'pkp_questionaires'
    list = ['id','question_m1','question_m2', 'question_m3', 'manager_done']
    values = [id, m1, m2, manager,"yes"]
    update_questionaire_model_manager(table_title, list, values)
    return success