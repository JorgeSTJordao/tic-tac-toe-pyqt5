from Interface import Interface

interface = Interface()

value = interface.options()

if value == 1:
    interface.play()

print("Bye bye!")
