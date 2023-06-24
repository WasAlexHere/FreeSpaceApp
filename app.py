import shutil
import rumps


class FreeSpace(rumps.App):
    def __init__(self):
        super(FreeSpace, self).__init__("FreeSpaceApp")
        # rumps.debug_mode(True)

        self.total, self.used, self.free = shutil.disk_usage("/")
        self.title = (
            f"{round(self.free / (2 ** 30), 1)} / {round(self.total / (2 ** 30), 1)} GB"
        )
        self.check_free_space = rumps.Timer(self.show_space, 2*3600)
        self.check_free_space.start()

    def show_space(self, _):
        self.title = (
            f"{round(self.free / (2 ** 30), 1)} / {round(self.total / (2 ** 30), 1)} GB"
        )


if __name__ == "__main__":
    FreeSpace().run()
