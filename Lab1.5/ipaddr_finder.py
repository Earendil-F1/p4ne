import glob

DIR = 'C:/Users/ap.lebedev/Seafile/Обучение/p4ne_training/config_files'

flist = glob.glob(DIR + '/*.txt')
target = []
for f in flist:
    with open(f) as file:
        for line in file:
            if ('ip address' in line and '.' in line):
                if ((not 'dhcp' in line) and (not 'no' in line)):
                    line = line.strip('\r\n')
                    if (line not in target):
                        print (line)
                        target.append(line)

print ('\r\nUnique ip addresses found: %s' % (len(target)))