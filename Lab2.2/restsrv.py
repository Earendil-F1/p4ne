import glob
from flask import Flask, request

DIR = 'C:/Users/ap.lebedev/Seafile/Обучение/p4ne_training/config_files'

app = Flask(__name__)

@app.route('/')
def mainpage():
    return ('<a href=\"%s%s\">%s</a><br/>' % (request.base_url, 'config', 'Devices'))

@app.route('/config')
def print_hostnames():
    hlist = ''
    flist = glob.glob(DIR + '/*.txt')
    for f in flist:
        filename = (f.split('\\')[1]).replace('.txt', '')
        hlist += ('<a href=\"%s/%s\">%s</a><br/>' % (request.base_url, filename, filename))
    return hlist

@app.route('/config/<hostname>')
def print_ipaddresses(hostname):
    target = []
    with open(DIR + '/' + hostname + '.txt') as file:
        for line in file:
            if ('ip address' in line and '.' in line):
                if (('dhcp' not in line) and ('no' not in line)):
                    line = line.strip('\r\n')
                    if (line not in target):
                        target.append(line)

    iplist = ''
    for ipaddr in target:
        iplist += ipaddr + '<br>'

    iplist += ('<br> Unique ip addresses found: %s' % (len(target)))
    return iplist

if __name__ == '__main__':
    app.run(debug=True)


