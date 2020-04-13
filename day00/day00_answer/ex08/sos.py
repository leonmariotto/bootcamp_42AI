import sys

morse_code = {
  'A':'.-',
  'B':'-...',
  'C':'-.-.',
  'D':'-..',
  'E':'.',
  'F':'..-.',
  'G':'--.',
  'H':'....',
  'I':'..',
  'J':'.---',
  'K':'-.-',
  'L':'.-..',
  'M':'--',
  'N':'-.',
  'O':'---',
  'P':'.--.',
  'Q':'--.-',
  'R':'.-.',
  'S':'...',
  'T':'-',
  'U':'..-',
  'V':'...-',
  'W':'.--',
  'X':'-..-',
  'Y':'-.--',
  'Z':'--..',
  '1':'.----',
  '2':'..---',
  '3':'...--',
  '4':'....-',
  '5':'.....',
  '6':'-....',
  '7':'--...',
  '8':'---..',
  '9':'----.',
  '0':'-----'
}


def print_word_to_morse(word):
  for letter in word:
    if letter.islower:
      letter = letter.upper()
    print(morse_code[letter], end='');
  


if len(sys.argv) < 2:
  sys.exit()

sys.argv.pop(0)
s = ' '.join(sys.argv)

lst = s.split(' ')
for word in lst:
  if word.isalnum() == False:
    print("ERROR")
    sys.exit()
for word in lst:
  print_word_to_morse(word)
  print(' ', end='')
print('')
