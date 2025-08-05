from setuptools import setup, find_packages

setup(
    name='stripe_old',
    version='5.0.0',
    description='Stripe Python bindings (unofficial repackaged)',
    author='Stripe (repackaged by Dr Noukhez Ahmed)',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[],  # Add dependencies if needed
    include_package_data=True,
    url='https://github.com/NoukhezAhmed786/stripe_v5.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
