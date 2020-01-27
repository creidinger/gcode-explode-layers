import os
import sys

# open a gcode file and split it into several files
gcode_file = './assets/cubelocal.gcode'


def explode_gcode_layers(file):
    """Split .gcode file into separate layers"""

    with open(gcode_file, 'r') as f:
        layers = 1
        for line in f:
            layer_file = './assets/layers/layer_' + \
                str('%06d' % layers) + '.gcode'
            with open(layer_file, 'a') as lf:
                lf.write(line)
            # if there is a 'z' change, increate the layers counter
            if "G1 Z" in line:
                print(line)
                layers = layers + 1


explode_gcode_layers(gcode_file)
