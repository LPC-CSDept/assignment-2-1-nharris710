def main():
    ##################################################
    # Comlete your code here
    ##################################################
    pass


if __name__ == '__main__':
    main()
numM =int(input('enter the number of males:'))
numF =int(input('enter the number of females:'))

perceM = numM /(numM + numF) * 100
perceF = numF /(numM + numF) * 100
# Output 
print ('total number of students: ',numM + numF)
print ('Number of males and females', numM, numF)
#print ("percentage of males and females")
print('The percentage of males and females',perceM,perceF)
