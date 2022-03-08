#!/usr/bin/python3
#
# Enumerates the devices currently connected to the [fake driver] daemon.
#
# This shouldn't be ran directly. Run 'update-device-list.sh' instead.
#

import openrazer.client

data_file = "../_data/devices.yml"
devman = openrazer.client.DeviceManager()
devices = sorted(list(devman.devices), key=lambda device: device.name)

parsed_devices = []

print("\nNow updating devices.yml...\n")

for device in devices:
    device_name = device.name.replace("Razer", "").strip()
    device_type = device.type
    vid = str(hex(device._vid))[-4:].replace("x", "0").upper()
    pid = str(hex(device._pid))[-4:].replace("x", "0").upper()

    # Merge duplicates (wired/wireless/receiver)
    for suffix in ["(Wired)", "(Wireless)", "(Receiver)"]:
        if device_name.find(suffix) != -1:
            device_name = device_name.replace(suffix, "").strip()

    duplicate = False
    for _device in parsed_devices:
        if _device["name"] == device_name:
            _device["alias_ids"].append(f'"{vid}:{pid}"')
            duplicate = True

    if duplicate:
        print("Merging: " + device.name)
        continue

    # Validate image URLs
    device_img_url = device.device_image

    if not device_img_url:
        print("Missing image URL: " + device_name)
        device_img_url = "img/placeholder.png"

    print("Adding: " + device.name)
    parsed_devices.append({
        "name": device_name,
        "type": device_type,
        "image_url": device_img_url,
        "vid": vid,
        "pid": pid,
        "alias_ids": [],
    })

# Replace sections
with open("../_data/devices.yml", "w") as f:
    f.write("#\n# This file was auto-generated using the update-device-listings.py in the root of this repository.\n#\n")
    for device in parsed_devices:
        f.write('\n- name: "{0}"'.format(device["name"]))
        f.write('\n  type: "{0}"'.format(device["type"]))
        f.write('\n  image_url: "{0}"'.format(device["image_url"]))
        f.write('\n  vid: "{0}"'.format(device["vid"]))
        f.write('\n  pid: "{0}"'.format(device["pid"]))
        f.write('\n  alias_ids: [{0}]'.format(", ".join(device["alias_ids"])))
        f.write('\n')
