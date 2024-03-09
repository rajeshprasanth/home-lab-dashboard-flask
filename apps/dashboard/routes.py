from flask import Blueprint, render_template, jsonify, request,abort
import subprocess
import os
import platform



routes_bp = Blueprint("routes_bp", __name__)


category_names = {
"Network": "network", 
"Remote Access": "remote_access", 
"Infrastructure": "infrastructure",
"Storage":"storage",
"Virtual Machines":"virtual_machines",
"Service Monitor":"service_monitor"
}

host_data = [
  {
    "ipaddress": "192.168.1.1",
    "hostname": "wlsrt.inet0",
    "fqdn": "wlsrt.inet0.internal.das",
    "comment": "Management Connection"
  },
  {
    "ipaddress": "10.0.0.1",
    "hostname": "wlsrt.inet1",
    "fqdn": "wlsrt.inet1.internal.das",
    "comment": "Management Connection"
  },
  {
    "ipaddress": "10.0.0.2",
    "hostname": "sw0",
    "fqdn": "sw0.internal.das",
    "comment": "Management Connection"
  },
  {
    "ipaddress": "10.0.0.3",
    "hostname": "sw1",
    "fqdn": "sw1.internal.das",
    "comment": "Management Connection"
  },
  {
    "ipaddress": "10.0.0.10",
    "hostname": "PLPBTH001",
    "fqdn": "PLPBTH001.internal.das",
    "comment": "Ethernet Connection"
  },
  {
    "ipaddress": "10.0.0.11",
    "hostname": "PLPBTH001",
    "fqdn": "PLPBTH001.rm.internal.das",
    "comment": "Management Connection"
  },
  {
    "ipaddress": "10.0.0.20",
    "hostname": "PEPESX001",
    "fqdn": "PEPESX001.internal.das",
    "comment": "Ethernet Connection"
  },
  {
    "ipaddress": "10.0.0.21",
    "hostname": "PEPESX001",
    "fqdn": "PEPESX001.rm.internal.das",
    "comment": "Management Connection"
  },
  {
    "ipaddress": "10.0.0.30",
    "hostname": "PEPESX002",
    "fqdn": "PEPESX002.internal.das",
    "comment": "Ethernet Connection"
  },
  {
    "ipaddress": "10.0.0.40",
    "hostname": "PUPNAS001",
    "fqdn": "PUPNAS001.internal.das",
    "comment": "Ethernet Connection"
  },
  {
    "ipaddress": "10.0.0.50",
    "hostname": "PLPLBR001",
    "fqdn": "PLPLBR001.internal.das",
    "comment": "Ethernet Connection"
  },
  {
    "ipaddress": "10.0.0.60",
    "hostname": "PLPLBR002",
    "fqdn": "PLPLBR002.internal.das",
    "comment": "Ethernet Connection"
  },
  {
    "ipaddress": "10.0.0.70",
    "hostname": "PLPCLT001",
    "fqdn": "PLPCLT001.internal.das",
    "comment": "Ethernet Connection"
  },
  {
    "ipaddress": "10.0.0.80",
    "hostname": "PWPCLT001",
    "fqdn": "PWPCLT001.internal.das",
    "comment": "Ethernet Connection"
  },
  {
    "ipaddress": "10.0.1.1",
    "hostname": "PLVAPP001",
    "fqdn": "PLVAPP001.internal.das",
    "comment": "Ethernet Connection"
  },
  {
    "ipaddress": "10.0.1.2",
    "hostname": "DLVAPP001",
    "fqdn": "DLVAPP001.internal.das",
    "comment": "Ethernet Connection"
  },
  {
    "ipaddress": "10.0.1.3",
    "hostname": "PLVDBS001",
    "fqdn": "PLVDBS001.internal.das",
    "comment": "Ethernet Connection"
  },
  {
    "ipaddress": "10.0.1.4",
    "hostname": "DLVDBS001",
    "fqdn": "DLVDBS001.internal.das",
    "comment": "Ethernet Connection"
  }
] 
    

def check_status (hostdata):

    status_data = []
    
    param = '-n' if platform.system().lower()=='windows' else '-c'

    for host in hostdata:
        command = ['ping', param, '1', host['ipaddress']]
        
        ret = subprocess.call(command)
        
        if ret == 0:
            connection = True
        else:
            connection = False
            

        #Connection|Host Name|FQDN|IP Address|Status|Comment|Last Updated
        temp = {}
        temp={"connection":connection, 
        "hostname":host['hostname'],
        "fqdn":host['fqdn'],
        "ipaddress":host['ipaddress'],
        "comment":host['comment']
        }
        status_data.append(temp)
    return status_data

@routes_bp.route('/')
def home():
    return render_template('home_template.html',my_dict_1=category_names,title="Home")
    
@routes_bp.route('/network')
def network():
    return render_template('network_template.html',my_dict_1=category_names,title="Network Management")

@routes_bp.route('/remote_access')
def remote():
    return render_template('remote_access_template.html',my_dict_1=category_names,title="Remote Access Management")

@routes_bp.route('/infrastructure')
def infrastructure():
    return render_template('infrastructure_template.html',my_dict_1=category_names,title="Infrastructure Management")

@routes_bp.route('/storage')
def storage():
    return render_template('storage_template.html',my_dict_1=category_names,title="Storage Management")

@routes_bp.route('/virtual_machines')
def virtual_machines():
    return render_template('virtual_machines_template.html',my_dict_1=category_names,title="Virtual Machines Management")

@routes_bp.route('/service_monitor')
def service_monitor():
    return render_template('service_monitor_template.html',my_dict_1=category_names,my_dict_2=check_status(host_data),title="Service Monitor")