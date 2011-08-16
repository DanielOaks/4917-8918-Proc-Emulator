#!/usr/bin/env python3

from .unsw4917 import processor as microprocessor

class processor(microprocessor):
    name = 'unsw8918'
    extension = '8918'
    
    def __init__(self):
        microprocessor.__init__(self)
        self.bitlength = 8
        self.instruction_codes['24'] = (self.ins_print_ascii, 2)
    
    def ins_print(self):
        print(self.memory_locations[self.registers['ip'] - 1], end='')
    
    def ins_print_ascii(self):
        print(chr(self.memory_locations[self.registers['ip'] - 1]), end='')