from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


def output_parser(cmd_output):
    new_output = {"hostname": "", "connected": "", "time": ""}
    output_list = cmd_output.split(" ")
    new_output["hostname"] = output_list[1]
    if int(output_list[output_list.index("Received") + 2][0]) > 0:
        new_output["connected"] = True
    else:
        new_output["connected"] = False
    new_output["time"] = int(output_list[output_list.index("Average") + 2][0])
    return new_output


@app.route('/api/ip/<hostname>')
def ping_ip(hostname):
    cmd = os.popen("ping " + hostname).read()
    return jsonify(output_parser(cmd))


@app.route('/api/ips/<hostnames>')
def ping_ips(hostnames):  # put application's code here
    results = []
    for host in hostnames.split(','):
        cmd = os.popen("ping " + host).read()
        results.append(cmd)
    return results


if __name__ == '__main__':
    app.run()
