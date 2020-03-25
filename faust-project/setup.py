from setuptools import setup, find_packages

requires = [
    "colorlog>=3.1.4",
    "fastavro<=0.22.3",
    "simple-settings",
    "faust>=1.10.4",
    "python-schema-registry-client",
    "typing-extensions==3.7.4.1",
]

setup(
    name='faust-example',
    version='1.2.1',
    description='Faust example with Docker Compose',
    long_description='''
    Example running Faust with Docker Compose (zookeeper, kafka and schema-registry)
    ''',
    classifiers=[
        "Programming Language :: Python",
    ],
    author='Marcos Schroh',
    author_email='schrohm@gmail.com',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=[],
    setup_requires=[],
    dependency_links=[],
    entry_points={
        'console_scripts': [
            'example = example.app:main',
        ],
        'faust.codecs': [
            'avro_users = example.codecs.avro:avro_user_codec',
        ],
    },
)
