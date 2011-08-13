#!/usr/bin/env python3

from microprocessors.unsw4917 import processor

custom_processor = processor()
custom_processor.initialise()
custom_processor.load_program('example.mc')
#print(custom_processor.memory_locations)

custom_processor.run_program()