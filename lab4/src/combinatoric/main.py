from modules.task1 import task1
from modules.recurrent_variant5 import recurrent_variant5
from modules.recurrent_variant6 import recurrent_variant6

task1()

print('Variant 5')
for i in range(6):
    print('%4d - %d' % (i, recurrent_variant5(i)))

print('Variant 6')
for i in range(6):
    print('%4d - %d' % (i, recurrent_variant6(i)))

