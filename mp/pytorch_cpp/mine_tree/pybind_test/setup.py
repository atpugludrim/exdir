from setuptools import setup
from torch.utils.cpp_extension import CppExtension, BuildExtension

setup(
        name='pybind_test',
        ext_modules=[CppExtension('pybind_test',['pybind_test.cpp'])],
        cmdclass={'build_ext':BuildExtension},
)
