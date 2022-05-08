from logicProcess import createKey


def checkRequestData(clientData) -> dict:
    validateData(clientData)

    createKeyResponse = createKey(clientData)

    return createKeyResponse


def validateData(data) -> None:
    try:
        initialCode = data["initialCode"]

        n = data["n"]
    except Exception as e:
        raise TypeError(f"Faltando propriedade {e}")

    if initialCode <= 10000000:
        raise TypeError("initialCode precisa ser maior que 10.000.000")

    if n <= 5000 or n >= 15000:
        raise TypeError("5.000 < n < 15000")
