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
    print("Found: " + device.name)

    device_name = device.name.replace("Razer", "").strip()
    device_type = device.type
    lsusb = str(hex(device._vid))[-4:] + ":" + str(hex(device._pid))[-4:]
    lsusb = lsusb.replace("x", "0").upper()

    # Prevent duplicates (wired/wireless sets) although PID is technically different
    if device_name.find("Wired") != -1:
        continue
    elif device_name.find("Wireless") != -1:
        device_name = device_name.replace("(Wireless)", "").strip()

    # Get and validate URLs
    device_img_url = device.device_image

    if not device_img_url:
        print("Missing image URL: " + device_name)
        device_img_url = "img/placeholder.png"

    parsed_devices.append({
        "name": device_name,
        "type": device_type,
        "image_url": device_img_url,
        "vid": lsusb.split(":")[0],
        "pid": lsusb.split(":")[1]
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
        f.write('\n')
