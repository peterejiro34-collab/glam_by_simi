from flask import Flask
app = Flask(__name__)

@app.route('/')
def glam():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>GLAM by Simi - Rate Card 2026</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * {margin:0; padding:0; box-sizing:border-box;}
            body {
                font-family: 'Georgia', serif;
                background: #0a0a0a;
                color: white;
                background-image: radial-gradient(circle at top right, #3a2a0a 0%, #0a0a0a 50%);
            }
            .container {max-width: 900px; margin:0 auto; padding: 20px;}
            
            .header {text-align:center; padding: 40px 20px;}
            .logo {font-size: 60px; font-weight: bold; background: linear-gradient(180deg, #F5DEB3, #CD853F); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
            .by {font-size: 28px; font-style: italic; color: #D4AF37; margin-top: -10px;}
            .tagline {font-size: 14px; letter-spacing: 2px; margin: 15px 0; color: #ccc;}
            
            .rate-title {
                background: linear-gradient(90deg, #2a1a0a, #4a2a10);
                padding: 20px;
                border-radius: 10px;
                text-align:center;
                border: 2px solid #D4AF37;
                margin: 30px 0;
            }
            .rate-title h1 {font-size: 40px; letter-spacing: 3px;}
            .year-badge {background: #D4AF37; color: black; padding: 5px 20px; border-radius: 20px; display:inline-block; font-weight:bold; margin-top: 10px;}
            
            table {
                width: 100%;
                border-collapse: collapse;
                background: #111;
                border-radius: 10px;
                overflow: hidden;
                border: 1px solid #D4AF37;
            }
            th {
                background: #2a1a0a;
                padding: 15px;
                font-size: 18px;
                text-align: left;
                color: #D4AF37;
            }
            td {
                padding: 18px 15px;
                border-bottom: 1px dashed #333;
            }
            td.price {text-align:right; font-weight:bold; font-size:18px;}
            .from {font-size:12px; color:#D4AF37;}
            .varies {font-size:14px; color:#D4AF37; font-weight:bold;}
            
            .note-box {
                background: #111;
                border: 1px solid #D4AF37;
                border-radius: 10px;
                padding: 20px;
                margin: 30px 0;
                display: flex;
                flex-wrap: wrap;
                gap: 20px;
                justify-content: space-around;
            }
            .note-item {flex:1; min-width:200px; text-align:center;}
            .note-item p {font-size:13px; margin-top:8px;}
            
            .footer {
                background: #111;
                padding: 30px;
                border-radius: 10px;
                text-align:center;
                border: 1px solid #D4AF37;
            }
            .contact-grid {display:flex; flex-wrap:wrap; justify-content:center; gap:30px; margin:20px 0;}
            .contact-item a {color: #D4AF37; text-decoration:none; font-weight:bold; font-size:18px;}
            .whatsapp-btn {
                display:inline-block; background:#D4AF37; color:black; padding:12px 25px; 
                border-radius:25px; text-decoration:none; font-weight:bold; margin-top:10px;
            }
            .location {background:#D4AF37; color:black; padding:10px; border-radius:20px; display:inline-block; margin-top:20px; font-weight:bold;}
            
            @media(max-width:600px){
                .logo {font-size:40px;}
                .rate-title h1 {font-size:28px;}
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="logo">GLAM 👑</div>
                <div class="by">by Simi ♡</div>
                <div class="tagline">ENHANCING YOUR BEAUTY, ONE FACE AT A TIME.</div>
            </div>
            
            <div class="rate-title">
                <h1>RATE CARD</h1>
                <div class="year-badge">2026 PRICE LIST</div>
            </div>
            
            <table>
                <tr><th>SERVICES (STUDIO RATES)</th><th style="text-align:right;">PRICES</th></tr>
                <tr><td>SOFT GLAM</td><td class="price">₦20,000</td></tr>
                <tr><td>BIRTHDAY GLAM</td><td class="price">₦25,000</td></tr>
                <tr><td>OWAMBE / TRADITIONAL GLAM</td><td class="price">₦25,000</td></tr>
                <tr><td>CIVIL WEDDING GLAM</td><td class="price">₦50,000</td></tr>
                <tr><td>BRIDAL GLAM</td><td class="price"><span class="from">FROM</span><br>₦80,000</td></tr>
                <tr><td>NYSC / POP SHOOT</td><td class="price">₦15,000</td></tr>
                <tr><td>HOME SERVICE</td><td class="price"><span class="varies">PRICE VARIES<br>BY LOCATION</span></td></tr>
            </table>
            
            <h3 style="text-align:center; color:#D4AF37; margin:30px 0 10px;">PLEASE NOTE</h3>
            <div class="note-box">
                <div class="note-item">
                    <p><b>A non-refundable booking fee is required to secure your slot.</b></p>
                </div>
                <div class="note-item">
                    <p><b>You're to pay 10% of your payment to book ahead.</b></p>
                </div>
                <div class="note-item">
                    <p><b>Home Service: Price varies by location.</b></p>
                </div>
            </div>
            
            <div class="footer">
                <p style="font-style:italic; font-size:20px;">Let's make you <br><b style="font-size:24px;">UNFORGETTABLE.</b></p>
                
                <div class="contact-grid">
                    <div class="contact-item">
                        <p><b>BOOKINGS & ENQUIRIES</b></p>
                        <p>DM OR WHATSAPP TO BOOK</p>
                        <a href="tel:07065053054">07065053054</a><br>
                        <a href="tel:09114916267">09114916267</a><br>
                        <a href="https://wa.me/2347065053054" class="whatsapp-btn">Chat on WhatsApp</a>
                    </div>
                    <div class="contact-item">
                        <p><b>FOLLOW US</b></p>
                        <p>INSTAGRAM: @Glam_by_simi01</p>
                        <p>TIKTOK: @glam_by_simi / muainakure</p>
                    </div>
                </div>
                
                <div class="location">📍 BASED IN AKURE, ONDO STATE</div>
            </div>
        </div>
    </body>
    </html>
    '''
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
