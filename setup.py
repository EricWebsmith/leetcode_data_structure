from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='leetcode_data_structure',
    version='0.1.2',
    description='This package provides three classes for working with data structures in LeetCode problems',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Eric Websmith',
    author_email='eric.websmith@example.com',
    url='https://github.com/EricWebsmith/leetcode_data_structure',
    packages=['leetcode_data_structure'],
    package_data={'leetcode_data_structure': ['py.typed']},
    install_requires=[
        # List your dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
