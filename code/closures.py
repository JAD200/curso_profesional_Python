#   Hola 3 => HolaHolaHola
#   Juan 2 => JuanJuan
#   Platzi 4 => PlatziPlatziPlatziPlatzi
# Main function with the parameter "n"
def make_repeater_of(n):
    # Nested function
    def repeater(string):
        assert type(string) == str, 'Solo puedes utlizar cadenas de texto'
        return string * n # Returns n but not the string
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5('Hola'))
    repeat_10 = make_repeater_of(10)
    print(repeat_10('Platzi'))

if __name__ == '__main__':
    run()