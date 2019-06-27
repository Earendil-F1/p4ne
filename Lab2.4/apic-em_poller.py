import requests, json
from flask import Flask, render_template, jsonify

app = Flask(__name__)
ticket = "ST-6006-UraAiLlRxKbqjwUVAjCG-cas"
controller = "devnetapi.cisco.com/sandbox/apic_em"

def new_ticket():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    payload = {"username": "devnetuser", "password": "Cisco123!"}
    header = {"content-type": "application/json"}
    r = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    return r.json()['response']['serviceTicket']

@app.route('/')
def index():
    return render_template('topology.html')

@app.route('/api/topology')
def print_topology():
    url = "https://%s/api/v1/topology/physical-topology" % controller
    header = {"content-type": "application/json", "X-Auth-Token": ticket}
    response = (requests.get(url, headers=header, verify=False)).json()['response']
    return jsonify(response)

@app.route('/api/ippool')
def print_ippool():
    url = "https://%s/api/v1/ippool" % controller
    header = {"content-type": "application/json", "X-Auth-Token": ticket}
    response = (requests.get(url, headers=header, verify=False)).json()['response']
    return jsonify(response)

#ticket = new_ticket()
print('Current ticket: %s' % ticket)

if __name__ == '__main__':
    app.run(debug=True)
