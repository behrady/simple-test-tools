# This is simple collection of REST Calls to verify APIs for openschema
# modify the api_endpoint and add your client certificate.

import requests
import json
import uuid
import time
api_endpoint = "https://magmahost.io/magma/v1/"


def get_all_gws():
    name = raw_input("Network Name to Get List of GWs: ")
    if name == "":
        return
    else:
        endpoint = api_endpoint + "networks/" + name + "/gateways"
        headers = {'Accept': 'application/json'}
        r = requests.get(endpoint,
                         verify=False,
                         cert='./cert.pem',
                         headers=headers)
        print(r.text)


def get_all_networks():
    r = requests.get(api_endpoint + "lte",
                     verify=False,
                     cert='./cert.pem',
                     stream=True)
    print(r.status_code, r.text)


def register_network():
    name = raw_input("Network Name to Register New Network: ")
    if name == "":
        return
    else:
        with open("./network.json", 'r+') as f:
            data = json.load(f)
            data['id'] = name
            data1 = json.dumps(data, indent=4)
            headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
            r = requests.post(api_endpoint+ "lte",
                              verify=False,
                              cert='./cert.pem',
                              headers=headers,
                              data=data1)
            print(r.status_code, r.text)


def register_gw():
    net_name = raw_input("Network Name to Register a GW: ")
    gw_name = raw_input("Gateway ID: ")
    if net_name == "" or gw_name == "":
        return
    else:
        endpoint = api_endpoint + "networks/" + net_name + "/gateways"
        with open("./gateway.json", 'r+') as f:
            data = json.load(f)
            data['id'] = gw_name
            data['device']['hardware_id'] = str(uuid.uuid4())
            data1 = json.dumps(data, indent=4)
            headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
            r = requests.post(endpoint,
                              verify=False,
                              cert='./cert.pem',
                              headers=headers,
                              data=data1)
            print(r.status_code, r.text)


# statically get an lte network detail
def get_network():
    r = requests.get(api_endpoint + "lte/test1",
                     verify=False,
                     cert='./cert.pem',
                     stream=True)
    print(r.status_code, " ", r.text)


def push_metrics():
    net_name = raw_input("Network Name to Push Test Metric: ")
    endpoint = api_endpoint + "networks/" + net_name + "/metrics/push"
    with open("./metric.json", 'r+') as f:
        data = json.load(f)
        data1 = json.dumps(data, indent=4)
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        r = requests.post(endpoint,
                          verify=False,
                          cert='./cert.pem',
                          headers=headers,
                          data=data1)
        print(r.status_code, r.text)


def get_metrics():
    net_name = raw_input("Network Name to get Metrics: ")
    metrics_name = raw_input("PromQL: ")
    endpoint = api_endpoint + "networks/" + net_name + "prometheus/query?query=" + metrics_name
    r = requests.get(endpoint,
                     verify=False,
                     cert='./cert.pem',
                     stream=True)
    print(r.status_code, r.text)


if __name__ == '__main__':
    get_all_networks()
    #get_all_gws()
    #register_network()
    #register_gw()
    #get_network()
    #push_metrics()
    #get_metrics()