from setuptools import setup

APP = ['WhyFi.py']
APP_NAME = 'WhyFi'
DATA_FILES = [
	'scripts',
	'icons'
]
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icons/app_icon.icns',
    'plist': {
        'LSUIElement': True,
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "WiFi Utilities",
        'CFBundleIdentifier': "com.oztamir.osx.whyfi",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': "Copyright 2016, Oz Tamir, All Rights Reserved"
    },
    'packages': ['rumps'],
}

setup(
	name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)