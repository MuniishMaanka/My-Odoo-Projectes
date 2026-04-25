from xmlrpc import client

# 1. Connection Details
url = 'https://muniishmaanka-my-odoo-projectes-16-academy-31249479.dev.odoo.com'
db = 'muniishmaanka-my-odoo-projectes-16-academy-31249479'
username = 'admin'
password = '0312c333bde4c6dd43adcdfc22fd4dfc9d7214fc'

print("--- 🛰️ Connecting to Odoo ---")
common = client.ServerProxy("{}/xmlrpc/2/common".format(url))

try:
    # 2. Authenticate
    uid = common.authenticate(db, username, password, {})
    if not uid:
        print("❌ AUTHENTICATION FAILED")
        print("Tip: Run 'echo $ODOO_DB_NAME' in your terminal to verify the DB name.")
    else:
        print(f"✅ AUTHENTICATED! Your UID is: {uid}")
        
        # 3. Connect to the Object Service
        models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

        # 4. Check Access Rights
        model_access = models.execute_kw(db, uid, password,
            'sale.order', 'check_access_rights',
            ['write'], {'raise_exception': False})
        print("Has Write Access:", model_access)

        # 5. Search for Draft Quotations
        draft_quotes = models.execute_kw(db, uid, password,
            'sale.order', 'search',
            [[['state', '=', 'draft']]])
        print("Draft Quote IDs:", draft_quotes)

        # 6. Confirm the Quotations
        if draft_quotes:
            if_confirmed = models.execute_kw(db, uid, password,
                'sale.order', 'action_confirm',
                [draft_quotes])
            print("Confirmation Result:", if_confirmed)
        else:
            print("No draft quotes found to confirm.")

except Exception as e:
    print(f"⚠️ An error occurred: {e}")