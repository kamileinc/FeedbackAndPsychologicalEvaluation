#!/usr/bin/env python3
#BETWEEN MODEL AND VIEW
from flask import Flask

def create_app(config):
    # create app and load config
    app = Flask(__name__)
    app.config.from_object(config)

    # initalize app with database
    #from model import mysql
    #mysql.init_app(app)

    # bind views
    from view import home, testimonials, register, login, logout, chat, my_profile, to_do, \
        my_home, results, settings, download_template, upload_file, employee_list, admin_home,\
        manager_home, m_manage_team, manager_profile, manage_feedback_tool, manager_team_results, manager_to_do, \
        manager_chat, admin_profile, admin_profile_password, admin_epmloyees_update, manager_profile_password, \
        employee_profile_password, manager_questionaire, employee_questionaire, admin_results, admin_questionaire
    app.add_url_rule('/', view_func=home)
    app.add_url_rule('/testimonials', view_func=testimonials)
    app.add_url_rule('/register', methods=['GET', 'POST'], view_func=register)
    app.add_url_rule('/login', methods=['GET', 'POST'], view_func=login)
    app.add_url_rule('/logout', view_func=logout)
    app.add_url_rule('/my/chat', view_func=chat)
    app.add_url_rule('/my/profile', view_func=my_profile)
    app.add_url_rule('/my/to_do', methods=['POST', 'GET'], view_func=to_do)
    app.add_url_rule('/my/home', view_func=my_home)
    app.add_url_rule('/my/results', view_func=results)
    app.add_url_rule('/admin/upload', view_func=settings)
    app.add_url_rule('/settings/download', methods=['GET'], view_func=download_template)
    app.add_url_rule('/settings/upload_file', methods=['POST', 'GET'], view_func=upload_file)
    app.add_url_rule('/admin/employees', view_func=employee_list)
    app.add_url_rule('/admin', view_func=admin_home)
   # app.add_url_rule('/login/person', methods=['GET', 'POST'], view_func=login_person)
   # app.add_url_rule('/login/company', methods=['GET', 'POST'], view_func=login_company)
    app.add_url_rule('/manager/home', view_func=manager_home)
    app.add_url_rule('/manager/manage-your-team', view_func=m_manage_team)
    app.add_url_rule('/manager/my-profile', view_func=manager_profile)
    app.add_url_rule('/manager/manage-feedback-tool', methods=['GET', 'POST'], view_func=manage_feedback_tool)
    app.add_url_rule('/manager/team-results', view_func=manager_team_results)
    app.add_url_rule('/manager/to-do',methods=['GET', 'POST'], view_func=manager_to_do)
    app.add_url_rule('/manager/chat', view_func=manager_chat)
    app.add_url_rule('/admin/profile', methods=['GET', 'POST'], view_func=admin_profile)
    app.add_url_rule('/admin/profile/password', methods=['GET', 'POST'], view_func=admin_profile_password)
    app.add_url_rule('/admin/employees/edit', methods=['GET', 'POST'], view_func=admin_epmloyees_update)

    app.add_url_rule('/manager/my-profile/password', methods=['GET', 'POST'], view_func=manager_profile_password)
    app.add_url_rule('/my/my-profile/password', methods=['GET', 'POST'], view_func=employee_profile_password)
    app.add_url_rule('/manager/team-results/questionaire', methods=['GET', 'POST'], view_func=manager_questionaire)
    app.add_url_rule('/my/results/questionaire', methods=['GET', 'POST'], view_func=employee_questionaire)
    app.add_url_rule('/admin/results', methods=['GET', 'POST'], view_func=admin_results)
    app.add_url_rule('/admin/results/questionaire', methods=['GET', 'POST'], view_func=admin_questionaire)
    return app
