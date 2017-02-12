from setuptools import setup


repo_url = 'https://github.com/chillaranand/httpie-token-auth'
author = 'Chillar Anand'
author_email = 'anand21nanda@gmail.com'


with open('README.md') as fh:
    long_description = fh.read()

setup(
    name='httpie-token-auth',
    version='0.1.7',
    description='token Auth plugin for HTTPie.',
    long_description=long_description,

    author=author,
    author_email=author_email,
    maintainer=author,
    maintainer_email=author_email,

    url=repo_url,
    download_url=repo_url,

    py_modules=['httpie_token_auth'],

    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_token_auth = httpie_token_auth:TokenAuthPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0'
    ],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
