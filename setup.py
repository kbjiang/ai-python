# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

import io
import os

# NOTE: DO NOT change the import order, as sometimes there is a conflict between setuptools and distutils,
# it will cause following error:
# error: each element of 'ext_modules' option must be an Extension instance or 2-tuple
from setuptools import find_packages
from distutils.core import setup

readme = io.open("./README.md", encoding="utf-8").read()

setup(
    name="pre-ai-python",
    version="0.0.1",
    description="Microsoft AI Python Package",
    long_description=readme,
    long_description_content_type="text/x-rst",
    author="Daniel Ciborowski",
    author_email="dciborow@microsoft.com",
    url="https://github.com/microsoft/ai-python",
    project_urls={
        "Code": "https://github.com/microsoft/ai-python",
        "Issues": "https://github.com/microsoft/ai-python/issues",
        "Documents": "https://github.com/microsoft/ai-python"
    },
    license="MIT License",
    platforms=["Windows", "Linux", "macOS"],
    keywords=[
        "ai",
    ],
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"],
    python_requires=">=3.7,<3.8",
    setup_requires=[
        "jupyter-packaging==0.7.12",
        "numpy==1.19.5",
        "pip-tools==5.5.0",
        "scikit-build==0.11.1",
        "scipy==1.4.1",
    ],
    install_requires=[      
        "aiohttp==3.7.4.post0",
        "asyncio==3.4.3",
        "azure-ai-formrecognizer==3.0.0",
        "azure-cognitiveservices-vision-customvision==1.0.0",
        "azure-cognitiveservices-vision-computervision==0.7.0",
        "azure-core==1.10.0",
        "azure-cosmos==4.2.0",
        "azure-cosmosdb-table==1.0.6",
        "azure-data-tables==12.0.0b1",
        "azure-functions==1.7.0",
        "azure-keyvault==4.1.0",
        "azure-keyvault-secrets==4.2.0",
        "azure-mgmt-compute",
        "azure-mgmt-deploymentmanager",
        "azure-mgmt-resource",
        "azure-search-documents==11.1.0b3",
        "azure-servicebus==0.50.3",
        "azure-storage==0.36.0",
        "azure-storage-blob<13.0.0,>=12.6.0",
        "azure-storage-common==2.1.0",
        "azure-storage-file==2.1.0",
        "azure-storage-file-datalake",
        "azure-storage-nspkg==3.1.0",
        "azure-storage-queue==12.1.4",
        "azureml-contrib-automl-pipeline-steps==1.21.0",
        "azureml-core==1.21.0.post2",
        "azureml-defaults==1.21.0",
        "azureml-pipeline==1.21.0",
        "azureml-train==1.21.0",
        "beautifulsoup4",
        "cached-property==1.5.1",
        "chardet",
        "ciso8601==2.1.3",
        "cornac==1.7.1",
        "cppy==1.1.0",
        "cryptography>=3.3,<3.4.0",
        "cycler>=0.10.0",
        "cvxpy>=1.1.10",
        "cvxopt>=1.2.6",
        "databricks-cli==0.14.1",
        "datasets==1.3.0",
        "dateparser==0.7.6",
        "dm-tree==0.1.5",
        "eli5==0.10.0",
        "fairlearn==0.5.0",
        "fastai==2.2.7",
        "fastapi==0.61.0",
        "feedparser==5.2.1",
        "flask>=1.0.3,<=1.1.1",
        "flask-login==0.5.0",
        "geopandas==0.8.2",
        "gym>=0.15.6",
        "hyperopt==0.2.3",
        "interpret-core==0.2.0",
        "ipython==7.22.0",
        "jieba3k==0.35.1",
        "joblib==0.16.0",
        "kiwisolver>=1.0.0",
        "lasio==0.25.0",
        "lightgbm==2.3.0",
        "llvmlite==0.35.0",
        "lxml>=4.6.2",
        "matplotlib==3.2.2",
        "msrest==0.6.19",
        "msrestazure==0.6.4",
        "netCDF4==1.5.5.1",
        "newspaper3k==0.2.8",
        "nltk==3.5",
        "numba==0.52.0",
        "opencensus-ext-azure==1.0.5",
        "opencv-python-headless==4.3.0.36",
        "opencv-python==4.3.0.36",
        "ortools==7.8.7959",
        "pandas>=1.0.3,<=1.1.3",
        "pathfinder==0.6.2",
        "pathlib2>=2.2.0",
        "pathspec==0.8.0",
        "pathtools",
        "pbr==5.4.5",
        "pkgconfig",
        "pip==20.3.3",
        "Pillow>=6.2",
        "preshed==3.0.4",
        "protobuf==3.15.7",
        "playfab==0.0.200914",
        "pluggy==0.13.1",
        "psycopg2==2.8.6", 
        "pydantic==1.7.3",
        "pyodbc==4.0.30",
        "pypandoc==1.5.0",
        "pyparsing>=2.0.3",
        "pyscaffold==3.2.1",
        "pyspark==2.4.0",
        "python-dateutil>=2.1",
        "python-dotenv==0.14.0",
        "pytorch-pretrained-bert==0.6.2",
        "pytz==2020.1",
        "pyyaml==5.4.1",
        "randomgen==1.19.3",
        "ray[rllib]==1.1.0",
        "regex==2020.7.14",
        "requests==2.24.0",
        "scikit-learn<=0.23.0",
        "scipy==1.5.4",
        "seaborn==0.10.1",
        "seqeval==1.2.2",
        "sentencepiece==0.1.95",
        "sentinelsat==0.14",
        "setuptools==54.2.0",
        "spacy<2.3.5",
        "tensorflow>=2.2.2,<2.4",
        "termcolor==1.1.0",
        "toml==0.10.1",
        "torch==1.7.1",
        "torchvision==0.8.2",
        "tqdm==4.46.0",
        "transformers==4.2.0",
        "urllib3==1.25.10",
        "utm==0.6.0",
        "uvicorn==0.12.2",
        "wget==3.2",
    ],
    entry_points={
    },
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*"]),
    include_package_data=True,
    package_data={
    },
    zip_safe=False,
)
