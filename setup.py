from setuptools import setup

APP = ['WhyFi.py']
DATA_FILES = [
	'scripts',
	# 'scripts/wifi_cycler.sh',
	# 'scripts/check_ping.sh',
	'icon.png'
]
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)