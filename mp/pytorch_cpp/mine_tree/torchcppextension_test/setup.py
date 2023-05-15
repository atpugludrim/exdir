from setuptools import setup
from torch.utils.cpp_extension import CppExtension, BuildExtension

setup(name='pygread',
        ext_modules=[CppExtension('pygread', ['pyg_read.cpp'])],
        cmdclass={'build_ext': BuildExtension},
        )
