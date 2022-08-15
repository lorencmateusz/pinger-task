from flask import Flask, jsonify
import os
import subprocess

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/ip/<hostname>')
def ping_ip(hostname):
    cmd = os.popen("ping -c 4 " + hostname).read()
    return str(cmd)


@app.route('/api/ips/<hostnames>')
def ping_ips(hostnames):  # put application's code here
    results = []
    for host in hostnames.split(','):
        cmd = os.popen("ping -c 4 " + host).read()
        results.append(cmd)
    return results


if __name__ == '__main__':
    app.run()
