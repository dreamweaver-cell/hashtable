import hashtable

# create a mapping of name to phone number
phonebook = hashtable.new()
hashtable.set(phonebook, 'Homer Simpson', '070 456382')
hashtable.set(phonebook, 'Lisa Simpson', '073 193872')
hashtable.set(phonebook, 'Bart Simpson',   '073 235454')
hashtable.set(phonebook, 'Magie Simpson', '070 343955')
hashtable.set(phonebook, 'Bender', '777 456382')

op = hashtable.new()
hashtable.set(op, '070 456382', 'Mobile Inc.')
hashtable.set(op, '073 193872', 'Telefonbolaget')
hashtable.set(op, '073 235454', 'Telefonbolaget')
hashtable.set(op, '070 343955', 'Mobile Inc.')

print('-' * 10)
print(f"Homer Simpson's number is: {hashtable.get(phonebook, 'Homer Simpson')}")
print(f"Lisa Simpson's number is: {hashtable.get(phonebook, 'Lisa Simpson')}")

print('-' * 10)
print('The hole phonebook:')
hashtable.list(phonebook)

print('-' * 10)
print(f"Bart Simpson's phone company is: {hashtable.get(op, hashtable.get(phonebook, 'Bart Simpson'))}")
print(f"Magie Simpson's phone company is: {hashtable.get(op, hashtable.get(phonebook, 'Magie Simpson'))}")

print('-' * 10)
print('Phone number belong to company:')
hashtable.list(op)

print('-' * 10)
name =(hashtable.get(phonebook, 'Sven Svensson'))

if not name:
  print("No Sven Svensson in phonebook.")

print('-' * 10)
phonebook = hashtable.get(phonebook, 'Sara Jansson', 'Not found in the phonebook')
print(f" 'Sara Jansson': {phonebook}")
