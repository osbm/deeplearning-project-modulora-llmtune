from setuptools import setup, Extension
from torch.utils import cpp_extension
setup(
    ext_modules=[cpp_extension.CUDAExtension(
        'quant_cuda', 
        [
        	'llmtune/engine/inference/cuda/quant_cuda.cpp', 
        	'llmtune/engine/inference/cuda/quant_cuda_kernel.cu'
        ]
    )],
    cmdclass={'build_ext': cpp_extension.BuildExtension}
)