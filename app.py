from distutils.command.build import build
from flask import Flask, render_template
from server import (one_result, two_result, three_result,
                   fouth_result, five_result, six_result,
                   sknf, sdnf, polinom, minimalize_map,
                   karno_map,
                   minimazide_sdnf, minimazide_sknf
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
                           karno_map = karno_map(res),
                           mknf = minimazide_sknf(0),
                           mdnf = minimazide_sdnf(0),
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
                           karno_map = karno_map(res),
                           mknf = minimazide_sknf(1),
                           mdnf = minimazide_sdnf(1),
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
                           karno_map = karno_map(res),
                           mknf = minimazide_sknf(2),
                           mdnf = minimazide_sdnf(2),
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
                           karno_map = karno_map(res),
                           mknf = minimazide_sknf(3),
                           mdnf = minimazide_sdnf(3),
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
                           karno_map = karno_map(res),
                           mknf = minimazide_sknf(4),
                           mdnf = minimazide_sdnf(4),
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
                           karno_map = karno_map(res),
                           mknf = minimazide_sknf(5),
                           mdnf = minimazide_sdnf(5),
                          )

if __name__ == '__main__':
    app.run()
