#!/usr/bin/env python3
"""Control Ultraloq lock via Bluetooth."""
import asyncio
import sys

from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from utecio.ble.lock import UtecBleLock
from utecio.api import UtecClient
from utecio import logger as liblogger

# Import credentials from config file
try:
    from config import EMAIL, PASSWORD, LOCK_NAME
except ImportError:
    EMAIL = "your@email.com"
    PASSWORD = "your_password"
    LOCK_NAME = "UL3-2ND"

bleak_scanner = BleakScanner()


async def async_bledevice_callback(address: str) -> BLEDevice:
    """Provide BLEDevice for the mac address."""
    if bleak_scanner:
        device = await bleak_scanner.find_device_by_address(address)
        return device
    return None


async def control_lock(lockname: str, action: str):
    """Control the lock - lock, unlock, or status."""
    # Enable debug output
    liblogger.setLevel(10)
    
    # Connect to web API and retrieve locks
    client = UtecClient(EMAIL, PASSWORD)
    ble_devices = await client.get_ble_devices()

    # Select lock based on name
    matching_locks = list(filter(lambda lock: lock.name == lockname, ble_devices))
    if not matching_locks:
        print(f"Error: Lock '{lockname}' not found!")
        print(f"Available locks: {[lock.name for lock in ble_devices]}")
        return

    lock: UtecBleLock = matching_locks[0]
    lock.async_bledevice_callback = async_bledevice_callback

    try:
        await bleak_scanner.start()
        
        if action == "status":
            print(f"Getting status for {lock.name}...")
            await lock.async_update_status()
            print(f"\n{'='*50}")
            print(f"Lock: {lock.name}")
            print(f"Model: {lock.model}")
            print(f"MAC: {lock.mac_uuid}")
            print(f"{'='*50}")
            print(f"Lock Status: {lock.lock_status}")
            print(f"Bolt Status: {lock.bolt_status}")
            print(f"Battery: {lock.battery}")
            print(f"Lock Mode: {lock.lock_mode}")
            print(f"Mute: {lock.mute}")
            print(f"Autolock Time: {lock.autolock_time} seconds")
            print(f"{'='*50}\n")
            
        elif action == "unlock":
            print(f"Unlocking {lock.name}...")
            await lock.async_unlock()
            print(f"✓ {lock.name} unlocked successfully!")
            
        elif action == "lock":
            print(f"Locking {lock.name}...")
            await lock.async_lock()
            print(f"✓ {lock.name} locked successfully!")
            
        else:
            print(f"Unknown action: {action}")
            print("Valid actions: status, lock, unlock")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await bleak_scanner.stop()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python control_lock.py [status|lock|unlock]")
        print("Example: python control_lock.py unlock")
        sys.exit(1)
    
    action = sys.argv[1].lower()
    asyncio.run(control_lock(LOCK_NAME, action))
