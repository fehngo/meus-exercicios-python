def leia_int(msg):
    while True:
        try:
            numero = int(input(msg))
            return numero

        except (ValueError, TypeError):
            print("Tivemos um problema com os tipos de dados que você digitou!")

        except KeyboardInterrupt:
            print("O usuário decidiu não informar esse número!")


def leia_float(msg):
    while True:
        try:
            numero = float(input(msg))
            return numero

        except (ValueError, TypeError):
            print("Tivemos um problema com os tipos de dados que você digitou!")

        except KeyboardInterrupt:
            print("O usuário decidiu não informar esse número!")
            return 0
