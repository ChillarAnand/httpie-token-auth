## httpie-token-auth

token auth plugin for HTTPie.


## Installation


    $ pip install httpie-token-auth

You should now see ``token`` under ``--auth-type`` in ``$ http --help`` output.


## Usage


    $ http --auth-type=token --auth='username:password' example.org
    $ http -A=token --auth='username:password' example.org


## License
