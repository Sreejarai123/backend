from flask import Flask, render_template

app = Flask(__name__)

# Sample quilts data
quilts = [
    {'id': 1, 'name': 'Spring Blossoms', 'description': 'Beautiful floral quilt'},
    {'id': 2, 'name': 'Cozy Cabin', 'description': 'Warm and snug quilt for winter'},
    # Add more quilt data as needed
]

@app.route('/')
def index():
    return render_template('index.html', quilts=quilts)

@app.route('/quilt/<int:quilt_id>')
def quilt_detail(quilt_id):
    quilt = next((q for q in quilts if q['id'] == quilt_id), None)
    if quilt:
        return render_template('quilt_detail.html', quilt=quilt)
    else:
        return render_template('not_found.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
