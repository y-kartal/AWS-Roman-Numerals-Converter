from flask import Flask, render_template, request

app = Flask(__name__)

def convert(decimal_num):
    roman = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    num_to_roman = ''

    for i in roman.keys():
        num_to_roman += roman[i]*(decimal_num//i) 
        decimal_num %= i
    return num_to_roman








if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)
