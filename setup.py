from setuptools import setup


setup(
    name='Neural_Social_Physics',
    version='0.0.1',
    packages=[
        'neural_social_physics',
    ],
    install_requires=[
        'matplotlib',
        'numpy',
        'scipy',
        'torch',
        'torchvision',
        'seaborn',
        'tqdm',
    ],
    extras_require={
        'test': [
            'pylint',
            'pytest',
        ],
    },
)