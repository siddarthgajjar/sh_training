from xmlrpc import client
import json

url = 'https://online-technical-training-13-0-dev-openacademy-2142807.dev.odoo.com'
db = 'online-technical-training-13-0-dev-openacademy-2142807'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print("VERSION:")
print(common.version())

uid = common.authenticate(db, username, password, {})
print("UID:")
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db, uid, password,
                                 'academy.session', 'check_access_rights',
                                 ['write'], {'raise_exception': False})
print("MODEL ACCESS:")
print(model_access)

courses = models.execute_kw(db, uid, password,
                           'academy.course', 'search_read',
                           [[('level', 'in', ['intermediate', 'beginner'])]])
print("BEGINNER/INTERMEDIATE COURSES:")
print(json.dumps(courses, indent=4, sort_keys=True))

course = models.execute_kw(db, uid, password,
                          'academy.course', 'search',
                          [[('name', '=', 'ACCOUNTING 200')]])
print("ACCOUNTING COURSE:")
print(json.dumps(course, indent=4, sort_keys=True))

session_fields = models.execute_kw(db, uid, password,
                                  'academy.session', 'fields_get',
                                  [], {'attributes': ['string', 'type', 'required']})
print("academy.session MODEL FIELDS:")
print(json.dumps(session_fields, indent=4, sort_keys=True))

new_session = models.execute_kw(db, uid, password,
                               'academy.session', 'create',
                               [
                                   {
                                       'course_id': course[0],
                                       'duration': 5,
                                   }
                               ])
print("NEW SESSION:")
print(new_session)