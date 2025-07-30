from setuptools import setup, find_packages

setup(
    name='sdgp',
    version='0.92.0',
    packages=find_packages(exclude=['tests']),
    ext_modules=[
        gtk_dialog_module
    ],
    entry_points={
        'console_scripts': [
            'my_command = sdgp.module:main_func',
        ],
    },
    # ... 他のメタデータ ...
)
