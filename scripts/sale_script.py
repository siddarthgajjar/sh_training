from xmlrpc import client

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
                                 'sale.order', 'check_access_rights',
                                 ['write'], {'raise_exception': False})
print("MODEL ACCESS:")
print(model_access)

draft_quotes = models.execute_kw(db, uid, password,
                                'sale.order', 'search',
                                [[('state', '=', 'draft')]])
print("DRAFT QUOTES:")
print(draft_quotes)

if_confirmed = models.execute_kw(db, uid, password,
                                'sale.order', 'action_confirm',
                                [draft_quotes])
print("DRAFT QUOTES HAVE BEEN CONFIRMED:")
print(if_confirmed)

confirmed_quotes = models.execute_kw(db, uid, password,
                                     'sale.order', 'search',
                                     [[('state', '=', 'sale')]])
print("CONFIRMED QUOTES/ SALES:")
print(confirmed_quotes)

