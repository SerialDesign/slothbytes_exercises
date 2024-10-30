
def numToEng(n):
    if not (0 <= n <= 999):
        return "Number out of range"

    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n < 10:
        return ones[n]
    elif 10 < n < 20:
        return teens[n - 10]
    elif n < 100:
        return tens[n // 10] + ('' if n % 10 == 0 else ' ' + ones[n % 10])
    else:
        return ones[n // 100] + ' hundred' + ('' if n % 100 == 0 else ' ' + numToEng(n % 100))

# Test cases
print(numToEng(0))    # Output: "zero"
print(numToEng(18))   # Output: "eighteen"
print(numToEng(54))   # Output: "fifty four"
print(numToEng(126))  # Output: "one hundred twenty six"
print(numToEng(909))  # Output: "nine hundred nine"
