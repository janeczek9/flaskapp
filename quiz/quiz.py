# -*- coding: utf-8 -*-
# quiz/quiz.py

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, flash

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='bradzosekretnawartosc',
))

# lista pytań
DANE = [{
    'pytanie': 'Stolica Hiszpani, to:',  # pytanie
    'odpowiedzi': ['Madryt', 'Warszawa', 'Barcelona'],  # możliwe odpowiedzi
    'odpok': 'Madryt'},  # poprawna odpowiedź
    {
    'pytanie': 'Objętość sześcianu o boku 6 cm, wynosi:',
    'odpowiedzi': ['36', '216', '18'],
    'odpok': '216'},
    {
    'pytanie': 'Symbol pierwiastka Helu, to:',
    'odpowiedzi': ['Fe', 'H', 'He'],
    'odpok': 'He'},
    {
    'pytanie': 'Gdy Thor uderza swoim młotem jakikolwiek kamień, ten rozpada się na pięć mniejszych kamieni.Która z poniższych liczb może być liczbą kamieni po kilku uderzeniach młota, jeśli na początkuThor miał siedem kamieni?',
    'odpowiedzi': ['17', '20', '21', '23', '25'],
    'odpok': '23'},
]



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', pytania=DANE)

@app.route('/odpowiedzi', methods=['GET', 'POST'])
def odpowiedzi():
    if request.method == 'POST':
        punkty = 0
        odpowiedzi = request.form
        for pnr, odp in odpowiedzi.items():
            if odp == DANE[int(pnr)]['odpok']:
                punkty += 1
        flash('Liczba poprawnych odpowiedzi, to: {0}'.format(punkty))
        return redirect(url_for('odpowiedzi'))
    return render_template('odpowiedzi.html', pytania=DANE)


if __name__ == '__main__':
    app.run(debug=True)
