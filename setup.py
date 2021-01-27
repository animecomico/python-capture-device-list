from distutils.core import setup, Extension

module_device = Extension('device',
                        sources = ['device.cpp'], 
                        library_dirs=["C:\Program Files (x86)\Windows Kits\10\Lib"]
                      )

setup (name = 'WindowsDevices',
        version = '1.0',
        description = 'Get device list with DirectShow',
        ext_modules = [module_device])
