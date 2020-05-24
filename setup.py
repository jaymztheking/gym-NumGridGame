from setuptools import setup, find_packages

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(name="gym-NumGridGame",
	  version="0.0.1",
	  install_requires=['gym'],
	  author="James Medaugh",
	  author_email="james.medaugh@gmail.com",
	  description="A OpenAI gym environment that plays a number grid game",
	  long_description=long_description,
	  long_description_content_type="text/markdown",
	  packages=find_packages(),
	  classifiers=[
		  "Programming Language :: Python :: 3",
		  "License :: OSI Approved :: MIT License",
		  "Operating System :: OS Independent",
	  ],
	  python_requires='>=3.6',
)