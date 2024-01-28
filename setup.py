from setuptools import setup, find_packages

setup(
    name="easy_udp",
    version="0.1.4",
    packages=find_packages(),
    install_requires=["numpy"],
    description="Easy UDP communication library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mookor/easyUDP",
    author="Andrey Mazko",
)
