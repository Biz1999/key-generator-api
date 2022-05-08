from sympy import isprime


def createKey(clientData) -> dict:
    initialCode = clientData["initialCode"]
    n = clientData["n"]

    minimumPrime = checkMinimumPrimeNumber(initialCode, n)
    maximumPrime = checkMaximumPrimeNumber(initialCode, n)

    newKey = generateKey(minimumPrime, maximumPrime)

    return {"key": newKey}


def checkMinimumPrimeNumber(initialCode, n):
    primesCount = 0
    actualNumber = initialCode

    while(primesCount < n):
        if(isprime(actualNumber)):
            primesCount += 1

        actualNumber -= 1

    return actualNumber + 1


def checkMaximumPrimeNumber(initialCode, n):
    primesCount = 0
    actualNumber = initialCode

    while(primesCount < n):
        if(isprime(actualNumber)):
            primesCount += 1

        actualNumber += 1

    return actualNumber - 1


def generateKey(minimumPrime, maximumPrime): return minimumPrime * maximumPrime
