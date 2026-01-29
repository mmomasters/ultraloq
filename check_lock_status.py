import asyncio

from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from utecio.ble.lock import UtecBleLock
from utecio.api import UtecClient, logger as liblogger

# Import credentials from config file
try:
    from config import EMAIL, PASSWORD, LOCK_NAME
except ImportError:
    EMAIL = "your@email.com"  # Your Utec app username/email
    PASSWORD = "your_password"  # Your Utec App Password
    LOCK_NAME = "UL3-2ND"  # Replace with your lock name

bleak_scanner = BleakScanner()

async def async_bledevice_callback(address: str) -> BLEDevice:
    # we need to provide a valid BLEDevice for the mac address when asked, or return None
    # in Home Assistant we should call 'bluetooth.async_ble_device_from_address' to return the BLEDevice.
    if bleak_scanner:
        device = await bleak_scanner.find_device_by_address(address)
        return device
    return None

async def check_lock_status(lockname: str):
    # enable debug output
    liblogger.setLevel(10)
    # connect to webapi and retrieve locks
    client = UtecClient(EMAIL, PASSWORD)
    ble_devices = await client.get_ble_devices()

    # select a lock based on a known property (e.g. name)
    l5: UtecBleLock = list(filter(lambda lock: lock.name == lockname, ble_devices))[0]
    # register a callback to provide bleak BLEDevice objects
    l5.async_bledevice_callback = async_bledevice_callback
    try:
        # start the scanner for the BLEDevice callback
        await bleak_scanner.start()
        # update the lock status
        await l5.async_update_status()
        # print the status
        print(f"Lock Status: {l5.lock_status}")
        print(f"Bolt Status: {l5.bolt_status}")
        print(f"Battery: {l5.battery}")
        print(f"Lock Mode: {l5.lock_mode}")
        print(f"Mute: {l5.mute}")
        print(f"Autolock Time: {l5.autolock_time}")
    except Exception as e:
        print("Status check failed.", e)
    finally:
        # cleanup
        await bleak_scanner.stop()

if __name__ == "__main__":
    asyncio.run(check_lock_status(LOCK_NAME))
