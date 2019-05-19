from setuptools import setup, find_packages

requires = [
    "avro-python3",
    "colorlog==3.1.4",
    "fastavro",
    "faust==1.5.4",
    "robinhood-aiokafka==1.0.2",
    "requests",
    "simple-settings==0.16.0",
    "python-schema-registry-client==0.0.2",
]

setup(
    name='faust-example',
    version='1.1.1',
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
