#!/usr/bin/env python3

#from microprocessors.unsw4917 import processor
from microprocessors.unsw8918 import processor

custom_processor = processor()
custom_processor.initialise()

#custom_processor.load_program('examples/countdown.4917')
custom_processor.load_program('examples/countdown.8918')

#print(custom_processor.memory_locations)

custom_processor.run_program()