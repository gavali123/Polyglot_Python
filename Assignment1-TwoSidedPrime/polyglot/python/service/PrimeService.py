import json

import polyglot.python.utils.PrimeCalculationUtility as PrimeUtil


def is_two_sided_prime(num):
    is_prime = {'is_two_sided_prime': PrimeUtil.two_sided_prime(num)}
    return json.dumps(is_prime)
