import sys
import time
import argparse
import request, requests
from classmodule import MyClass
import whois
import click


@click.command()
@click.option('--number1', prompt='Number 1:', help='First Number')
@click.option('--number2', prompt='Number 2', help='Second Number')
@click.option('--operation', prompt='Enter operation (add, subtract, multiply, divide)', help='Operation')
def Calculator(number1,number2,operation):
    n1 = int(number1)
    n2 = int(number2)
    result = ''
    if operation == "add":
        result = n1+n2
    elif operation == "subtract":
        result = n1-n2
    elif operation == "multiply":
        result = n1*n2
    elif operation == "divide":
        result = n1/n2
    else:
        print("unspported operation")
        
    print("Result:", result)

@click.command()
@click.option('--domain', prompt='Please enter a domain', help='Enter a domain')
def whoisDomain(domain):
    w = whois.whois(domain)
    print(w)

@click.command()
@click.option('--zipcode', prompt='Please enter a zipcode', help='Enter a zipcode')
def GetTempByZipCode(zipcode):
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=0bfdb889cbb648fab0ac52f70199760e')
    json_object = r.json()
    tempk= float(json_object["main"]["temp"])
    tempf = (tempk -273.15)*1.8+32
    print(tempf)

@click.command()
@click.option('--count', prompt='Number of greets', help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def Greeter(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    counter = int(count)
    for x in range(counter):
        click.echo('Hello %s!' % name)


@click.command()
@click.option('--selection', 
                prompt='Please enter a selection 1=Greeter, 2=Get Temperature by Zipcode, 3=Calculator 4=Get WhoIs info', 
                help='Selection Choice')
def main(selection):
    if selection == "1":
        Greeter()
    elif selection == "2":
        GetTempByZipCode()      
    elif selection == "3":
        Calculator()
    elif selection == "4":
        whoisDomain()
    else:
        print("unspported operation")


if __name__ == '__main__':
    main()