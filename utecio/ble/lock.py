class UtecBleLock:
    def __init__(self):
        self.capabilities = type("obj", (object,), {"bluetooth": True})()
        self.name = "test"
        self.lock_status = "unlocked"
        self.bolt_status = "unlocked"
        self.battery = 100
        self.lock_mode = "normal"
        self.mute = False
        self.autolock_time = 0
        self.async_bledevice_callback = None

    @classmethod
    def from_json(cls, api_device):
        return cls()

    async def async_update_status(self):
        pass
