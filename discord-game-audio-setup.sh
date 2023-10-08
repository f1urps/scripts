#!/bin/bash

SOURCE_MIC=4
SINK_HEADPHONES=3

pactl load-module module-null-sink sink_name=Virtual1
pactl load-module module-loopback source=$SOURCE_MIC sink=Virtual1
pactl load-module module-loopback source=Virtual1.monitor sink=$SINK_HEADPHONES

