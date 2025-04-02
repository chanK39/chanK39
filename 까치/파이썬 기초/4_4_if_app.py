from distutils.util import change_root


input_id = input('id: ')
id = 'chan'
input_password = input('password: ')
password = '0225'
if input_id == id:
        if input_password == password:
                print('wellcome')
        else:
                print('wrong password')
else:
        print('worng id')