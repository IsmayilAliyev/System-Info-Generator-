import platform  as plf
import socket as sk
import re
import uuid

print(""""
        -----------------------------------------------------
        -------------> S Y S T E M    I N F O <--------------
        -----> You can see your system parametrs below <-----
        -----------------------------------------------------
      """ )

def getSystemParametrs():
    try:
        
        sys_info = {}
        sys_info['OS'] = plf.system() + ' ' + plf.release()
        sys_info['OS version']  = plf.version()
        sys_info['Architecture'] = plf.machine()
        sys_info['Your Host Name'] = sk.gethostname()
        sys_info['Your IP Address'] = sk.gethostbyname(sk.gethostname())
        sys_info['Your MAC Address'] = ':'.join(re.findall('..','%012x' % uuid.getnode()))
        sys_info['Processor'] = plf.processor()
        return sys_info
    except Exception as e:
        print(logging.exception(e))

for key , val in getSystemParametrs().items():
    print(key  + ' --- >> ' +  val)
    


"""
# with yield  parametr

def getSystemParametrs():
    try:
        
        sys_info = {}
        sys_info['OS'] = plf.system() + ' ' + plf.release()
        sys_info['OS version']  = plf.version()
        sys_info['Architecture'] = plf.machine()
        sys_info['Your Host Name'] = sk.gethostname()
        sys_info['Your IP Address'] = sk.gethostbyname(sk.gethostname())
        sys_info['Your MAC Address'] = ':'.join(re.findall('..','%012x' % uuid.getnode()))
        sys_info['Processor'] = plf.processor()
        yield sys_info
    except Exception as e:
        print(logging.exception(e))

for key  in getSystemParametrs():
    print(key )

"""


    
