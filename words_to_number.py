class wordstonumber:
    words={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,
           'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,
           'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,
           'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20,
           'thirty':30,'forty':40,'fifty':50,'sixty':60,'seventy':70,
           'eighty':80,'ninety':90,'hundred':100,'thousand':1000}

    def __init__(self,input_words):
           self.input_words=input_words.lower()

    def converter(self):
        word=self.input_words.split()
        current=0
        for i in word:
            if i in self.words:
                value=self.words[i]

                if value==100 or value==1000:
                    current*=value
                else:
                    current+=value
            elif (i=='and'):
                continue
            else:
                raise ValueError(f"Unknown word: {i}")

        return current


def main():
    try:
        input_words = input('Enter a number in words (eg:"one hundred twenty three"):')
        convert=wordstonumber(input_words)
        result=convert.converter()
        print(f"The number is: {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()