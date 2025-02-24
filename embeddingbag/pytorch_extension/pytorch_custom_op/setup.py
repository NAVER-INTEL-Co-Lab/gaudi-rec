###############################################################################
# Copyright (C) 2020-2021 Habana Labs, Ltd. an Intel Company
###############################################################################

from setuptools import setup
from torch.utils import cpp_extension
from habana_frameworks.torch.utils.lib_utils import get_include_dir, get_lib_dir
import os
import pybind11

torch_include_dir = get_include_dir()
torch_lib_dir = get_lib_dir()
habana_modules_directory = "/usr/include/habanalabs"
pybind_include_path = pybind11.get_include()

setup(name='hpu_custom_embedding_bag_sum',
      ext_modules=[cpp_extension.CppExtension('hpu_custom_embedding_bag_sum', ['hpu_custom_embedding_bag_sum.cpp'],
            language='c++', extra_compile_args=["-std=c++17"],
            libraries=['habana_pytorch_plugin'],
            library_dirs=[torch_lib_dir])],
      include_dirs=[torch_include_dir,
                    habana_modules_directory,
                    pybind_include_path,
                    ],
      cmdclass={'build_ext': cpp_extension.BuildExtension})

setup(name='hpu_custom_table_batched_embedding_bag_sum',
      ext_modules=[cpp_extension.CppExtension('hpu_custom_table_batched_embedding_bag_sum', ['hpu_custom_table_batched_embedding_bag_sum.cpp'],
            language='c++', extra_compile_args=["-std=c++17"],
            libraries=['habana_pytorch_plugin'],
            library_dirs=[torch_lib_dir])],
      include_dirs=[torch_include_dir,
                    habana_modules_directory,
                    pybind_include_path,
                    ],
      cmdclass={'build_ext': cpp_extension.BuildExtension})