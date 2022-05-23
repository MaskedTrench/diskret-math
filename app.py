from distutils.command.build import build
from flask import Flask, render_template
from forms import (one_result, two_result, three_result,
                   fouth_result, five_result, six_result,
                   double_build_sknf, double_build_sdnf,
                   third_build_sdnf, third_build_sknf,
                   build_polinom, minimalization
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
                           polinom = build_polinom(res, 0),
                           map_carno = minimalization(res, 0)[0],
                           m_sknf = minimalization(res, 0)[1],
                           m_sdnf = minimalization(res, 0)[2],
                          )


@app.route('/second')
def second():
    res = two_result()
    return render_template('result_out.html',
                           title='second',
                           result=res,
                           sknf=double_build_sknf(res),
                           sdnf=double_build_sdnf(res),
                           polinom = build_polinom(res, 1),
                           map_carno = minimalization(res, 1)[0],
                           m_sknf = minimalization(res, 1)[1],
                           m_sdnf = minimalization(res, 1)[2],
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
                           map_carno = minimalization(res, 2)[0],
                           m_sknf = minimalization(res, 2)[1],
                           m_sdnf = minimalization(res, 2)[2],
                          )


@app.route('/fourth')
def fourth():
    res = fouth_result()
    return render_template('result_three.html',
                           title='fourth',
                           result=res,
                           sknf=third_build_sknf(res),
                           sdnf=third_build_sdnf(res),
                           polinom = build_polinom(res, 3),
                           map_carno = minimalization(res, 3)[0],
                           m_sknf = minimalization(res, 3)[1],
                           m_sdnf = minimalization(res, 3)[2],
                          )


@app.route('/fives')
def fives():
    res = five_result()
    return render_template('result_three.html',
                           title='fives',
                           result=res,
                           sknf=third_build_sknf(res),
                           sdnf=third_build_sdnf(res),
                           polinom = build_polinom(res, 4),
                           map_carno = minimalization(res, 4)[0],
                           m_sknf = minimalization(res, 4)[1],
                           m_sdnf = minimalization(res, 4)[2],
                          )


@app.route('/sixth')
def sixth():
    res = six_result()
    return render_template('result_three.html',
                           title='sixth',
                           result=res,
                           sknf=third_build_sknf(res),
                           sdnf=third_build_sdnf(res),
                           polinom = build_polinom(res, 5),
                           map_carno = minimalization(res, 5)[0],
                           m_sknf = minimalization(res, 5)[1],
                           m_sdnf = minimalization(res, 5)[2],
                          )

if __name__ == '__main__':
    app.run()
