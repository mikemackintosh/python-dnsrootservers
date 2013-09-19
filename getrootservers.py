#!/usr/bin/env python

"""
Resolved Address Verifier For Root Servers
"""

""" Imports """
import DNS
import urllib2
from BeautifulSoup import BeautifulSoup
from webscraping import common, download, xpath

""" Author Details """
__author__ = "Mike Mackintosh"
__copyright__ = "Copyright 2013"
__credits__ = ["Mike Mackintosh"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Mike Mackintosh"
__email__ = "m@zyp.io"
__status__ = "Production"

""" Set URL """
url = "http://www.root-servers.org/"
soup = BeautifulSoup(urllib2.urlopen(url))

""" Scrap the Page """
servers = soup.findAll('td', attrs ={'id':'server'})
operators = soup.findAll('td', attrs = {'id':'operator'})
ips = soup.findAll('td', attrs = {'id':'ips'})

""" Join The Finds """
for server, operator, ip in zip(servers,operators,ips):
    rootserver = (server.find('a') or server).contents[0]
    operator = operator.contents[0]
    ip = ip.contents[0].split(":")[1]

    """ Print Out What We Found """
    print '{0}.root-servers.org is operated by {1} and exists at {2}'.format(rootserver,operator,ip)
