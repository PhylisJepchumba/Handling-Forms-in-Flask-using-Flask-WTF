from flask import Flask, render_template, request
from forms import ContactForm
app = Flask(__name__)  

app.secret_key = 'development key'  
  



@app.route('/contact', methods = ['GET', 'POST'])  
def contact():  
    
    form=ContactForm()

    if form.validate_on_submit():
        return ' form submitted'
    return render_template('contact.html', form=form)
    
   
  
  

if __name__ == '__main__':  
   app.run(debug = True)  

