import rumps
from script_util import *

# Check ping every 15 seconds
PING_INTERVAL=10

def ping_timer(menu_item):
    def update_function(timer):
        menu_item.title = 'Ping: %s' % str(check_ping())
    return rumps.Timer(update_function, PING_INTERVAL)

class WhyFi(rumps.App):
    def __init__(self):
        super(WhyFi, self).__init__(
            name="WhyFi",
            icon="icon.png"
            )
        self.ping_item = rumps.MenuItem("Ping: N/A")
        self.timer = ping_timer(self.ping_item)
        self.timer.start()

        ping_checks = rumps.MenuItem("Ping Checks")
        ping_checks.state = True

        self.menu = ["Wifi Power Cycle", "Reboot Router", self.ping_item, ping_checks]

    @rumps.clicked("Wifi Power Cycle")
    def wifi(self, _):
        wifi_cycler()
        rumps.notification("WhyFi", "Wifi Rebooted", "It might take a few seconds to reconnect")

    @rumps.clicked("Ping Checks")
    def ping_checks(self, sender):
        if sender.state:
            self.timer.stop()
            self.ping_item.title = 'Ping: OFF'
        else:
            self.timer.start()
        sender.state = not sender.state


    @rumps.clicked("Reboot Router")
    def router(self, _):
        msg = router_reboot()
        rumps.notification("WhyFi", "Router Rebooted", "Message: %s" % msg)

if __name__ == "__main__":
    WhyFi().run()