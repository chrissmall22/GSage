#!/usr/bin/python

"""
Checks to see if a network exists on an Open Stack cluster
If it doesn't create it
"""

import logging
from keystoneclient.v2_0 import client
from neutronclient.neutron import client as neutronclient

class Openstack(object):

	# Turn on debug logging
	#logging.basicConfig(level=logging.DEBUG)

 # Get the catalog from keystone url
 def get_token(url, user, pw, tenant):
	
	keystone = client.Client(username=user, password=pw, tenant_name=tenant, auth_url=url)
	auth_ref = keystone.auth_ref
	
	return auth_ref
	
 def get_serviceid(token, serv_type):
 	keystone = client.Client(auth_ref=token)
 	serv = keystone.services.list()
 	for service in serv:
 		if serv_type == service.type:
 			return service.id
 	return	


 def get_endpoint_url(token,serv_type):
	
	serv_id = get_serviceid(token,serv_type)
	
	keystone = client.Client(auth_ref=token)
	endpoints = keystone.endpoints.list()
	for endpoint in endpoints:
 		if serv_id == endpoint.service_id:
 			return endpoint.publicurl
	
	return 
	
	
 def get_networks(n_url,token):

	neutron = neutronclient.Client('2.0', endpoint_url=n_url, token=token)
	pprint(neutron)
	networks = neutron.list_networks(name='LSST')

	return networks


