# BasilPi
[![Build Status](https://travis-ci.org/arunderwood/BasilPi.svg?branch=master)](https://travis-ci.org/arunderwood/BasilPi)
[![Code Climate](https://codeclimate.com/github/arunderwood/BasilPi/badges/gpa.svg)](https://codeclimate.com/github/arunderwood/BasilPi)
[![Test Coverage](https://codeclimate.com/github/arunderwood/BasilPi/badges/coverage.svg)](https://codeclimate.com/github/arunderwood/BasilPi/coverage)

Automated system for growing basil indoors.  Powered with Python and Raspberry Pi.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Goals](#goals)
  - [Inputs](#inputs)
  - [Outputs](#outputs)
- [Future](#future)
- [Testing](#testing)
- [Dependencies](#dependencies)
  - [Raspbian](#raspbian)
  - [Python](#python)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Goals

This project aims to automate the task of growing plants indoors.  If a reoccurring task can be automated, it should be.  If it cannot be automated, an alert should be fired to tell a human to perform the task.

### Inputs
_Information to be collected_
  * Temperature of the enclosure
  * Humidity of the enclosure
  * Soil moisture of the planter

### Outputs
_Actions to be taken based on inputs or schedule_
  * Toggle fan based on humidity and temperature
      - Use a small fan to push air out of the enclosure to control humidity and temperature.  Controlled amounts of air turbulence are also required to encourage stronger plant stem growth.  Without air movement, the plant will eventually collapse under its own weight.
  * Toggle lights on and off based on schedule
      - Plants need light.  'Nuff said.
  * __FUTURE__ Water pump to add water to the planter, triggered by low soil moisture
      - Automate the process of water the planter.  There will a bucket of similar container to hold water in reserve.  When triggered, the pump pulls water from the reservoir and mist it on the plants.  The fan should be disabled while the pump is on to prevent spraying water out of the enclosure.

## Future
_Random stuff that may or may not make it in in the future_

* The ability to read all configuration from a YAML file
* Main loop
    * Implement [scheduler](https://docs.python.org/3/library/sched.html) that can run various actions such as poll sensors and trigger functions.
    * [Argument acceptance](https://pypi.python.org/pypi/begins)
* Publish as a package (investigate [Flit](https://flit.readthedocs.io/en/latest/flit_ini.html).
* [Colored logging](https://coloredlogs.readthedocs.io/en/latest/)
* Cloud integration
    - Data is synchronized to AWS for altering, monitoring, and reporting

## Testing

Certain libraries such as _Adafruit_Python_DHT_ and _gpiozero_ do not function on platforms that are not RaspberryPis.  This causes tests to fail when they are run on an x86 machine or on TravisCI.  To get around this, stubs that emulate the functionality that needs to be tested in those libraries should be entered into the `lib/` directory.  Those libraries with this restriction should then be called in a way similar to:

```
# If we're not running on a Raspberry, use a GPIO stub so we can still get some coding done
from platform import processor
if processor() == 'x86_64' or 'i386':
    from lib.gpio_stub import LED
else:
    from gpiozero import LED  # pylint: disable=import-error
```

## Dependencies

### Raspbian

- Python 3.6 (Python 2.7 will be supported until it becomes inconvenient)
- `sudo adduser [USERNAME] gpio`
- `sudo adduser [USERNAME] i2c`

### Python

- [Adafruit_Python_DHT](https://github.com/adafruit/Adafruit_Python_DHT)
- [gpiozero](https://github.com/RPi-Distro/python-gpiozero)
