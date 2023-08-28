from setuptools import setup, find_packages
from test_pip_package import __version__

extra_math = [
    'returns-decorator',
]
extra_bin = [
    *extra_math,
]
extra_test = [
    *extra_math,
    'pytest>=4',
    'pytest-cov>=2',
]
extra_dev = [
    *extra_test,
]

extra_ci = [
    *extra_test,
    'python-coveralls',
]

setup(
    name='test_pip_package',
    version=__version__,
    description='creating pip packages.',
    url='https://github.com/huajuak/test-pip-package',
    author='Anan Sangthongtum',
    author_email='hujauak@gmail.com',
    # packages=find_packages(exclude=['tests', 'tests.*']),
    extras_require={
        'math': extra_math,
        'bin': extra_bin,
        'test': extra_test,
        'dev': extra_dev,
        'ci': extra_ci,
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
