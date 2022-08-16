from flask import Flask, jsonify, request
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
        new_output["time"] = output_list[output_list.index("Average") + 2][0]
    else:
        new_output["connected"] = False
        new_output["time"] = "n/a"
    return new_output


@app.route('/api/ip/<hostname>')
def ping_ip(hostname):
    cmd = os.popen("ping " + hostname).read()
    return jsonify(output_parser(cmd))


@app.route('/api/ips/', methods=['POST'])
def ping_ips():  # put application's code here
    hostnames = request.json.get("hosts")
    results = []
    for i in hostnames:
        cmd = os.popen("ping " + i).read()
        results.append(output_parser(cmd))
    return jsonify(results)


if __name__ == '__main__':
    app.run()
