from xmlrpc import client

# 1. Connection Details
url = 'https://muniishmaanka-my-odoo-projectes-16-academy-31384971.dev.odoo.com'
db = 'muniishmaanka-my-odoo-projectes-16-academy-31384971'

# FIXED: Changed from 'admin' to the email seen in your Mitchell Admin profile
username = 'admin' 

# Ensure this matches your fresh API key exactly
password = 'admin'

# 2. Connect to the Common Service & Check Version
common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print("Odoo Version Info:", common.version())

# 3. Authenticate to get a UID (User ID)
uid = common.authenticate(db, username, password, {})
print("Authenticated UID:", uid)

# 4. Connect to the Object Service (The database interaction layer)
models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

# 5. Check Access Rights
# This checks if the user has permission to 'write' (edit) sale orders
model_access = models.execute_kw(db, uid, password,
    'sale.order', 'check_access_rights',
    ['write'], {'raise_exception': False})
print("Has Write Access:", model_access)

# 6. Search for Draft Quotations
# This returns a list of IDs for all Sale Orders in 'draft' state
draft_quotes = models.execute_kw(db, uid, password,
    'sale.order', 'search',
    [[['state', '=', 'draft']]])
print("Draft Quote IDs:", draft_quotes)

# 7. Confirm the Quotations
# This calls the Odoo method 'action_confirm' for all found IDs
if draft_quotes:
    if_confirmed = models.execute_kw(db, uid, password,
        'sale.order', 'action_confirm',
        [draft_quotes])
    print("Confirmation Result:", if_confirmed)
else:
    print("No draft quotes found to confirm.")