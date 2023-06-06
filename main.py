# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

#authorsnote: I would like to have the feedback in English.

#Part 1: Greet Template
def greet(name, greeting_template='Hello, <name>!'):
  return greeting_template.replace('<name>', name)

print(greet('Bob', "What's up, <name>!"))

#Part 2: Force
def force(mass, body='earth'):
  gravity_factor= {
    'mercury': 3.7,
    'venus': 8.9,
    'earth': 9.8,
    'moon': 1.6,
    'mars': 3.7,
    'jupiter': 23.1,
    'saturn': 10.4,
    'uranus': 8.7,
    'neptune': 11,
    'pluto': 0.6,
    'sun': 274,
    }
  
  gravity = gravity_factor.get(body) 
  if gravity is None:
        gravity = 9.8
  return round(mass* gravity,2)

print(force(2, 'earth'))

#Part 3: Gravity
def pull(m1, m2, d):
  G= 6.674e-11
  return G*((m1*m2)/ (d**2))
print(pull(800, 1500, 3))
