from setuptools import setup, find_packages

setup(name='trustpilot_scraper',
      version='0.2.0',
      description='Scraping Utility for trustpilot.com',
      url='https://github.com/AlessandroGianfelici/trutpilot_scraper',
      author='Alessandro Gianfelici',
      author_email='alessandro.gianfelici@hotmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'pandas', 'bs4', 'langdetect'
      ],
      zip_safe=False)