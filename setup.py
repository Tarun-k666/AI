from setuptools import setup, find_packages

setup(
    name="AI",
    version="0.1.0",
    description="AI Engineering Project",
    author="Developer",
    python_requires=">=3.8",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24.0",
        "pandas>=1.5.0",
        "scikit-learn>=1.2.0",
        "tensorflow>=2.11.0",
        "torch>=1.13.0",
        "matplotlib>=3.6.0",
        "seaborn>=0.12.0",
        "jupyter>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.2.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ]
    },
)
