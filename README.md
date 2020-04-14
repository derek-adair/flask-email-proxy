# flask-email-proxy
API that forwards contact submission forms to mailgun.  Before running make sure you have [signed up for mailgun](https://signup.mailgun.com/new/signup) and [configured](https://documentation.mailgun.com/en/latest/quickstart-sending.html) with your domains settings.

## Config
This script uses environment variables;

**MG_DOMAIN**:STRING - Find your list of domains [here](https://app.mailgun.com/app/sending/domains)
**MG_TO**:STRING - Where you want the emails to be sent to.
**MG_KEY**:STRING - os.getenv('MG_KEY', "REPLACE_ME_YOUR_KEY")
**FRONTEND_URI**:STRING - used for CORS whitelist

## To Run...
```
pip install -r requirements.txt && \
    python app.py
``
