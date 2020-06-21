#!/usr/bin/env python3
#
# Enumerates the daemon's classes and uses those URLs
#

import os
import sys
import inspect
import re
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "openrazer", "daemon", "openrazer_daemon", "hardware"))
sys.path.append(lib_path)

# "openrazer" directory expected in parent folder.
import keyboards
import mouse
import mouse_mat
import core
import headsets
import accessory

razer_devices = []
parsed_devices = []

# Gather list of devices by looking in Razer* classes
for module in [keyboards, mouse, mouse_mat, core, headsets, accessory]:
    for inspection in inspect.getmembers(module):
        if inspection[0].startswith("Razer"):
            razer_devices.append(inspection[1])

# Used to remove plurals for consistency
device_types_from_daemon = {
    "keyboards": "keyboard",
    "headsets": "headset"
}

for device in razer_devices:
    daemon_type = inspect.getmodule(device).__name__
    print(device)

    try:
        device_type = device_types_from_daemon[daemon_type]
    except KeyError:
        device_type = daemon_type

    device_name = device.__name__
    lsusb = str(hex(device.USB_VID))[-4:] + ":" + str(hex(device.USB_PID))[-4:]
    lsusb = lsusb.replace("x", "0").upper()

    # Prevent duplicates (wired/wireless sets)
    if device_name.endswith("Wired"):
        continue
    elif device_name.endswith("Wireless"):
        device_name = device_name.replace("Wireless", "")

    # Get and validate URLs
    device_img_url = device.DEVICE_IMAGE

    if not device_img_url:
        print("Missing image URL for " + device_name)
        device_img_url = "img/placeholder.png"

    # Strip Razer name
    device_name = device_name.replace("Razer", "")

    # Clean up name from class
    device_name_ui = re.sub(r"(\w)([A-Z])", r"\1 \2", device_name)
    device_name_ui = device_name_ui \
                        .replace("Black Widow", "BlackWidow") \
                        .replace("Death Adder", "DeathAdder") \
                        .replace("Death Stalker", "DeathStalker") \
                        .replace("TE", "Tournament Edition") \
                        .replace("20", " 20") \
                        .replace("3500", " 3500") \
                        .replace("QH D", "QHD") \
                        .replace(" X", " X ") \
                        .replace("Abyssus1800", "Abyssus 1800") \
                        .replace("Kraken71", "Kraken 7.1") \
                        .replace("Adder3_5 G", "Adder 3.5G") \
                        .replace("Adv", "Advanced") \
                        .replace("HD K", "HDK")

    parsed_devices.append({
        "name": device_name_ui,
        "type": device_type,
        "image_url": device_img_url,
        "vid": lsusb.split(":")[0],
        "pid": lsusb.split(":")[1]
    })

# Replace sections
with open("_data/devices.yml", "w") as f:
    f.write("#\n# This file was auto-generated using the update-device-listings.py in the root of this repository.\n#\n")
    for device in parsed_devices:
        f.write('\n- name: "{0}"'.format(device["name"]))
        f.write('\n  type: "{0}"'.format(device["type"]))
        f.write('\n  image_url: "{0}"'.format(device["image_url"]))
        f.write('\n  vid: "{0}"'.format(device["vid"]))
        f.write('\n  pid: "{0}"'.format(device["pid"]))
        f.write('\n')
