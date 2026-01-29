#!/usr/bin/env python3
"""Check lock status via API only (no BLE)."""
import asyncio
from utecio.api import UtecClient
from config import EMAIL, PASSWORD, LOCK_NAME

async def check_api_status():
    client = UtecClient(EMAIL, PASSWORD)
    devices_json = await client.get_json()
    
    for device in devices_json:
        if device["name"] == LOCK_NAME:
            sep = "="*50
            print(f"\n{sep}")
            print(f"Lock: {device['name']}")
            print(f"Model: {device['model']}")
            print(f"MAC: {device['uuid']}")
            print(sep)
            params = device["params"]
            is_locked = params.get("is_locked", 2)
            battery = params.get("battery", 0)
            status = "locked" if is_locked == 1 else "unlocked"
            print(f"Lock Status: {status}")
            print(f"Battery Level: {battery} (0=empty, 3=full)")
            print(f"WiFi Strength: {params.get('wifi_strength')} dBm")
            print(f"BLE Strength: {params.get('ble_strength')} dBm")
            print(f"Serial: {params.get('serialnumber')}")
            print(f"Firmware: {params.get('version')}")
            print(f"{sep}\n")
            break

if __name__ == "__main__":
    asyncio.run(check_api_status())
