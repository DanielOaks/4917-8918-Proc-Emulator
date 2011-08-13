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
            '1' : (self.ins_add, 1),
            '2' : (self.ins_subtract, 1),
            '3' : (self.ins_increment_r0, 1),
            '4' : (self.ins_increment_r1, 1),
            '5' : (self.ins_decrement_r0, 1),
            '6' : (self.ins_decrement_r1, 1),
            '7' : (self.ins_bell, 1),
            '8' : (self.ins_print, 2),
            '9' : (self.ins_load_into_r0, 2),
            '10' : (self.ins_load_into_r1, 2),
            '11' : (self.ins_load_from_r0, 2),
            '12' : (self.ins_load_from_r1, 2),
            '13' : (self.ins_jump, 2),
            '14' : (self.ins_jump_if_0, 2),
            '15' : (self.ins_jump_if_not_0, 2),
        }
    
    
    def load_program(self, path=None):
        if path:
            program_file = open(path, 'r')
            ip = 0 # instruction pointer
            while 1:
                instruction = return_next_word(program_file)
                if instruction == '':
                    break
                self.memory_locations[ip] = int(instruction)
                ip += 1
                    
                
        
        else:
            ...
    
    
    def step_program(self):
        #print('    step_program:', self.registers['ip'], ',',  self.memory_locations[self.registers['ip']])
        self.registers['is'] = self.memory_locations[self.registers['ip']]
        if str(self.registers['is']) in self.instruction_codes:
            self.registers['ip'] = self.registers['ip'] + self.instruction_codes[str(self.registers['is'])][1]
            self.instruction_codes[str(self.registers['is'])][0]()
        
        else:
            print('unknown command, skipping:', self.registers['ip'], ',',  self.memory_locations[self.registers['ip']])
            self.registers['ip'] = self.registers['ip'] + 1
    
    
    def ins_halt(self):
        #print('halt')
        exit()
    
    def ins_add(self):
        #print('r0 = r0(%s) + r1(%s)' % (self.registers['r0'], self.registers['r1']))
        self.registers['r0'] = self.registers['r0'] + self.registers['r1']
    
    def ins_subtract(self):
        #print('r0 = r0(%s) - r1(%s)' % (self.registers['r0'], self.registers['r1']))
        self.registers['r0'] = self.registers['r0'] - self.registers['r1']
    
    def ins_increment_r0(self):
        #print('r0 = r0(%s) + 1' % (self.registers['r0']))
        self.registers['r0'] = self.registers['r0'] + 1
    
    def ins_increment_r1(self):
        #print('r1 = r1(%s) + 1' % (self.registers['r1']))
        self.registers['r1'] = self.registers['r1'] + 1
    
    def ins_decrement_r0(self):
        #print('r0 = r0(%s) - 1' % (self.registers['r0']))
        self.registers['r0'] = self.registers['r0'] - 1
    
    def ins_decrement_r1(self):
        #print('r1 = r1(%s) - 1' % (self.registers['r1']))
        self.registers['r1'] = self.registers['r1'] - 1
    
    def ins_bell(self):
        print('*bell*')
    
    def ins_print(self):
        print(self.memory_locations[self.registers['ip'] - 1])
    
    def ins_load_into_r0(self):
        #print('r0 =', self.memory_locations[self.registers['ip'] - 1])
        self.registers['r0'] = self.memory_locations[self.registers['ip'] - 1]
    
    def ins_load_into_r1(self):
        #print('r1 =', self.memory_locations[self.registers['ip'] - 1])
        self.registers['r1'] = self.memory_locations[self.registers['ip'] - 1]
    
    def ins_load_from_r0(self):
        #print('memory_location[%s] = r0(%s)' % (self.memory_locations[self.registers['ip'] - 1], self.registers['r0']))
        self.memory_locations[self.memory_locations[self.registers['ip'] - 1]] = self.registers['r0']
    
    def ins_load_from_r1(self):
        #print('memory_location[%s] = r1(%s)' % (self.memory_locations[self.registers['ip'] - 1], self.registers['r1']))
        self.memory_locations[self.memory_locations[self.registers['ip'] - 1]] = self.registers['r1']
    
    def ins_jump(self):
        #print('jumping from %s to %s' % (self.registers['ip'] - 2, self.memory_locations[self.registers['ip'] - 1]))
        self.registers['ip'] = self.memory_locations[self.registers['ip'] - 1]
    
    def ins_jump_if_0(self):
        if self.registers['r0'] == 0:
            #print('jumping from %s to %s' % (self.registers['ip'] - 2, self.memory_locations[self.registers['ip'] - 1]))
            self.registers['ip'] = self.memory_locations[self.registers['ip'] - 1]
        else:
            #print('not jumping from %s to %s' % (self.registers['ip'] - 2, self.memory_locations[self.registers['ip'] - 1]))
            ...
    
    def ins_jump_if_not_0(self):
        if self.registers['r0'] != 0:
            #print('jumping from %s to %s' % (self.registers['ip'] - 2, self.memory_locations[self.registers['ip'] - 1]))
            self.registers['ip'] = self.memory_locations[self.registers['ip'] - 1]
        else:
            #print('not jumping from %s to %s' % (self.registers['ip'] - 2, self.memory_locations[self.registers['ip'] - 1]))
            ...
    

def return_next_word(file):
    skip_whitespace = True
    word = ''
    while 1:
        char = file.read(1)
        if char == "'":
            while char != '\n':
                char = file.read(1)
                if char == '':
                    break
        if skip_whitespace:
            if char.isspace():
                ...
            elif char == '':
                break
            else:
                skip_whitespace = False
        if not skip_whitespace:
            if char.isspace():
                break
            elif char == '':
                break
            else:
                word += char
    return word