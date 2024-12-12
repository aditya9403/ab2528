from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def customer_form():
    if request.method == 'POST':
        cust_name = request.form['CustName']
        email = request.form['email']
        mob_no = request.form['MobNo']
        address = request.form['address']
        pincode = request.form['pincode']
        
        # Render the display template with customer details
        return render_template('display.html', 
                               cust_name=cust_name,
                               email=email,
                               mob_no=mob_no,
                               address=address,
                               pincode=pincode)
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True, port=5021)

