#!/usr/bin/env python3
#
# Enumerates the daemon's classes and uses those URLs
#

import os
import sys
import inspect
import re
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "razer-drivers", "daemon", "razer_daemon", "hardware"))
sys.path.append(lib_path)

# "razer-drivers" directory expected in parent folder.
import keyboards
import mouse
import mouse_mat
import core
import headsets
import mug

razer_devices = []
html_keyboards = ""
html_mice = ""
html_other = ""

# Gather list of devices by looking in Razer* classes
for module in [keyboards, mouse, mouse_mat, core, headsets, mug]:
    for inspection in inspect.getmembers(module):
        if inspection[0].startswith("Razer"):
            razer_devices.append(inspection[1])

for device in razer_devices:
    device_type = inspect.getmodule(device).__name__
    device_name = device.__name__

    # Prevent duplicates (wired/wireless sets)
    if device_name.endswith("Wired"):
        continue
    elif device_name.endswith("Wireless"):
        device_name = device_name.replace("Wireless", "")

    # Get and validate URLs
    store_url = device.RAZER_URLS["store"]
    device_img_url = device.RAZER_URLS["perspective_img"]

    if store_url == None:
        print("Missing store URL for " + device_name)
        store_url = ""

    if device_img_url == None:
        print("Missing image URL for " + device_name)
        device_img_url = "img/logo.png"

    # Strip Razer name
    device_name = device_name.replace("Razer", "")

    # Clean up name from class
    device_name_ui = re.sub(r"(\w)([A-Z])", r"\1 \2", device_name)
    device_name_ui = device_name_ui.replace("Black Widow", "BlackWidow") \
                        .replace("T E", "Tournament Edition") \
                        .replace("Death Stalker", "DeathStalker") \
                        .replace("TE", "Tournament Edition") \
                        .replace("Fire Fly", "Firefly") \
                        .replace("20", " 20") \
                        .replace("QH D", "QHD") \
                        .replace(" X", " X ") \
                        .replace("BlackWidow 2012", "BlackWidow Ultimate 2012 (Classic)") \
                        .replace("BlackWidow 2013", "BlackWidow Ultimate 2013") \
                        .replace("BlackWidow 2016", "BlackWidow Ultimate 2016") \
                        .replace("Deathadder", "DeathAdder") \
                        .replace("Kraken", "Kraken 7.1")

    def get_device_html(store_url, img_url, name):
        print("Adding " + name + "...")
        return \
        '                <div class="col-md-3 col-sm-4 device-icon">\n' \
        '                  <a href="{0}" target="_blank">\n' \
        '                    <div class="inner" style="background-image:url({1})"></div>\n' \
        '                    <h5>{2}</h5>\n' \
        '                  </a>\n' \
        '                </div>\n'.format(
            store_url, img_url, name)

    html_buffer = get_device_html(store_url, device_img_url, device_name_ui)

    if device_type == "keyboards":
        html_keyboards += html_buffer

    elif device_type in ["mouse", "mouse_mat"]:
        html_mice += html_buffer

    else:
        html_other += html_buffer

# Replace sections
with open("index.html") as f:
    raw_html = f.readlines()
index_html = "".join(raw_html)

def update_placeholders(html_data, placeholder_name):
    global index_html
    before_comment = "                <!-- START {0} -->".format(placeholder_name)
    after_comment = "                <!-- END {0} -->".format(placeholder_name)
    before = index_html.split(before_comment)
    after = index_html.split(after_comment)
    index_html = before[0] + before_comment + "\n" + html_data + "\n" + after_comment + after[1]

update_placeholders(html_keyboards, "KEYBOARD")
update_placeholders(html_mice, "MICE")
update_placeholders(html_other, "OTHER")

with open("index.html", "w") as f:
    f.writelines(index_html)
