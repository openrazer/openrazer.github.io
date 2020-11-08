#!/bin/bash -x
#
# Run this script after a new OpenRazer release. This will re-populate
# the device list according to the fake device.
#
# This will stop any existing OpenRazer daemon as the fake one is spawned.
#
# The script expects a clone of 'openrazer' adjacent to 'openrazer.github.io'
#

cd "$(dirname $0)"

if [ ! -d "../../openrazer/" ]; then
    echo "OpenRazer repository not found."
    exit 1
fi

# Stop any existing daemon
openrazer-daemon -s

# Create fake devices and start daemon
mkdir /tmp/{daemon_test,daemon_run,daemon_logs,daemon_test}
../../openrazer/scripts/create_fake_device.py --dest "/tmp/daemon_test" --non-interactive --all &
sleep 1
../../openrazer/daemon/run_openrazer_daemon.py -F --run-dir "/tmp/daemon_run" --log-dir "/tmp/daemon_logs" --test-dir "/tmp/daemon_test" &
sleep 2

# Update data files
./_write_devices.py

# Stop fake driver / daemon
kill $(jobs -p)
