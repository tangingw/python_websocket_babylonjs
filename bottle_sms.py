import androidhelper
import json
import time
from bottle import bottle
from bottle import run, request, response


app = Bottle()
droid = androidhelper.Android()


@app.route("/"):
def index():

    return "Hello World"


@app.route("/sms/read")
def read_sms():

    unread_sms = droid.smsGetMessages(True).result
    response.content_type = "application/json"

    return json.dumps(
        {
            "unread": unread_sms,
        }, indent=4, ensure_ascii=False
    )


@app.get("/sms/send")
def sms_get():

    return """
    <html>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My SMS Portal</title>
        <body>
            <h1>My SMS Portal</h1>
            <h2>Please enter the following details</h2>
            <form action="/sms/send" id="smsform" method="post">
                Phone Number: <input type="text", name="phone_number">
                <br>
                <br>
                <textarea rows="5" cols="40" name="smsContent" form="smsform">Enter message here...</textarea>
                <br>
                <input type="submit">
            </form>
            <p>
                Once you are done, please click submit button!
            </p>
        </body>
    </html>
    """


@app.post("/sms/send")
def sms_post():

    sms_phone = request.forms.get("phone_number")
    sms_content = request.forms.get("smsContent").strip("\r\n")

    status_code = droid.smsSend(sms_phone, sms_content)

    return json.dumps(
        {
            "phone_number": sms_phone,
            "sms_content": sms_content
        }
    )

run(app, host="0.0.0.0", port=8080)