from setuptools import setup

setup(
    name='pers_assist_miv',
    version='0.1',
    packages=['personal_assistant'],
    install_requires=[
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'assist = personal_assistant.main_menu:menu'
        ]
    }
)
