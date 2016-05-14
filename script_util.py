import subprocess
from os import sep

SCRIPTS_DIR = 'scripts' + sep

def run_script(script_name):
	cmd = '.%s%s%s' % (sep, SCRIPTS_DIR, script_name)
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