from setuptools import setup
from torch.utils.cpp_extension import CppExtension, BuildExtension

setup(
        name="pygcanl",
        ext_modules=[CppExtension('pygcanl',['pygcanl.cpp'],extra_compile_args=['-g'])],
        cmdclass={'build_ext':BuildExtension},
)
