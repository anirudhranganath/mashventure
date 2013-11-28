import httplib
import urllib
import csv_helper
import config
import xml.etree.ElementTree as ET


def ridb_fetch():
    con = httplib.HTTPConnection("ridb.recreation.gov")
    con.request("GET", "/webservices/RIDBServiceNG.cfc?method=getAllRecElementsForOrgID&orgID=-1")
    response = con.getresponse()
    f1 = open(config.RIDB_DATA_XML_PATH, 'wb')
    f1.write(response.read())
    f1.close()


def ridb_convert():
    tree = ET.parse(config.RIDB_DATA_XML_PATH)
    rec_info = []
    columns = []
    for rec_area in tree.findall('.//{http://www.recreation.gov/architecture/}RecArea'):
        rec_area_info_tags = rec_area.getchildren()
        rec_info_hash = {}
        for rec_area_info in rec_area_info_tags:
            rec_info_hash[rec_area_info.tag] = rec_area_info.text.encode('utf-8').strip() if rec_area_info.text is not None else ''
            if rec_area_info.tag not in columns:
                columns.append(rec_area_info.tag)
        rec_info.append(rec_info_hash)
    csv_helper.write_list_of_dict_to_csv(config.RIDB_DATA_CSV_PATH, rec_info, columns)


if __name__ == '__main__':
    #ridb_fetch()
    ridb_convert()