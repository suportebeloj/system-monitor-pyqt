#!/bin/bash

source venv/bin/activate

pyside6-rcc ui/compiled/resource.qrc -o resource_rc.py