#!/usr/bin/env python3

class microprocessor:
    name = 'microprocessor'
    
    def __init__(self):
        self.memory_locations = []
        self.registers = {}
        self.instruction_codes = {}
        self.bitlength = 0
    
    
    def initialise(self):
        self.clear_registers()
        self.clear_memory_locations()
    
    
    def clear_registers(self):
        for key in self.registers:
            self.registers[key] = 0
    
    def clear_memory_locations(self):
        self.memory_locations = []
        for i in range(0, self.bitlength ** 2):
            self.memory_locations.append(0)
    
    
    def run_program(self):
        while 1:
            self.step_program()
    
    def step_program(self):
        ...
    
    
    def load_program(self, path=None):
        ...