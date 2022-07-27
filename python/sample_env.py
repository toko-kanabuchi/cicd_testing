import os

firstName = os.environ.get('FIRST_NAME')
lastName  = os.environ.get('LAST_NAME')

print(f"私の名前は {firstName} {lastName} です")