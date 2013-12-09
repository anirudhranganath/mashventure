from SPARQLWrapper import SPARQLWrapper, SPARQLWrapper2, JSON
import querier

#Given rec area name fetch all data
def get_recarea_details_from_name(name):
    activity_query = 'prefix mvac: <http://mashventure.com/ont/activity/> \
                prefix mvrec: <http://mashventure.com/ont/rec/> \
                SELECT ?ActivityName WHERE \
                {?rec mvrec:RecAreaName "%s". \
                ?rec mvrec:hasActivity ?act. \
                ?act mvac:RecActivityName ?ActivityName.}'%name
    results = querier.query(activity_query)
    activity_list = []
    for binding in results.bindings :
        activity_list.append(binding[u"ActivityName"].value)
    rec_area_query = 'prefix mvac: <http://mashventure.com/ont/activity/> \
                prefix mvrec: <http://mashventure.com/ont/rec/> \
                SELECT ?pred ?val WHERE \
                {?rec mvrec:RecAreaName "%s". \
                ?rec ?pred ?val.}'%name
    results = querier.query(rec_area_query)
    activity_details = {}
    for binding in results.bindings :
        #print "%s %s" % (binding[u"pred"].value.split('/')[-1], binding[u"val"].value)
        key = binding[u"pred"].value.split('/')[-1]
        value = binding[u"val"].value
        if key in activity_details.keys():
            if activity_details[key].__class__ == list:
                if value.__class__ == list:
                    activity_details[key] = [activity_details[key]]
                activity_details[key].append(value)
            else:
                activity_details[key] = [activity_details[key], value]
        else:
            activity_details[key] = value
    activity_details["activities"] = activity_list
    return(activity_details)