import setuptools

__version__ = "0.0.1"

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


REPO_NAME = "FSDSCNNCLASSIFIER"
AUTHOR_NAME = 'Alisha Tromp'
SRC_REPO = 'CNNClassifier'
AUTHOR_EMAIL = "alisha.lear@gmail.com"

setuptools.setup(name=REPO_NAME,
                version = __version__,
                author = AUTHOR_NAME,
                author_email=AUTHOR_EMAIL,
                description="this is my classification project", 
                long_description=long_description
                long_description_content = "text/markdown", 
                url = f"https://github/{AUTHOR_NAME}/{REPO_NAME}"
                
                project_urls = {
                "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",

                package_dir={"":"src"}
                packages=setuptools.find_packages(where="src")}     )