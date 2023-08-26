from setuptools import setup

setup(
    name='Personal assistant project',
    version='0.1.11',
    description='Personal Assistant Project',
    license='MIT',
    author='Next Frontier',
    packages=['per_assist'],
    install_requires=['rich'],
    entry_points={
        'console_scripts': [
            'per_assist = personal_assistant.main_menu:menu'
        ]
    }
)