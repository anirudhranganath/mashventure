import httplib
import urllib

con = httplib.HTTPConnection("ridb.recreation.gov")
con.request("GET", "/webservices/RIDBServiceNG.cfc?method=getAllRecElementsForOrgID&orgID=-1")
response = con.getresponse()
f1 = open('/home/anirudh/548/data/ridbData.xml','wb')
f1.write(response.read())
f1.close()