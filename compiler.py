import os
import time
import marshal

green = '\x1b[32m'
y     = '\x1b[33m'
bl    = '\x1b[34m'
pur   = '\x1b[35m'
cy    = '\x1b[36m'
red   = '\x1b[31m'

def asu():
    print red + ('____        _    _   __        _    _____').center(44)
    print red + ('| __ )  ___ | |_ | | / / _____ | |_ |  __ \\ ').center(44)
    print y + ('|  _ \\ / _ \\|  _|| |/ / |  _  ||  _|| |  \\ \\ ').center(44)
    print y + ('| |_) | (_) | |_ |  _ \\ | | | || |_ | |__/ / ').center(44)
    print green + ('|____/ \\___/ \\__||_| \\_\\|_| |_|\\___||_____/ ').center(44)
    print green + '=' * 45
    print cy + 'Author  : Al2VyN '
    print cy + 'Type    : Compiler Python'
    print cy + 'Github  : Https://github.com/Al2VyN'
    print cy + 'Version : 1.0 \n'
    print y + '[!]' + red + ' The file must be one folder with this tool, if not, please move it first ' + y + '[!]\n'


def py():
    try:
        os.system('clear')
        asu()
        a = raw_input(green + 'Input File Name : ' + bl)
        x = open(a).read()
        b = compile(x, '', 'exec')
        c = marshal.dumps(b)
        d = open('Enc' + a, 'w')
        d.write('#######################\n')
        d.write('# T E R C O M P I L E #\n')
        d.write('#        Al2VyN       #\n')
        d.write('#######################\n')
        d.write('import marshal\n')
        d.write('exec(marshal.loads(' + repr(c) + '))')
        d.close()
        print y + 'Processing Compile ' + red + '1%'
        time.sleep(0.7)
        print y + 'Processing Compile ' + red + '8%'
        time.sleep(0.9)
        print y + 'Processing Compile ' + red + '17%'
        time.sleep(0.7)
        print y + 'Processing Compile ' + red + '24%'
        time.sleep(0.7)
        print y + 'Processing Compile ' + red + '31%'
        time.sleep(1.4)
        print y + 'Processing Compile ' + red + '45%'
        time.sleep(0.8)
        print y + 'Processing Compile ' + red + '53%'
        time.sleep(0.6)
        print y + 'Processing Compile ' + red + '69%'
        time.sleep(0.7)
        print y + 'Processing Compile ' + red + '76%'
        time.sleep(0.6)
        print y + 'Processing Compile ' + red + '82%'
        time.sleep(0.6)
        print y + 'Processing Compile ' + red + '98%'
        time.sleep(0.9)
        print y + 'Processing Compile ' + red + '100%'
        print '\x1b[1;32mFile Name Output :' + bl + ' Enc' + a
        tanya1 = raw_input(pur + '[?] Compile Again ? (y/n) ')
        if tanya1 == 'y':
            py2()
        elif tanya1 == 'n':
            print red + '[!] Ahhhhhhh Sheeeee Uuuuuuuup'
            exit()
        else:
            print red + '[!] Ahhhhhhh Sheeeee Uuuuuuuup'
            exit()
    except KeyboardInterrupt:
        print r + '[!] ERROR'
        exit()


def py2():
    try:
        os.system('clear')
        asu()
        a = raw_input(green + 'Input File Name : ' + bl)
        x = open(a).read()
        b = compile(x, '', 'exec')
        c = marshal.dumps(b)
        d = open('Enc' + a, 'w')
        d.write('#######################\n')
        d.write('# T E R C O M P I L E #\n')
        d.write('#        Al2VyN       #\n')
        d.write('#######################\n')
        d.write('import marshal\n')
        d.write('exec(marshal.loads(' + repr(c) + '))')
        d.close()
        print y + 'Processing Compile ' + red + '0%'
        time.sleep(0.7)
        print y + 'Processing Compile ' + red + '7%'
        time.sleep(1)
        print y + 'Processing Compile ' + red + '18%'
        time.sleep(0.7)
        print y + 'Processing Compile ' + red + '23%'
        time.sleep(0.7)
        print y + 'Processing Compile ' + red + '32%'
        time.sleep(1.4)
        print y + 'Processing Compile ' + red + '46%'
        time.sleep(0.5)
        print y + 'Processing Compile ' + red + '51%'
        time.sleep(0.6)
        print y + 'Processing Compile ' + red + '64%'
        time.sleep(0.7)
        print y + 'Processing Compile ' + red + '77%'
        time.sleep(0.9)
        print y + 'Processing Compile ' + red + '89%'
        time.sleep(0.8)
        print y + 'Processing Compile ' + red + '95%'
        time.sleep(0.9)
        print y + 'Processing Compile ' + red + '100%'
        print '\x1b[1;32mFile Name Output :' + bl + ' Enc' + a
        tanya1 = raw_input(pur + '[?] Compile Again ? (y/n) ')
        if tanya1 == 'y':
            py3()
        elif tanya1 == 'n':
            print red + '[!] Ahhhhhhh Sheeeee Uuuuuuuup'
            exit()
        else:
            print red + '[!] Ahhhhhhh Sheeeee Uuuuuuuup'
            exit()
    except KeyboardInterrupt:
        print r + '[!] ERROR'
        exit()


def py3():
    try:
        os.system('clear')
        asu()
        a = raw_input(green + 'Input File Name : ' + bl)
        x = open(a).read()
        b = compile(x, '', 'exec')
        c = marshal.dumps(b)
        d = open('Enc' + a, 'w')
        d.write('#######################\n')
        d.write('# T E R C O M P I L E #\n')
        d.write('#        Al2VyN       #\n')
        d.write('#######################\n')
        d.write('import marshal\n')
        d.write('exec(marshal.loads(' + repr(c) + '))')
        d.close()
        print y + 'Processing Compile ' + red + '2%'
        time.sleep(0.7)
        print y + 'Processing Compile ' + red + '9%'
        time.sleep(0.9)
        print y + 'Processing Compile ' + red + '15%'
        time.sleep(0.7)
        print y + 'Processing Compile ' + red + '27%'
        time.sleep(0.7)
        print y + 'Processing Compile ' + red + '36%'
        time.sleep(1.4)
        print y + 'Processing Compile ' + red + '48%'
        time.sleep(0.8)
        print y + 'Processing Compile ' + red + '55%'
        time.sleep(0.6)
        print y + 'Processing Compile ' + red + '62%'
        time.sleep(0.7)
        print y + 'Processing Compile ' + red + '71%'
        time.sleep(0.6)
        print y + 'Processing Compile ' + red + '84%'
        time.sleep(0.6)
        print y + 'Processing Compile ' + red + '93%'
        time.sleep(0.9)
        print y + 'Processing Compile ' + red + '100%'
        print '\x1b[1;32mFile Name Output :' + bl + ' Enc' + a
        tanya1 = raw_input(pur + '[?] Compile Again ? (y/n) ')
        if tanya1 == 'y':
            py()
        elif tanya1 == 'n':
            print red + '[!] Ahhhhhhh Sheeeee Uuuuuuuup'
            exit()
        else:
            print red + '[!] Ahhhhhhh Sheeeee Uuuuuuuup'
            exit()
    except KeyboardInterrupt:
        print r + '[!] ERROR'
        exit()


os.system('clear')
asu()
py2()
