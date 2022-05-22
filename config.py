APP = {
    'APP_SETTINGS':'development',
    'APP_NAME':'FastAPI',
    'APP_IP':'0.0.0.0',
    'API_PORT':5000,
    'SECRET_KEY':'this_is_the_secret_key'
}

DB = {
    'URL' : '/sqlite.db'
}

CORS = {
    'ORIGINS' : ["*"], # not best practice, dont do this in prod
    'METHODS' : ["POST", "GET", "PUT", "DELETE"],
    'HEADERS' : ["*"]
}

DESC = '''
# API developed using FastAPI 🚀 Framework (Python 🐍)

### Basic CRUD API
DB used is sqlite 🗄️

**API response time is in second(s)**
'''
