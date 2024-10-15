def interest_math(pv, year, interest):
    e = 2.7183
    interest = interest / 100

    exponent = year * interest
    expo_pow = pow(e, exponent)

    answer = pv * expo_pow
    return answer
