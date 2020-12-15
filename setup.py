from setuptools import setup, find_packages

setup(
    name='PyPointGroup',
    version='2.0.1',
    packages=['pypointgroup', 'pypointgroup.gl', 'pypointgroup.gui', 'pypointgroup.gui.ui', 'pypointgroup.core'],
    url='https://github.com/nik0380/pypointgroup',
    license='MIT',
    author='Nikolay Somov',
    author_email='somov@phys.unn.ru',
    description='Point group symmetry study software',
    keywords=['symmetry','group','crystallography','xray'],
    install_requires=["PyQt5", "numpy","PyOpenGL"],
    #package_data={'pypointgroup.img' : ['2.BMP'],},
    include_package_data=True,
    entry_points={'console_scripts': ['pypointgroup=pypointgroup:main',],},

)
