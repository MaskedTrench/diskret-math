from distutils.command.build import build
from flask import Flask, render_template
from server import (one_result, two_result, three_result,
                   fouth_result, five_result, six_result,
                   sknf, sdnf, polinom, minimalize_map
                   )

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/first')
def first():
    res = one_result()
    return render_template('result_out.html',
                           title='one',
                           result=res,
                           sknf=sknf(res),
                           sdnf=sknf(res),
                           polinom = polinom(res),
                           classfications = minimalize_map(res),
                          )


@app.route('/second')
def second():
    res = two_result()
    return render_template('result_out.html',
                           title='second',
                           result=res,
                           sknf=sknf(res),
                           sdnf=sknf(res),
                           polinom = polinom(res),
                           classfications = minimalize_map(res),
                          )


@app.route('/third')
def third():
    res = three_result()
    return render_template('result_out.html',
                           title='third',
                           result=res,
                           sknf=sknf(res),
                           sdnf=sknf(res),
                           polinom = polinom(res),
                           classfications = minimalize_map(res),
                          )


@app.route('/fourth')
def fourth():
    res = fouth_result()
    return render_template('result_three.html',
                           title='fourth',
                           result=res,
                           sknf=sknf(res),
                           sdnf=sdnf(res),
                           polinom = polinom(res),
                           classfications = minimalize_map(res),
                          )


@app.route('/fives')
def fives():
    res = five_result()
    return render_template('result_three.html',
                           title='fives',
                           result=res,
                           sknf=sknf(res),
                           sdnf=sdnf(res),
                           polinom = polinom(res),
                           classfications = minimalize_map(res),
                          )


@app.route('/sixth')
def sixth():
    res = six_result()
    return render_template('result_three.html',
                           title='sixth',
                           result=res,
                           sknf=sknf(res),
                           sdnf=sdnf(res),
                           polinom = polinom(res),
                           classfications = minimalize_map(res),
                          )

if __name__ == '__main__':
    app.run()
