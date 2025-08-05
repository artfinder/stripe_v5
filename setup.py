from setuptools import setup, find_packages

setup(
    name='stripe_old',
    version='5.0.0',
    description='Unofficial repackaged Stripe Python bindings. Original code by Stripe.',
    author='Dr Noukhez Ahmed',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        "requests>=2.20",
        "urllib3>=1.25",  # These are typical for Stripe v5.x
    ],
    include_package_data=True,
    url='https://github.com/NoukhezAhmed786/stripe-py-v5',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
