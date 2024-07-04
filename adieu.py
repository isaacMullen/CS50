import inflect

p = inflect.engine()

names = []
end_index = 0

while True:
    try:
        name = input("Name: ")

        names.append(name)
    except KeyboardInterrupt:
        print()
        break

prefix = "adieu, adieu, to "

for i in names:
    end_index += 1
    output = p.join(names[0: end_index])
    print(prefix + output)