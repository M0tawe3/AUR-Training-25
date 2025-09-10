from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'weather_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share','weather_pkg','launch'),glob('launch/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Motawe',
    maintainer_email='Motawe@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'temperature=weather_pkg.temperature_node:main',
            'pressure=weather_pkg.pressure_node:main',
            'humidity=weather_pkg.humidity_node:main',
            'monitor=weather_pkg.monitor_node:main'
        ],
    },
)
