class Amplifier():
    def __init__(self, ID, codes, relativeBase):
        self._systemID = [ID]
        self._state = codes.copy()
        self._copyOfState = list(codes)
        self._instructionPointer = 0
        self._output = ""
        self._input = 0
        self._newInput = None
        self._systemIDPointer = 0
        self._relativeBase = relativeBase

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

    def computePositionParameter( self, opCode, operand ):
        if( opCode <= 0):
            return self._state[operand]
        elif( opCode == 1):
            return operand
        elif( opCode == 2):
            return self._state[self._relativeBase + operand ]

    def computeOutputParameter( self, opCode, operand):
        if( opCode <= 0 or opCode == 1):
            return operand
        elif( opCode == 2):
            return self._relativeBase + operand

    def compute(self):
        while(self._state[ self._instructionPointer ] != 99):
            opCode = self.computeOpCode( self._state[ self._instructionPointer ] )
            if( opCode[0] == 1 ):
                operandA = self._state[ self._instructionPointer + 1 ]
                operandB = self._state[ self._instructionPointer + 2 ]
                operandC = self._state[ self._instructionPointer + 3 ]
                valueA = self.computePositionParameter( opCode[1], operandA )
                valueB = self.computePositionParameter( opCode[2], operandB )
                valueC = self.computeOutputParameter( opCode[3], operandC )
                self._state[ valueC ] = valueA + valueB
                self._instructionPointer += 4
            elif( opCode[0] == 2 ):
                operandA = self._state[ self._instructionPointer + 1 ]
                operandB = self._state[ self._instructionPointer + 2 ]
                operandC = self._state[ self._instructionPointer + 3 ]
                valueA = self.computePositionParameter( opCode[1], operandA )
                valueB = self.computePositionParameter( opCode[2], operandB )
                valueC = self.computeOutputParameter( opCode[3], operandC )
                self._state[ valueC ] = valueA * valueB
                self._instructionPointer += 4
            elif( opCode[0] == 3 ):
                operandA = self._state[ self._instructionPointer + 1 ]
                valueA = self.computeOutputParameter( opCode[1], operandA )
                self._state[valueA] = self._systemID[self._systemIDPointer]
                self._systemIDPointer += 1
                self._instructionPointer += 2
            elif( opCode[0] == 4 ):
                operandA = self._state[ self._instructionPointer + 1 ]
                medium = self.computePositionParameter( opCode[1], operandA )
                self._instructionPointer += 2
                return [int(medium), 4]
            elif( opCode[0] == 5 ):
                operandA = self._state[ self._instructionPointer + 1 ]
                operandB = self._state[ self._instructionPointer + 2 ]
                valueA = self.computePositionParameter( opCode[1], operandA )
                if valueA:
                    self._instructionPointer = self.computePositionParameter( opCode[2], operandB)
                else:
                    self._instructionPointer += 3
            elif( opCode[0] == 6 ):
                operandA = self._state[ self._instructionPointer + 1 ]
                operandB = self._state[ self._instructionPointer + 2 ]
                valueA = self.computePositionParameter( opCode[1], operandA )
                if valueA == 0:
                    self._instructionPointer = self.computePositionParameter( opCode[2], operandB)
                else:
                    self._instructionPointer += 3
            elif( opCode[0] == 7 ):
                operandA = self._state[ self._instructionPointer + 1 ]
                operandB = self._state[ self._instructionPointer + 2 ]
                operandC = self._state[ self._instructionPointer + 3 ]
                valueA = self.computePositionParameter( opCode[1], operandA )
                valueB = self.computePositionParameter( opCode[2], operandB )
                valueC = self.computeOutputParameter( opCode[3], operandC )
                self._state[ valueC ] = 1 if valueA < valueB else 0
                self._instructionPointer += 4
            elif( opCode[0] == 8 ):
                operandA = self._state[ self._instructionPointer + 1 ]
                operandB = self._state[ self._instructionPointer + 2 ]
                operandC = self._state[ self._instructionPointer + 3 ]
                valueA = self.computePositionParameter( opCode[1], operandA )
                valueB = self.computePositionParameter( opCode[2], operandB )
                valueC = self.computeOutputParameter( opCode[3], operandC )
                self._state[ valueC ] = 1 if valueA == valueB else 0
                self._instructionPointer += 4
            elif( opCode[0] == 9 ):
                operandA = self._state[ self._instructionPointer + 1 ]
                self._relativeBase += self.computePositionParameter( opCode[1], operandA )
                self._instructionPointer += 2
        return [0, 99] # Just for signaling the end
