import subprocess
import os

if '.app' in os.path.dirname(os.path.abspath(__file__)):
	PATH = os.path.dirname(os.path.abspath(__file__)).split('lib')[0]
	SCRIPTS_DIR = PATH + 'scripts'
else:
	SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'scripts'

def run_script(script_name):
	cmd = os.sep.join([SCRIPTS_DIR, script_name])
	pipe = subprocess.Popen([cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = pipe.communicate()
	if err:
		return 'Error: %s' % str(err)
	return out

def wifi_cycler():
	return run_script('wifi_cycler.sh')

def router_reboot():
	return run_script('power_cycle.sh')

def check_ping():
	return run_script('check_ping.sh')	