from setuptools import setup

setup(
    name='pyprofmem',
    version='0.1.0',
    description='A simple utility decorator to helps developers to see the memory usage and '
                'profile',
    long_description='A simple utility decorator to helps developers to see the memory usage '
                     'of a determined function and its internal calls. It also provides a '
                     'decorator to see the profile stats usage with memory. In this case, '
                     'the cProfile implementation will be used',
    url='https://github.com/fvlima/pyprofmem',
    author='Frederico V Lima',
    author_email='frederico.vieira at gmail dot com',
    license='MIT',
    packages=['pyprofmem'],
    zip_safe=True,
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: System',
    ])
