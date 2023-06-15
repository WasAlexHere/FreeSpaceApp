from setuptools import setup

APP = ["FreeSpaceApp.py"]
OPTIONS = {
    "argv_emulation": True,
    "iconfile": "icon.icns",
    "plist": {
        "CFBundleShortVersionString": "0.2.0",
        "LSUIElement": True,
    },
    "packages": ["rumps"],
}

setup(
    app=APP,
    name="FreeSpaceApp",
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
    install_requires=OPTIONS["packages"]
)


#pip3 install py2app
#python setup.py py2app
