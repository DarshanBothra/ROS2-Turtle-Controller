from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'turtle_controller'

setup(
    name=package_name,
    version='0.0.1',
    packages= find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='darshan',
    maintainer_email='darshan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle_navigator = turtle_controller.turtle_navigator:main',
            'turtle_odometer = turtle_controller.turtle_odometer:main'
        ],
    },
)
