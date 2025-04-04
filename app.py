from flask import Flask, render_template, request
import imaplib

app = Flask(__name__)

def check_imap_connection(host, port, username, password):
    try:
        mail = imaplib.IMAP4_SSL(host, port)
        mail.login(username, password)
        mail.logout()
        return True, "Connection successful"
    except Exception as e:
        return False, str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        host = request.form.get('host')
        port = request.form.get('port', 993)
        username = request.form.get('email')
        password = request.form.get('password')
        try:
            port = int(port)
        except ValueError:
            port = 993
        success, message = check_imap_connection(host, port, username, password)
        result = {"success": success, "message": message}
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
