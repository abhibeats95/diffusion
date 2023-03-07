# pylint: disable=line-too-long

from setuptools import find_packages, setup

install_requires = [
    "numpy",
    "matplotlib",
    "pandas",
    "pytest",
    "scikit-image",
    "tqdm",
    "fastapi",
    "motor",
    "pydantic[email]",
    "pymongo",
    "gunicorn",
    "uvicorn",
    "requests-html",
    "jinja2",
    "pika",
    "python-multipart",
    "httpx",
    "rich",
    "trio",
    "google-cloud-storage",
    "ray[serve,k8s] @ https://s3-us-west-2.amazonaws.com/ray-wheels/latest/ray-3.0.0.dev0-cp310-cp310-manylinux2014_x86_64.whl",  # noqa: E501
    "accelerate==0.12.0",
    "torch",
    "torchvision",
    "transformers>=4.21.0",
    "ftfy",
    "tensorboard",
    "modelcards",
    "gitpython",
    "bitsandbytes",
    "diffusers[torch]",
]


test_requires = [
    "flake8",
    "pylint",
    "pytest",
    "pytest-cov",
    "pytest-env",
    "pytest-sugar",
]

dev_requires = test_requires + [
    "pre-commit",
    "ipdb",
]


setup(
    name="dsq-research",
    version="0.0.1",
    description="",
    python_requires=">=3.9",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=install_requires,
    extras_require={
        "test": test_requires,
        "dev": dev_requires,
    },
)
