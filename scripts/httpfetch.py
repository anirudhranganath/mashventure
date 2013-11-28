import httplib
import urllib
import config

con = httplib.HTTPConnection("ridb.recreation.gov")
con.request("GET", "/webservices/RIDBServiceNG.cfc?method=getAllRecElementsForOrgID&orgID=-1")
response = con.getresponse()
f1 = open(config.RIDB_DATA_XML_PATH,'wb')
f1.write(response.read())
f1.close()