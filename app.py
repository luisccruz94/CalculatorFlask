from flask import Flask, render_template, url_for, request
from math import sin, cos, tan, sqrt, exp, log, acosh, asinh, atanh, asin, acos


app = Flask(__name__)

@app.route("/")
def  main():

    return render_template('index.html',home=True)

@app.route("/simple")
def simple(): 
    return render_template("simple.html",home=False)

@app.route('/avancado')
def avancado():
    return render_template('avancado.html',home=False)



@app.route("/calculadora", methods=["post"])
def calculadora():
    first_number = float(request.form["firstNumber"])
    operacao = request.form["operacao"]
    second_number = float(request.form["secondNumber"])
    note=""
    color = "alert-primary"
    if operacao == "plus":
        resultado = first_number + second_number
        note= "adiçao executada com sucesso"
    elif operacao == "minus":
        resultado = first_number-second_number
        note= "subtraçao executada com sucesso"
    elif operacao == "multiply":
        resultado = first_number * second_number
        note= "multiplicaçao executada com sucesso"
    elif operacao == "divide":
        resultado = first_number / second_number
        note= "divisão executada com sucesso"
    else:
        note = "ops... algo deu errado"
        color = "alert-warning " 
        return render_template("simple.html", note=note)
    return render_template("simple.html", resultado=resultado, note=note, color=color)



@app.route('/calculadora_avancado', methods=["post"])
def calculadora_avancado():
    first_number = float(request.form["firstNumber"])
    operacao = request.form["operacao"]
    color="alert-sucess"
    note=""
    try:
        if operacao == "sin":
            resultado = sin(first_number)
            note = "sin has been calculated"
        
        elif operacao == "cos":
            resultado = cos(first_number)
            note = "cos has been calculated"
        
        elif operacao == "tan":
            resultado = tan(first_number)
            note = "tan has been calculated"
        
        elif operacao == "squr":
            resultado = sqrt(first_number)
            note = "squr root has been calculated"
        
        elif operacao == "log":
            resultado = log(first_number)
            note = "log has been calculated"
    
        elif operacao == "exp":
            resultado = exp(first_number)
            note = "exp has been calculated"
        
        elif operacao == "acosh":
            resultado = acosh(first_number)
            note = "acosh has been calculated"
        
        elif operacao == "asinh":
            resultado = asinh(first_number)
            note = "asinh has been calculated"
        
        elif operacao == "atanh":
            resultado = atanh(first_number)
            note = "atanh has been calculated"
        
        elif operacao == "asin":
            resultado = asin(first_number)
            note = "asin has been calculated"
        
        elif operacao == "acos":
            resultado = acos(first_number)
            note = "acos has been calculated"

        else:
            note = "no function has been selected"
            color = "alert-danger"
            return render_template("avancado.html",note=note)
    except ValueError: 
        return render_template("avancado.html", resultado=0, note="erro matematico", color="alert=danger")
    return render_template("avancado.html", resultado=resultado, note=note, color=color)




        
if __name__ == "__main__":
    app.run (debug=True) 
