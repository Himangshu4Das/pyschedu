from setuptools import setup, find_packages

setup(
    name='pyschedu',
    version='1.0.0',
    author='Himangshu Das',
    author_email='himangshu4das@gmail.com',
    description='Python package for scheduling events',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Himangshu4Das/pyschedu',
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)