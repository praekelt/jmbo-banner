from setuptools import setup, find_packages

setup(
    name='jmbo-banner',
    version='0.6',
    description='Jmbo banner app.',
    long_description=open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/praekelt/jmbo-banner',
    packages=find_packages(),
    install_requires=[
        # Pinned because django-dfp has no pin while jmbo has, but setuptools
        # is not smart enough to resolve this. Also setuptools ignores the pin
        # if in tests_require.
        'django>=1.4,<1.7',
        'jmbo>=1.1.1',
        'django-dfp>=0.3.3',
    ],
    tests_require=[
        'django-setuptest>=0.1.4',
        'psycopg2',
    ],
    test_suite="setuptest.setuptest.SetupTestSuite",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
