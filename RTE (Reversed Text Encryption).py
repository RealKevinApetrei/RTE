class ReversedText(str):
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self

while True:
    input_code = input("What text would you like reversed? (!QUIT! to quit.) ")
    print("Here is your reversed text: \n\n {}".format(ReversedText(input_code)))


