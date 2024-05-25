from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'unrealbot',
    version = '1.0.0',
    author = 'Heath Sinclair',
    author_email = 'hsinclair6140@gmail.com',
    license = '',
    description = 'Python-based CLI utility for Unreal Engine project support, assisting with setup, build, and publish tasks.',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/hsinclair6140/unreal-bot',
    py_modules = ['unreal_bot', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        unrealbot=unreal_bot:cli
    '''
)