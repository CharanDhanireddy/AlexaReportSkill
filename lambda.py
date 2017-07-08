from __future__ import print_function

import urllib2
import json

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()
def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill 
    """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "ReportIntent":
        return Report_status(intent, session)
    elif intent_name == "AnyIntent":
        return any_status(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.StopIntent":
        return close()
    else:
        raise ValueError("Invalid intent")


# --------------- Functions that control the skill's behavior ------------------

def close():
    session_attributes = {}
    card_title = "Closing"
    speech_output = "Bye Bye!"
    reprompt_text = ""
    should_end_session = True

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_welcome_response():
    session_attributes = {}
    card_title = "Good Morning"
    speech_output = "Hi Josey, What do you want to know?"

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Didn't you hear me!"
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def any_status(intent,session):
    # Here the URLs cannot be given to public use, but any URL in JSON format should
    # work given that proper changes are made in the subsequent code
	
    req = urllib2.Request("URL1")
    resp = urllib2.urlopen(req)
    datati = json.loads(resp.read())
    
    req = urllib2.Request("URL2")
    resp = urllib2.urlopen(req)
    datasmc = json.loads(resp.read())
    
    req = urllib2.Request("URL3")
    resp = urllib2.urlopen(req)
    datasm = json.loads(resp.read())
    
    date = datasm[0]["last_updated"]
    avg_eve = datasm[1]["average_events_per_second"]
    tot_eve = datasm[2]["events"]
    eve_to_alert = datasm[3]["events_contributing_to_alerts"]
    tot_alert = datasm[4]["alerts"]
    tot_pos = datasm[5]["true_positive_alerts"]
    high_prio = datasm[6]["high_priority_incidents"]
    
    
    tot_vul = datati[0]["Reported Vulnerabilities "]
    crit_vul = datati[1][0]["Critical"]
    hi_vul = datati[1][1]["High"]
    med_vul = datati[1][2]["Medium"]
    
    aff_vendor1 = datati[2]["Most Affected Vendors "][0]["Vendor name"]
    aff_vendor2 = datati[2]["Most Affected Vendors "][1]["Vendor name"]
    aff_vendor3 = datati[2]["Most Affected Vendors "][2]["Vendor name"]
    
    top_mal1 = datati[3]["Top Malware By Reported Indicators"][0]["Malware Name"]
    top_mal2 = datati[3]["Top Malware By Reported Indicators"][1]["Malware Name"]
    top_mal3 = datati[3]["Top Malware By Reported Indicators"][2]["Malware Name"]
    
    risk = datasmc[0]["Operational Risk"]
    reliability = datasmc[1]["Operational Reliability"] 
    efficiency = datasmc[2]["Operational Efficiency"]

    speech_output = ""
    re = intent['slots']['data']['value']
    
    if re == "vulnerabilities":
        speech_output = "Number of vulnerablities are %s." %(tot_vul)
    elif re == "critical":
        speech_output = "Number of critical vulnerablities are %s." %(crit_vul)
    elif re == "high":
        speech_output = "Number of high risk vulnerablities are %s." %(hi_vul)
    elif re == "medium":
        speech_output = "Number of medium risk vulnerablities are %s." %(med_vul)
    elif re == "vendors":
        speech_output = "Most affected vendors are %s, %s and %s." %(aff_vendor1, aff_vendor2, aff_vendor3)
    elif re == "malwares":
        speech_output = "Top Malware By Reported Indicators are %s, %s and %s." %(top_mal1, top_mal2, top_mal3)
    elif re == "average events":
        speech_output = "Average events per second are %s." %(avg_eve)
    elif re == "total events":
        speech_output = "Total number of events are %s." %(tot_eve)
    elif re == "events contributing to alerts":
        speech_output = "Number of  are events contributing to alerts %s." %(eve_to_alert)
    elif re == "alerts":
        speech_output = "Number of alerts are %s." %(tot_alert)
    elif re == "true positive alerts":
        speech_output = "Number of true positive alerts are %s." %(tot_pos)
    elif re == "high priority incidents":
        speech_output = "Number of high priority incidentses are %s." %(high_prio)
    elif re == "operational efficiency":
        speech_output = "Operational efficiency percentage is %s." %(efficiency)
    elif re == "operational reliability":
        speech_output = "Operational reliability percentage is %s." %(reliability)
    elif re == "operational risk":
        speech_output = "Operational risk percentage is %s." %(risk)

    return build_response({}, build_speechlet_response(
        "I am saying something", speech_output, "", False))


def Report_status(intent, session):

    
    req = urllib2.Request("URL1")
    resp = urllib2.urlopen(req)
    datati = json.loads(resp.read())
    
    req = urllib2.Request("URL2")
    resp = urllib2.urlopen(req)
    datasmc = json.loads(resp.read())
    
    req = urllib2.Request("URL3")
    resp = urllib2.urlopen(req)
    datasm = json.loads(resp.read())
    
    date = datasm[0]["last_updated"]
    avg_eve = datasm[1]["average_events_per_second"]
    tot_eve = datasm[2]["events"]
    eve_to_alert = datasm[3]["events_contributing_to_alerts"]
    tot_alert = datasm[4]["alerts"]
    tot_pos = datasm[5]["true_positive_alerts"]
    high_prio = datasm[6]["high_priority_incidents"]
    
    
    tot_vul = datati[0]["Reported Vulnerabilities "]
    crit_vul = datati[1][0]["Critical"]
    hi_vul = datati[1][1]["High"]
    med_vul = datati[1][2]["Medium"]
    
    aff_vendor1 = datati[2]["Most Affected Vendors "][0]["Vendor name"]
    aff_vendor2 = datati[2]["Most Affected Vendors "][1]["Vendor name"]
    aff_vendor3 = datati[2]["Most Affected Vendors "][2]["Vendor name"]
    
    top_mal1 = datati[3]["Top Malware By Reported Indicators"][0]["Malware Name"]
    top_mal2 = datati[3]["Top Malware By Reported Indicators"][1]["Malware Name"]
    top_mal3 = datati[3]["Top Malware By Reported Indicators"][2]["Malware Name"]
    
    risk = datasmc[0]["Operational Risk"]
    reliability = datasmc[1]["Operational Reliability"] 
    efficiency = datasmc[2]["Operational Efficiency"]

    speech_output = ""
    
    re=intent['slots']['portal']['value']
	
    
    if re == "security monitoring":
        speech_output = "Security Monitoring overview as of date %s is as following. average events per second are %s.total events are %s.Total events contributing to alerts are %s.  total number of alerts are %s. True Positive alerts are %s . High Priority incidents %s." %(date, avg_eve, tot_eve, eve_to_alert, tot_alert, tot_pos, high_prio)
    elif re == "security management":
        speech_output = "Security management report is as following. operational risk is %s. operational reliability is %s. operational efficiency is %s."  %(risk, reliability, efficiency)
    elif re == "threat intelligence":
        speech_output = "Threat Intelligence report is as following. total number of reported vulnerabilities are %s. Out of %s, %s are critical, %s are high, %s are medium Vulnerabilities. Most affected vendors are %s, %s and %s .Top Malware By Reported Indicators are %s, %s and %s" %(tot_vul, tot_vul, crit_vul, hi_vul, med_vul, aff_vendor1, aff_vendor2, aff_vendor3, top_mal1, top_mal2, top_mal3)
    
        
    return build_response({}, build_speechlet_response(
        "I am saying something", speech_output, "", False))


# --------------- Helpers that build all of the responses ----------------------


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
