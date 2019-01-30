 import pyperclip, sys, random

 5.

 6.

 7. LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

 8.

 9. def main():

10. myMessage = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell'

11. myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'

12. myMode = 'encrypt' # set to 'encrypt' or 'decrypt'

13.

14. checkValidKey(myKey)

15.

16. if myMode == 'encrypt':

17. translated = encryptMessage(myKey, myMessage)

18. elif myMode == 'decrypt':

19. translated = decryptMessage(myKey, myMessage)

20. print('Using key %s' % (myKey))

21. print('The %sed message is:' % (myMode))

22. print(translated)

23. pyperclip.copy(translated)

24. print()

25. print('This message has been copied to the clipboard.')

26.

27.

28. def checkValidKey(key):

29.     keyList = list(key)

30.     lettersList = list(LETTERS)

31.     keyList.sort()

32.     lettersList.sort()

33.     if keyList != lettersList:

34.         sys.exit('There is an error in the key or symbol set.')

35.

36.

37. def encryptMessage(key, message):

38. return translateMessage(key, message, 'encrypt')

39.

40.

41. def decryptMessage(key, message):

42. return translateMessage(key, message, 'decrypt')

43.

44.

45. def translateMessage(key, message, mode):

46. translated = ''

47. charsA = LETTERS

48. charsB = key

49. if mode == 'decrypt':

50. # For decrypting, we can use the same code as encrypting. We

51. # just need to swap where the key and LETTERS strings are used.

52. charsA, charsB = charsB, charsA

53.

54. # loop through each symbol in the message

55. for symbol in message:

56. if symbol.upper() in charsA:

57. # encrypt/decrypt the symbol

58. symIndex = charsA.find(symbol.upper())

59. if symbol.isupper():

60. translated += charsB[symIndex].upper()

61. else:

62. translated += charsB[symIndex].lower()

63. else:

64. # symbol is not in LETTERS, just add it

65. translated += symbol

66.

67. return translated

68.

69.

70. def getRandomKey():

71. key = list(LETTERS)

72. random.shuffle(key)

73. return ''.join(key)

74.

75.

76. if __name__ == '__main__':

77. main()