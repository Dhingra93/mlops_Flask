from flask import Flask, request,jsonify

app=Flask(__name__)

@app.route('/hello',methods=['GET'])
def hello():
    return{"message":"Hello World"}

@app.route('/',methods=['GET'])
def home():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Fluffy Stack Pancake Shop</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      margin: 0;
      padding: 0;
      background: #fff8f0;
      color: #333;
    }
    header {
      background-color: #ffcc70;
      padding: 20px;
      text-align: center;
    }
    header h1 {
      margin: 0;
      font-size: 2.5em;
    }
    nav {
      background: #ffb347;
      text-align: center;
      padding: 10px;
    }
    nav a {
      color: white;
      text-decoration: none;
      margin: 0 15px;
      font-weight: bold;
    }
    .hero {
      background-image: url('https://example.com/pancakes.jpg'); /* Replace with your image */
      background-size: cover;
      background-position: center;
      height: 300px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      text-shadow: 2px 2px 4px #000;
      font-size: 2em;
    }
    .content {
      padding: 30px;
    }
    .menu-section, .contact-section {
      margin-bottom: 40px;
    }
    .menu-items {
      display: flex;
      gap: 20px;
      flex-wrap: wrap;
    }
    .menu-item {
      background: #fff;
      padding: 15px;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      width: 200px;
    }
    footer {
      text-align: center;
      padding: 15px;
      background: #ffb347;
      color: white;
    }
  </style>
</head>
<body>

<header>




'''