from setuptools import find_packages, setup

setup(
    name='pyMSpro',
    version='0.1.0',
    description='A Python project for analyzing mass spectrometry data in proteomics.',
    author='Gerard Font',
    author_email='ath@athzone.com',
    url='https://github.com/powwowath/pyMSpro',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas',
        'pyteomics',
    ],
    extras_require={
        'dev': [
            'pytest',
            'black',
            'flake8',
            'jupyterlab',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    python_requires='>=3.9',
)
