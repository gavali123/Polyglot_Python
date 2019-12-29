from flask import Flask

import polyglot.python.service.PrimeService as PrimeService

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello From Flask'


@app.route('/prime/<int:num>')
def is_two_sided_prime(num):
    return PrimeService.is_two_sided_prime(num)


if __name__ == '__main__':
    app.run()