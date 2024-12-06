import shutil
import rumps


class FreeSpace(rumps.App):
    def __init__(self):
        super(FreeSpace, self).__init__("FreeSpaceApp")
        # rumps.debug_mode(True)

        self.check_free_space = rumps.Timer(self.show_space, 10)
        self.check_free_space.start()

    def show_space(self, _):
        total, used, free = shutil.disk_usage("/")
        self.title = (
            f"{round(free / (2 ** 30), 1)} / {round(total / (2 ** 30), 1)} GB"
        )


if __name__ == "__main__":
    FreeSpace().run()
