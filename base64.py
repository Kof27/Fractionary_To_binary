class base64Binary():
    def __init__(self,number:float,base:int):
        self.number = number
        self.base = base
        self.exp = 0
        self.bit_exp = []
        self.exp_string = ''
        self.x = str
        i = number

        
    def positive_or_negative(self,number):
        bit_positive_or_negative = 0
        if number > 1:
            bit_positive_or_negative = 0
        elif number < 0:
            bit_positive_or_negative = 1
        return bit_positive_or_negative
    
    def number_to_binary(self,negative_or_positive,number,base,bit_exp,i,exp,exp_string):
        while int(i) != 0:
            i /= base
            exp += 1
            print (i)
            exp = exp 
            print (exp)
    
        #exponent
        while exp > 0:
            binary_value = int(exp % 2)
            exp = int(exp / 2)
            bit_exp.append(binary_value)
            bit_exp.reverse()
        for x in bit_exp:
            #print (x, end='')
            exp_string += str(x)
            exp_string = exp_string.zfill(23)
    
        print('')
        #mantisa
        mantisa_binary = ''
        mantisa = number - int(number)
    
        #in case mantisa is negative to prevent 000000000000 
        if mantisa < -0:
            mantisa_positive = mantisa * -1
        else:
            mantisa_positive = mantisa
        
        print(mantisa)
        precision = 52
        while (precision):
            mantisa_positive*=2
            bit_mantisa = int(mantisa_positive)
            if (bit_mantisa == 1) :   
                mantisa_positive -= bit_mantisa  
                mantisa_binary += '1'
            else : 
                mantisa_binary += '0'
            precision -= 1
        print(negative_or_positive,'|',exp_string,'|',mantisa_binary)