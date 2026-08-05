from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1 style="text-align:center; padding:100px; background:#0a0a0a; color:#D4AF37; font-family:Georgia;">
    GLAM by Simi<br>
    <a href="/glam" style="color:#D4AF37; font-size:20px;">View 2026 Rate Card →</a>
    </h1>
    '''

@app.route('/glam')
def glam():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>GLAM by Simi - Rate Card 2026</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * {margin:0; padding:0; box-sizing:border-box;}
            body {font-family: 'Georgia', serif; background: #0a0a0a; color: white;}
            .container {max-width: 900px; margin:0 auto; padding: 20px;}
            .header {text-align:center; padding: 40px 20px;}
            .logo {font-size: 60px; font-weight: bold; background: linear-gradient(180deg, #F5DEB3, #CD853F); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
            .by {font-size: 28px; font-style: italic; color: #D4AF37; margin-top: -10px;}
            .rate-title {background: linear-gradient(90deg, #2a1a0a, #4a2a10); padding: 20px; border-radius: 10px; text-align:center; border: 2px solid #D4AF37; margin: 30px 0;}
            .rate-title h1 {font-size: 40px; letter-spacing: 3px;}
            table {width: 100%; border-collapse: collapse; background: #111; border-radius: 10px; overflow: hidden; border: 1px solid #D4AF37;}
            th {background: #2a1a0a; padding: 15px; font-size: 18px; text-align: left; color: #D4AF37;}
            td {padding: 18px 15px; border-bottom: 1px dashed #333;}
            td.price {text-align:right; font-weight:bold; font-size:18px;}
            .footer {background: #111; padding: 30px; border-radius: 10px; text-align:center; border: 1px solid #D4AF37; margin-top:30px;}
            .whatsapp-btn {display:inline-block; background:#D4AF37; color:black; padding:12px 25px; border-radius:25px; text-decoration:none; font-weight:bold;}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="logo">GLAM 👑</div>
                <div class="by">by Simi ♡</div>
                <p>ENHANCING YOUR BEAUTY, ONE FACE AT A TIME.</p>
            </div>
            
            <div class="rate-title"><h1>RATE CARD 2026</h1></div>
            
            <table>
                <tr><th>SERVICES (STUDIO RATES)</th><th style="text-align:right;">PRICES</th></tr>
                <tr><td>SOFT GLAM</td><td class="price">₦20,000</td></tr>
                <tr><td>BIRTHDAY GLAM</td><td class="price">₦25,000</td></tr>
                <tr><td>OWAMBE / TRADITIONAL GLAM</td><td class="price">₦25,000</td></tr>
                <tr><td>CIVIL WEDDING GLAM</td><td class="price">₦50,000</td></tr>
                <tr><td>BRIDAL GLAM</td><td class="price">FROM ₦80,000</td></tr>
                <tr><td>NYSC / POP SHOOT</td><td class="price">₦15,000</td></tr>
                <tr><td>HOME SERVICE</td><td class="price">PRICE VARIES</td></tr>
            </table>
            
            <div class="footer">
                <p><b>BOOKINGS:</b> 07065053054 / 09114916267</p>
                <p><b>INSTAGRAM:</b> @Glam_by_simi01</p>
                <p><b>LOCATION:</b> AKURE, ONDO STATE</p>
                <a href="https://wa.me/2347065053054" class="whatsapp-btn">Book on WhatsApp</a>
            </div>
        </div>
    </body>
    </html>
    '''
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
