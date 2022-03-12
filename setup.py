from setuptools import setup

setup(
    name='anydeck',
    version='0.0.1',
    description='Generates a deck of virtually any type of cards from which drawing, '
                'adding, removing, and shuffling is handled by the package.',
    py_modules=['AnyDeck', 'Card'],
    package_dir={'': 'src'},

    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)
