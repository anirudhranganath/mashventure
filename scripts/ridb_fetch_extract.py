import httplib
import urllib
import csv_helper
import sys
sys.path.append('../')
import config
import xml.etree.ElementTree as ET
import os

ridb_RecArea_csv = os.path.join(config.DATA_DIR_PATH,'ridb-EntityMedia.csv')

def ridb_fetch():
    con = httplib.HTTPConnection("ridb.recreation.gov")
    con.request("GET", "/webservices/RIDBServiceNG.cfc?method=getAllRecElementsForOrgID&orgID=128")
    response = con.getresponse()
    f1 = open(config.RIDB_DATA_XML_PATH, 'wb')
    f1.write(response.read())
    f1.close()


def ridb_extract_by_tag(tag):
    tree = ET.parse(config.RIDB_DATA_XML_PATH)
    rec_info = []
    columns = []
    for rec_area in tree.findall(tag):
        rec_area_info_tags = rec_area.getchildren()
        rec_info_hash = {}
        for rec_area_info in rec_area_info_tags:
            rec_info_hash[rec_area_info.tag] = rec_area_info.text.encode('utf-8').strip() if rec_area_info.text is not None else ''
            if rec_area_info.tag not in columns:
                columns.append(rec_area_info.tag)
        rec_info.append(rec_info_hash)
    csv_helper.write_list_of_dict_to_csv(ridb_RecArea_csv, rec_info, columns)


if __name__ == '__main__':
    #ridb_fetch()
    ridb_extract_by_tag('.//{http://www.recreation.gov/architecture/}EntityMedia')