import os

##############################################
#       Application Constants
##############################################

# Query Params
SERVER_TAG = 'server'
DELLVE_TAG = 'dellve_port'
NETDATA_TAG = 'netdata_port'

# External API Endpoints used for dependency verification and form submission
NETDATA_SUFFIX = '/api/vi/data?chart=netdata.plugin_pythond_nv'
DVE_BENCH_LIST = ''# TODO: ammend as API is determined

# Local/Bluemix Deployment
DEFAULT_PORT = 8080
DEFAULT_HOST = '0.0.0.0'
CF_APP_ENV = 'VCAP_APP_PORT'

# Templates
TEMPLATE_DIR = 'templates/'
HOME_PAGE = 'portal_home.html'
SYS_PAGE = 'system_metrics.html'
BENCH_PAGE = 'benchmark.html'

# TODO: remove
WHITE_LIST = [ { 'server' : '10.157.26.8' , 'netdata_port' : '5555' } ]
