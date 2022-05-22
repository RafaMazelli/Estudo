ano = int(input('\33[33mQual a sua idade?\n'))

if ano <= 9:
    print('Você esta classificado para a categoria \33[35mMirim!')
elif ano > 9 and ano <= 14:
    print('Você foi classificado para a categoria \33[35mInfantil!')
elif ano > 14 and ano <= 19:
    print('Você foi classificado para a categoria \33[35mJunior!')
elif ano > 19 and ano <= 20:
    print('Você foi classificado para a categoria \33[35mSenior!')
else:
    print('Você foi classificado para a categoria \33[35mMaster!')