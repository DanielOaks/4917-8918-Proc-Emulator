#!/usr/bin/env python3

from .default import microprocessor

class processor(microprocessor):
    name = 'unsw4917'
    
    def __init__(self):
        microprocessor.__init__(self)
        self.bitlength = 4
        self.registers = {
            'ip' : 0, # instruction pointer
            'is' : 0, # instruction store
            'r0' : 0, # register 0
            'r1' : 0, # register 1
        }
        self.instruction_codes = {
            '0' : (self.ins_halt, 1),
        }
    
    
    def step_program(self):
        ...
    
    
    def ins_halt(self):
        print('halt')