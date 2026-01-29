class UtecBleLock:
    def __init__(self):
        self.capabilities = type("obj", (object,), {"bluetooth": True})()
        self.name = "Unknown"
        self.lock_status = "unknown"
        self.bolt_status = "unknown"
        self.battery = 0
        self.lock_mode = "normal"
        self.mute = False
        self.autolock_time = 0
        self.async_bledevice_callback = None
        self.uuid = None
        self.model = None
        
    @classmethod
    def from_json(cls, api_device):
        lock = cls()
        lock.name = api_device.get("name", "Unknown")
        lock.model = api_device.get("model", "Unknown")
        lock.uuid = api_device.get("uuid", None)
        
        params = api_device.get("params", {})
        
        # Parse battery (0-3 scale, convert to percentage)
        battery_level = params.get("battery", 0)
        battery_map = {0: 0, 1: 33, 2: 66, 3: 100}
        lock.battery = battery_map.get(battery_level, 0)
        
        # Parse lock status (is_locked: 1=locked, 2=unlocked)
        is_locked = params.get("is_locked", 2)
        lock.lock_status = "locked" if is_locked == 1 else "unlocked"
        lock.bolt_status = "engaged" if is_locked == 1 else "retracted"
        
        return lock

    async def async_update_status(self):
        # BLE update not implemented yet
        pass
