class Amplifier():
    def __init__(self, ID, codes):
        self._systemID = [ID]
        self._state = codes.copy()
        self._copyOfState = list(codes)
        self._instructionPointer = 0
        self._output = ""
        self._input = 0
        self._newInput = None
        self._systemIDPointer = 0

    def reset(self):
        self._systemID[1] = 0
        self._instructionPointer = 0
        self._output = ""
        self._input = 0
        self._newInput = None
        self._systemIDPointer = 0
        self._state = list(self._copyOfState)

    def input(self, inputAmp):
        self._systemID.append(inputAmp)

    def computeOpCode(self, number ):
        return [number % 100, int(number/100)%10, int(number/1000)%10, int(number/10000)%10]

    def compute(self):
        while(self._state[ self._instructionPointer ] != 99):
            opCode = self.computeOpCode( self._state[ self._instructionPointer ] )
            if( opCode[0] == 1 ):
                operandA = self._state[ self._instructionPointer + 1 ]
                operandB = self._state[ self._instructionPointer + 2 ]
                pointerResult = self._state[ self._instructionPointer + 3 ]
                valueA = self._state[ operandA ] if not opCode[1] else operandA
                valueB = self._state[ operandB ] if not opCode[2] else operandB
                result = valueA + valueB
                self._instructionPointer += 4
                self._state[ pointerResult ] = result
            elif( opCode[0] == 2 ):
                operandA = self._state[ self._instructionPointer + 1 ]
                operandB = self._state[ self._instructionPointer + 2 ]
                valueA = self._state[ operandA ] if not opCode[1] else operandA
                valueB = self._state[ operandB ] if not opCode[2] else operandB
                pointerResult = self._state[ self._instructionPointer + 3 ]
                result = valueA * valueB
                self._instructionPointer += 4
                self._state[ pointerResult ] = result
            elif( opCode[0] == 3 ):
                operandA = self._state[ self._instructionPointer + 1 ]
                self._state[operandA] = self._systemID[self._systemIDPointer]
                self._systemIDPointer += 1
                self._instructionPointer += 2
            elif( opCode[0] == 4 ):
                operandA = self._state[ self._instructionPointer + 1 ]
                medium = self._state [ operandA ] if not opCode[1] else operandA
                self._instructionPointer += 2
                return [int(medium), 4]
            elif( opCode[0] == 5 ):
                operandA = self._state[ self._instructionPointer + 1 ]
                operandB = self._state[ self._instructionPointer + 2 ]
                valueA = operandA if opCode[1] else self._state[ operandA ]
                if valueA:
                    self._instructionPointer = operandB if opCode[2] else self._state[ operandB ]
                else:
                    self._instructionPointer += 3
            elif( opCode[0] == 6 ):
                operandA = self._state[ self._instructionPointer + 1 ]
                operandB = self._state[ self._instructionPointer + 2 ]
                valueA = operandA if opCode[1] else self._state[ operandA ]
                if valueA == 0:
                    self._instructionPointer = operandB if opCode[2] else self._state[ operandB ]
                else:
                    self._instructionPointer += 3
            elif( opCode[0] == 7 ):
                operandA = self._state[ self._instructionPointer + 1 ]
                operandB = self._state[ self._instructionPointer + 2 ]
                operandC = self._state[ self._instructionPointer + 3 ]
                valueA = operandA if opCode[1] else self._state[ operandA ]
                valueB = operandB if opCode[2] else self._state[ operandB ]
                self._state[ operandC ] = 1 if valueA < valueB else 0
                self._instructionPointer += 4
            elif( opCode[0] == 8 ):
                operandA = self._state[ self._instructionPointer + 1 ]
                operandB = self._state[ self._instructionPointer + 2 ]
                operandC = self._state[ self._instructionPointer + 3 ]
                valueA = operandA if opCode[1] else self._state[ operandA ]
                valueB = operandB if opCode[2] else self._state[ operandB ]
                self._state[ operandC ] = 1 if valueA == valueB else 0
                self._instructionPointer += 4
        return [0, 99] # Just for signaling the end
