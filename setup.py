from setuptools import setup, find_packages
from pypointgroup import VERSION
#-----------------------------------------------------------------------------------------

def load_description():
    with open('README.md','r') as f:
        text = f.read()
    return text

#-----------------------------------------------------------------------------------------
#
#-----------------------------------------------------------------------------------------

setup(
    name='PyPointGroup',
    version=VERSION,
    python_requires='>3.4',
    packages=['pypointgroup', 'pypointgroup.gl', 'pypointgroup.gui', 'pypointgroup.gui.ui', 'pypointgroup.core'],
    url='https://github.com/nik0380/pypointgroup',
    license='MIT',
    author='Nikolay Somov',
    author_email='somov@phys.unn.ru',
    description='Point group symmetry study software',
    long_description=load_description(),
    long_description_content_type='text/markdown',
    keywords=['symmetry','group','crystallography','xray'],
    install_requires=["PyQt5", "numpy","PyOpenGL","pyshortcuts"],
    include_package_data=True,
    entry_points={'gui_scripts': ['pypointgroup=pypointgroup:main',],},
)
