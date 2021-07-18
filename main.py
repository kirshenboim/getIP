from flask import Flask
from flask import request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SERVER_NAME'] = "127.0.0.1:5000"
limiter = Limiter(app, key_func=get_remote_address)


# Return IP address of visitor
@app.route('/ip/')
@limiter.limit("10/minute")  # maximum of 10 requests per minute
def ip():
    my_ip = get_ip(parse_http_headers(request), request.remote_addr)
    return {"ip": my_ip}


def get_ip(headers, rmtip):
    for i in headers:
        # Look for 'X-Forwarded-For'
        if i == "X-Forwarded-For":
            # If 'X-Forwarded-For' contains a ','
            # since 'X-Forwarded-For' format is:
            # X-Forwarded-For: client, proxy1, proxy2
            # Must return the first value
            if ',' in headers[i]:
                return headers[i].split(', ')[0]
            else:
                return headers[i]

    # Else return request.remote_addr
    # if no 'X-Real-Ip' or 'X-Forwarded-For'
    return rmtip


# Loop over HTTP headers and return a dictionnary filled by them
def parse_http_headers(req):
    headers = {}

    for header in req.headers:
        headers[header[0]] = header[1]
    return headers


if __name__ == "__main__":
    app.run(host='0.0.0.0')
