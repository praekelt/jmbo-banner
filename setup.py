from setuptools import setup, find_packages

setup(
    name='jmbo-banner',
    version='0.6',
    description='Jmbo banner app.',
    long_description=open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Consulting',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/praekelt/jmbo-banner',
    packages=find_packages(),
    install_requires=[
        'django>=1.11',
        'django-link',
        'django-simplemde',
        'jmbo',
    ],
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
