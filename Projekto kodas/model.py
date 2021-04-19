#!/usr/bin/env python3
import pymysql as pymysql
import sqlite3 as sqlite3
def connectToDB():
    con = pymysql.connect(host="localhost", user="root",password="", db="testdb",
                          cursorclass=pymysql.cursors.DictCursor)
    return con

def feedback_history_db(table_title,list,values):
    con = connectToDB()
    cur = con.cursor()
    result = cur.execute("SELECT * FROM " + table_title + " WHERE " + list[0] + " = %s and " + list[1] + " = %s", (values[0], values[1]))
    result=cur.fetchall()
    return result
def m_feedback_history_db(table_title,list,values):
    con = connectToDB()
    cur = con.cursor()
    result = cur.execute("SELECT * FROM " + table_title + " WHERE " + list[0] + " = %s and " + list[1] + " = %s", (values[0], values[1]))
    result=cur.fetchall()
    return result

def get_cursor(connection):
    cur =connection.cursor()
    return cur

def create(table_title,list,values):
    success = 0
    con = connectToDB()
    cur = con.cursor()
    try:
        with cur as cursor:
            cursor.execute(
                "INSERT INTO " + table_title + "(" + list[0] + "," + list[1] + "," + list[2] + "," + list[3] +  ") VALUES(%s, %s, %s, %s)",
                (values[0],values[1],values[2], values[3]))
        con.commit()
    finally:
        con.close()
    return success

def create_category(table_title,list,values):
    success = 0
    con = connectToDB()
    cur = con.cursor()
    try:
        with cur as cursor:
            cursor.execute(
                "INSERT INTO " + table_title + "(" + list[0] + "," + list[1] + "," + list[2] + "," + list[3] + "," +
                list[4]  +") VALUES(%s, %s, %s, %s, %s)",
                (values[0],values[1],values[2],values[3],values[4]))
        con.commit()
    finally:
        con.close()
    return success

def create_questionaire(table_title,list,values):
    success = 0
    con = connectToDB()
    cur = con.cursor()
    try:
        with cur as cursor:
            cursor.execute(
                "INSERT INTO " + table_title + "(" + list[0] + "," + list[1] + "," + list[2] + "," + list[3]  +") VALUES(%s, %s, %s, %s)",
                (values[0],values[1],values[2],values[3]))
        con.commit()
    finally:
        con.close()
    return success

def create_kudos(table_title,list,values):
    success = 0
    con = connectToDB()
    cur = con.cursor()
    try:
        with cur as cursor:
            cursor.execute(
                "INSERT INTO " + table_title + "(" + list[0] + "," + list[1] + "," + list[2]  +") VALUES(%s, %s, %s)",
                (values[0],values[1],values[2]))
        con.commit()
    finally:
        con.close()
    return success

def create_employee(table_title,list,values):
    success = 0
    con = connectToDB()
    cur = con.cursor()
    try:
        with cur as cursor:
            cursor.execute(
                "INSERT INTO " + table_title + "(" + list[0] + "," + list[1] + "," + list[2] + "," + list[3] + "," +
                list[4] + "," + list[5] + "," + list[6]  +") VALUES(%s, %s, %s, %s, %s, %s, %s)",
                (values[0],values[1],values[2],values[3],values[4],values[5], values[6]))
        con.commit()
    finally:
        con.close()
    return success

def read(table_title,list,values):
    success = 0
    con = connectToDB()
    cur = con.cursor()
    result = cur.execute("SELECT * FROM " + table_title + " WHERE " + list[0] + " = %s", [values[0]])
    if result > 0:
        result  = passw(con, cur)
        return result
    else:
        result = -1
        con.close()
        return result

def read_e(table_title, list, values):
        success = 0
        con = connectToDB()
        cur = con.cursor()
        result = cur.execute("SELECT * FROM " + table_title + " WHERE " + list[0] + " = %s", [values[0]])
        if result > 0:
            result = passw(con, cur)
            return result
        else:
            result = -1
            con.close()
            return result

def read_password_try(table_title, list, values):
        success = 0
        con = connectToDB()
        cur = con.cursor()
        result = cur.execute("SELECT password_try FROM " + table_title + " WHERE " + list[0] + " = %s", [values[0]])
        data = cur.fetchone()
        result = data['password_try']
        return result




def change_password_tried(table_title, list, values):
    success = 0
    con = connectToDB()
    cur = con.cursor()
    try:
        result = cur.execute("UPDATE " + table_title +  " SET " + list[1] + " = " + str(values[1]) + " where " + list[0] + """='""" + values[0] + """'""")
        con.commit()
    finally:
        con.close()
    return result


def change_company_profile_m(table_title, list, values):
    success = 0
    con = connectToDB()
    cur = con.cursor()
    try:
        with cur as cursor:

            cursor.execute("UPDATE " + table_title +  " SET " + list[0] + """ = '""" + str(values[0]) + """' where """ + list[1] + """='""" + str(values[1]) + """'""")
            cursor.execute("UPDATE " + table_title +  " SET " + list[2] + """ = '""" + str(values[2]) + """' where """ + list[0] + """='""" + str(values[0]) + """'""")
        con.commit()
    finally:
        con.close()
    return success

def change_company_profile_password_m(table_title, list, values):
    success = 0
    con = connectToDB()
    cur = con.cursor()
    try:
        with cur as cursor:
            cursor.execute(
                "UPDATE " + table_title + " SET " + list[1] + """ = '""" + str(values[1]) + """' where """ + list[
                    0] + """='""" + str(values[0]) + """'""")
        con.commit()
    finally:
        con.close()
    return success


def change_employee_company_email_m(table_title, list, values):
    success = 0
    con = connectToDB()
    cur = con.cursor()
    try:
        with cur as cursor:
            cursor.execute(
                "UPDATE " + table_title + " SET " + list[1] + """ = '""" + str(values[1]) + """' where """ + list[
                    0] + """='""" + str(values[0]) + """'""")
        con.commit()
    finally:
        con.close()
    return success

def read_category(table_title,list,values):
    con = connectToDB()
    cur = con.cursor()
    result = cur.execute("SELECT * FROM " + table_title + " WHERE " + list[0] + " = %s and " + list[1] + " = %s and " + list[2] + " = %s", (values[0], values[1], values[2]))
    if result > 0:
        return result
    else:
        result = -1
        con.close()
        return result

def read_person(table_title,list,values):
    success = 0
    con = connectToDB()
    cur = con.cursor()
    result = cur.execute("SELECT * FROM " + table_title + " WHERE " + list[0] + " = %s", [values[0]])
    if result > 0:
        result = passw(con, cur)
        return result
    else:
        result = -1
        con.close()
        return result

def read_person_details(table_title,list,values):
    success = 0
    con = connectToDB()
    cur = con.cursor()
    result = cur.execute("SELECT * FROM " + table_title + " WHERE " + list[0] + " = %s", [values[0]])
    result = cur.fetchone()
    return result


def read_level(table_title,list,values):
    con = connectToDB()
    cur = con.cursor()
    result = cur.execute("SELECT level FROM " + table_title + " WHERE " + list[0] + " = %s", [values[0]])
    result=cur.fetchone()
    return result

def read_company_email(table_title,list,values):
    con = connectToDB()
    cur = con.cursor()
    result = cur.execute("SELECT company_email FROM " + table_title + " WHERE " + list[0] + " = %s", [values[0]])
    result=cur.fetchone()
    return result


def read_company_name(table_title,list,values):
    con = connectToDB()
    cur = con.cursor()
    result = cur.execute("SELECT company_name FROM " + table_title + " WHERE " + list[0] + " = %s", [values[0]])
    result=cur.fetchone()
    return result

def read_all_employees(table_title,list,values):
    con = connectToDB()
    cur = con.cursor()
    cur.execute("SELECT * FROM " + table_title + " WHERE " + list[0] + " = %s and " + list[1] + " = %s", [values[0], values[1]])
    result = cur.fetchall()

def read_all_employees2(table_title, list, values):
    con = connectToDB()
    cur = con.cursor()
    cur.execute("SELECT * FROM " + table_title + " WHERE " + list[0] + " = %s",[values[0]])
    result = cur.fetchall()
    return result

def questionairs_for_admin(table_title,list,values):
    con = connectToDB()
    cur = con.cursor()
    cur.execute("select * from pkp_questionaires, pkp_employees where pkp_questionaires.manager_email=pkp_employees.email and pkp_employees.company_email= " + """%s""", [values[0]])
    result = cur.fetchall()
    return result


def check_for_email_m(table_title,list,values):
    con = connectToDB()
    cur = con.cursor()
    cur.execute("SELECT * FROM " + table_title + " WHERE " + list[0] + " = %s and " + list[1] + " = %s", [values[0], values[1]])
    result = cur.fetchall()
    return result



def check_for_email(table_title,list,values):
    con = connectToDB()
    cur = con.cursor()
    cur.execute("SELECT * FROM " + table_title + " WHERE " + list[0] + " = %s", [values[0]])
    result = cur.fetchall()
    return result

def change_e_email_e(table_title, list, values):
    success = 0
    con = connectToDB()
    cur = con.cursor()
    try:
        with cur as cursor:
            cursor.execute(
                "UPDATE " + table_title + " SET " + list[1] + """ = '""" + str(values[1]) + """' where """ + list[
                    0] + """='""" + str(values[0]) + """'""")

        con.commit()
    finally:
        con.close()
    return success



def delete_e(table_title, list, values):
    success = 0
    con = connectToDB()
    cur = con.cursor()
    try:
        with cur as cursor:
            cursor.execute(
                "DELETE FROM " + table_title + "  where """ + list[0] + """='""" + str(values[0]) + """'""")
        con.commit()
    finally:
        con.close()
    return success


def read_all_questions(table_title,list,values):
    con = connectToDB()
    cur = con.cursor()
    cur.execute("SELECT * FROM " + table_title + " WHERE " + list[0] + " = %s ", (values[0]))
    result = cur.fetchall()
    return result

def passw(con, cur):
    password = fetch_one(cur)
    con.close()
    result = password
    return result
def fetch_one(cur):
    data = cur.fetchone()
    password = data['password']
    return password

def read_all_employees_email(table_title,list,values):
    con = connectToDB()
    cur = con.cursor()
    cur.execute("SELECT email FROM " + table_title + " WHERE " + list[0] + " = %s", [values[0]])
    result = cur.fetchall()
    return result

def read_questionaires(table_title,list,values):
    con = connectToDB()
    cur = con.cursor()
    result = cur.execute("SELECT * FROM " + table_title + " WHERE " + list[0] + " = %s and " + list[1] + " = %s", (values[0], values[1]))
    return result

def read_questionaires_manager(table_title,list,values):
    con = connectToDB()
    cur = con.cursor()
    result = cur.execute("SELECT * FROM " + table_title + " WHERE " + list[0] + " = %s and " + list[1] + " = %s and " + list[2] + " = %s", (values[0], values[1], values[2]))
    return result

def read_questionaires_manager_detail(table_title,list,values):
    con = connectToDB()
    cur = con.cursor()
    import datetime
    now = datetime.datetime.now()
    then = now - datetime.timedelta(days=90)
    print("SELECT * FROM " + table_title + " WHERE " + list[0] + " = %s and " + list[1] + " = %s and " + list[2] + " = %s and " + list[3] + " %s" , (values[0], values[1], values[2], then))
    result = cur.execute("SELECT * FROM " + table_title + " WHERE " + list[0] + " = %s and " + list[1] + " = %s and " + list[2] + " = %s and " + list[3] + " >= %s" , (values[0], values[1], values[2], then))
    result=cur.fetchall()
    return result
def read_questionaires_employee_detail(table_title,list,values):
    con = connectToDB()
    cur = con.cursor()
    result = cur.execute("SELECT * FROM " + table_title + " WHERE " + list[0] + " = %s and " + list[1] + " = %s and " + list[2] + " = %s", (values[0], values[1], values[2]))
    result=cur.fetchall()
    return result

def update_questionaire_model(table_title,list,values):
    success = 0
    con = connectToDB()
    cur = con.cursor()
    try:
        with cur as cursor:
             cursor.execute("Update pkp_questionaires SET " + list[2] + """ = '""" + str(values[2]) + "' where " + list[0] + """='""" + values[0] + """' and """ + list[11] + """ = '"""+str(values[12]) +"""'""")
             cursor.execute("Update pkp_questionaires SET " + list[3] + """ = '""" + str(values[3]) + "' where " + list[0] + """='""" + values[0] + """' and """ + list[11] + """ = '"""+str(values[12]) +"""'""")
             cursor.execute("Update pkp_questionaires SET " + list[4] + """ = '""" + str(values[4]) + "' where " + list[0] + """='""" + values[0] + """' and """ + list[11] + """ = '"""+str(values[12]) +"""'""")
             cursor.execute("Update pkp_questionaires SET " + list[5] + """ = '""" + str(values[5]) + "' where " + list[0] + """='""" + values[0] + """' and """ + list[11] + """ = '"""+str(values[12]) +"""'""")
             cursor.execute("Update pkp_questionaires SET " + list[6] + """ = '""" + str(values[6]) + "' where " + list[0] + """='""" + values[0] + """' and """ + list[11] + """ = '"""+str(values[12]) +"""'""")
             cursor.execute("Update pkp_questionaires SET " + list[7] + """ = '""" + str(values[7]) + "' where " + list[0] + """='""" + values[0] + """' and """ + list[11] + """ = '"""+str(values[12]) +"""'""")
             cursor.execute("Update pkp_questionaires SET " + list[8] + """ = '""" + str(values[8]) + "' where " + list[0] + """='""" + values[0] + """' and """ + list[11] + """ = '"""+str(values[12]) +"""'""")
             cursor.execute("Update pkp_questionaires SET " + list[9] + """ = '""" + str(values[9]) + "' where " + list[0] + """='""" + values[0] + """' and """ + list[11] + """ = '"""+str(values[12]) +"""'""")
             cursor.execute("Update pkp_questionaires SET " + list[10] + """ = '""" + str(values[10]) + "' where " + list[0] + """='""" + values[0] + """' and """ + list[11] + """ = '"""+str(values[12]) +"""'""")

        con.commit()
    finally:
        con.close()
    return success

def update_questionaire_model_manager(table_title,list,values):
    success = 0
    con = connectToDB()
    cur = con.cursor()
    try:
        with cur as cursor:
             cursor.execute("Update pkp_questionaires SET " + list[1] + """ = '""" + str(values[1]) + "' where " + list[0] + """='""" + values[0] + """'""")
             cursor.execute("Update pkp_questionaires SET " + list[2] + """ = '""" + str(values[2]) + "' where " + list[0] + """='""" + values[0] + """'""")
             cursor.execute("Update pkp_questionaires SET " + list[3] + """ = '""" + str(values[3]) + "' where " + list[0] + """='""" + values[0] + """'""")
             cursor.execute("Update pkp_questionaires SET " + list[4] + """ = '""" + str(values[4]) + "' where " + list[0] + """='""" + values[0] + """'""")

        con.commit()
    finally:
        con.close()
    return success