import time

print('This is a conversion bot made to simulate a real conversion')
time.sleep(2)
input(str('Bot: Hi!\nYou: '))
time.sleep(0.5)
name = input(str("What's your name?"))
time.sleep(0.5)
print('Bot: How are you', name,'?(good/ok/bad)\n')
response1 = input(str('You:'))
time.sleep(1)
if response1 == 'good':
    print('Good!')
    time.sleep(0.5)
    print('Looks like i need to go!')
    time.sleep(0.5)
    print('Bye,',name,'Hope to see you again!')
    input()
    time.sleep
elif response1 == 'ok':
    print('ok')
