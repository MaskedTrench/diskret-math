from distutils.command.build import build
from flask import Flask, render_template
from forms import (one_result, two_result, three_result,
                   fouth_result, five_result, six_result,
                   double_build_sknf, double_build_sdnf,
                   third_build_sdnf, third_build_sknf,
                   build_polinom_2, build_polinom_3
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
                           sknf=double_build_sknf(res),
                           sdnf=double_build_sdnf(res),
                           polinom = build_polinom2(res),
                          )


@app.route('/second')
def second():
    res = two_result()
    return render_template('result_out.html',
                           title='second',
                           result=res,
                           sknf=double_build_sknf(res),
                           sdnf=double_build_sdnf(res),
                           polinom = build_polinom2(res),
                          )


@app.route('/third')
def third():
    res = three_result()
    return render_template('result_out.html',
                           title='third',
                           result=res,
                           sknf=double_build_sknf(res),
                           sdnf=double_build_sdnf(res),
                           polinom = build_polinom(res, 2),
                          )


@app.route('/fourth')
def fourth():
    res = fouth_result()
    return render_template('result_three.html',
                           title='fourth',
                           result=res,
                           sknf=third_build_sknf(res),
                           sdnf=third_build_sdnf(res),
                           polinom = build_polinom_3(res),
                          )


@app.route('/fives')
def fives():
    res = five_result()
    return render_template('result_three.html',
                           title='fives',
                           result=res,
                           sknf=third_build_sknf(res),
                           sdnf=third_build_sdnf(res),
                           polinom = build_polinom_3(res),
                          )


@app.route('/sixth')
def sixth():
    res = six_result()
    return render_template('result_three.html',
                           title='sixth',
                           result=res,
                           sknf=third_build_sknf(res),
                           sdnf=third_build_sdnf(res),
                           polinom = build_polinom_3(res),
                          )

if __name__ == '__main__':
    app.run()
