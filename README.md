# TinyPilot

[![CircleCI](https://circleci.com/gh/mtlynch/tinypilot.svg?style=svg)](https://circleci.com/gh/mtlynch/tinypilot) [![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](LICENSE) [![Reddit](https://img.shields.io/badge/reddit-join-orange?logo=reddit)](https://www.reddit.com/r/tinypilot)

## Overview

Turn your Raspberry Pi into a browser-based KVM.

![TinyPilot demo](https://raw.githubusercontent.com/kobrient/tinypilot/master/readme-assets/demo.gif)

## Features

* Video capture (HDMI/DVI/VGA)
* Keyboard forwarding
* Mouse forwarding
* Power and Reset switch control
* Fullscreen mode
* Paste text from clipboard

## Hardware requirements

* [Raspberry Pi 4](https://amzn.to/3fdarLM) (all variants work)
* [HDMI to USB dongle](https://amzn.to/2YHEvJN)
  * It has no brand name, but you can identify them by sight.
  * They're available for $10-15 on eBay.
* [USB-C to USB-A](https://www.amazon.com/AmazonBasics-Type-C-USB-Male-Cable/dp/B01GGKYN0A/) cable (Male/Male)
* [USB to TTL serial cable](https://amzn.to/3cVkuTT)
* [3 Amp USB wall charger](https://amzn.to/3hal8Ax)
* [microSD card](https://amzn.to/2VH0RcL) (Class 10, 8 GB or larger)
* [HDMI to HDMI cable](https://amzn.to/3gnlZwj)
  * Or \[other\] to HDMI, depending on how your target machine displays output.
* (Optional) [VGA to HDMI Adapter](https://amzn.to/30SZWYh)
  * If your target computer has VGA output, the above adapter is [confirmed to work](https://github.com/mtlynch/tinypilot/issues/76#issuecomment-664736402) with TinyPilot.

See ["TinyPilot: Build a KVM Over IP for Under $100"](https://mtlynch.io/tinypilot/#how-to-build-your-own-tinypilot) for a more detailed tutorial on how to assemble these parts to create a TinyPilot.

## GPIO Circuit

The simple circuit needed to provide Power and Reset control over the controlled PC. This assumes the PC under control uses a standard ATX style motherboard with a header exposed for front panel reset and power switches.

![GPIO Circuit](https://raw.githubusercontent.com/kobrient/tinypilot/master/readme-assets/tinypilot_gpio_circuit.png)

Pin 4 on the PC817 ICs should be connected to the respective positive pin for the front panel switch and Pin 3 should be connectected to the associated negative pins.

![ATX Front Panel Header](https://raw.githubusercontent.com/kobrient/tinypilot/master/readme-assets/ATX_MB_FP_pinout.png)


## Pre-requisites

* Raspberry Pi OS Stretch or later
* python3-venv

## Simple installation

You can install TinyPilot on a compatible Raspberry Pi in just two commands.

```bash
curl \
  --silent \
  --show-error \
  https://raw.githubusercontent.com/kobrient/tinypilot/master/quick-install | \
    bash - && \
  sudo reboot
```

The installation process:

* Creates a service account for TinyPilot with limited priviliges.
* Installs TinyPilot as a systemd service so it runs automatically on every boot.
* Installs TinyPilot's dependencies.

When your Pi reboots, you should be able to access TinyPilot by visiting your Pi hostname in the browser. For example, if your device is named `raspberrypi`:

* [http://raspberrypi/](http://raspberrypi/)

### Other installation options

* [Advanced installation options](https://github.com/mtlynch/tinypilot/wiki/Installation-Options#advanced-installation)
* [Remote installation via Ansible](https://github.com/mtlynch/tinypilot/wiki/Installation-Options#remote-installation)

## Developer installation

If you're interesting in contributing to TinyPilot, follow these instructions to install the required developer packages in your development environment:

```bash
python3.7 -m venv venv
. venv/bin/activate
pip install --requirement dev_requirements.txt
hooks/enable_hooks
```

To run TinyPilot's build scripts, run:

```bash
./dev-scripts/build-python
```

To enable TinyPilot's Git hooks, run:

```bash
./hooks/enable_hooks
```

To run TinyPilot on a non-Pi machine, run:

```bash
./dev-scripts/serve-dev
```
Then navigate to localhost:8000 in a web browser

## Options

TinyPilot accepts various options through environment variables:

| Environment Variable | Default      | Description |
|----------------------|--------------|-------------|
| `HOST`               | `0.0.0.0`    | Network interface to listen for incoming connections. |
| `PORT`               | `8000`       | HTTP port to listen for incoming connections. |
| `KEYBOARD_PATH`      | `/dev/hidg0` | Path to keyboard HID interface. |
| `MOUSE_PATH`         | `/dev/hidg1` | Path to mouse HID interface. |
| `DEBUG`              | undefined    | Set to `1` to enable debug logging. |

## Upgrades

To upgrade to the latest version of TinyPilot, run the upgrade script:

```bash
/opt/tinypilot/scripts/upgrade && sudo reboot
```

## Diagnostics

If you're having trouble with TinyPilot, you can run `/opt/tinypilot/dev-scripts/dump-logs` to print logs for all the software components related to TinyPilot. This log is useful if you [file a bug report](https://github.com/mtlynch/tinypilot/issues/new?assignees=&labels=&template=bug_report.md&title=).

You can read more details about the logs [in the wiki](https://github.com/mtlynch/tinypilot/wiki/Troubleshooting-and-Diagnostics).

## Security considerations

TinyPilot does not support authentication. You should only use TinyPilot on networks that you trust. Anyone who accesses the TinyPilot URL can shutdown or restart your Pi and type arbitrary commands into the device to which your Pi is connected.

If you need authentication, the simplest solution would be to adjust your Nginx configuration (included by default with the installation) to require [HTTP Basic Authentication](https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-http-basic-authentication/).

## Support

If this project is useful to you, consider making a financial contribution to support its development:

* [paypal.me/tinypilotkvm](https://paypal.me/tinypilotkvm)

## See also

* [TinyPilot Wiki](https://github.com/mtlynch/tinypilot/wiki): Guides for tasks related to TinyPilot.
* [TinyPilot Ansible Role](https://github.com/mtlynch/ansible-role-tinypilot): Use [Ansible](https://docs.ansible.com/ansible/latest/index.html) to install TinyPilot and all dependencies as a systemd service.

