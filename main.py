#!/usr/bin/env python
import subprocess
import sys
import re
import webbrowser
import requests

def getBranch():
    output = subprocess.check_output('git rev-parse --abbrev-ref HEAD', shell=True)
    return output.split('\n')[0]

def getFilePathRelativeToRepo(branch, filename):
    cmd = 'git ls-tree --full-name --name-only {0} {1}'.format(branch, filename)
    output = subprocess.check_output(cmd)
    return output.split('\n')[0]

if __name__ == '__main__':
    output = subprocess.check_output('git remote -v', shell=True)
    # Check for no git repo
    if output == '':
        sys.exit('err: No remote provided')
    remotes = output.split('\n')

    # origin	git@github.com:dani-h/bash (fetch)
    # print remotes[0]
    reg = re.compile(r':(.+) ')
    match = reg.search(remotes[0])
    repo = match.group(1)

    baseUrl = 'https://github.com/'
    repoUrl = baseUrl + repo + '/tree' + '/' + getBranch()

    req = requests.get(repoUrl)
    if req.status_code == 404:
        sys.exit('Request returned 404, this branch might not exist remotely')


    # webbrowser.open(repoUrl)



