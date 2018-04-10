from setuptools import setup, find_packages

setup (
  name = "polls",
  version = "0.1.0",
  description = "Polls Django REST service",
  packages = find_packages(),
  include_package_data = True,
  scripts = ["manage.py"],
  install_requires = ["Django>=2.0.1",
		      "django-cors-headers>=2.1.0",
		      "djangorestframework>=3.7.7",
                      "mysqlclient>=1.3.12",
                      "uwsgi>=2.0"],
  extras_require = {
                    "test": [
                        "colorama>=0.3.9",
                        "coverage>=4.5",
                        "django-nose>=1.4.5",
                        "nose>=1.3.7",
                        "pinocchio>=0.4.2",
                        "PyMySQL==0.8.0",
                        "pytz>=2017.3"
                    ]  
 }
)
