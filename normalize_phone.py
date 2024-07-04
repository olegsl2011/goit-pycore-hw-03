import re

def normalize_phone(phoneNum):
    digits = re.findall(r'\d+', phoneNum)
    phone_number = ''.join(digits)
    prefix_len = 13 - len(phone_number)
    prefix = "+380"[:prefix_len]
    phone_number = f"{prefix}{phone_number}"
    return phone_number
    

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)