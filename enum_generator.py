def generate(enum_class_name, enum_variants):
    print("inline std::ostream& operator<<(std::ostream& os, const " + enum_class_name + "& s)")
    print("{")
    print("\tswitch (s)")
    print("\t{")
    for enum_variant in enum_variants:
        print("\tcase " + enum_class_name + "::" + enum_variant + ":")
        print('\t\tos << " ' + enum_variant + '";')
        print("\t\tbreak;")
    print("\t}")
    print("\treturn os;")
    print("}")


def read_input(input_file):
    with open(input_file) as file:
        return file.readlines()


def prepare_input(input_enums):
    result = [item.replace(',', '') for item in input_enums]
    result = [item.replace('\n', '') for item in result]
    result = [item.strip() for item in result]

    return result


def app():
    input_enums = read_input("state.txt")
    prepared_enums = (prepare_input(input_enums))
    generate("State", prepared_enums)


if __name__ == '__main__':
    app()
