import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailService:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def send_movie_report(self, recipient, movies):
        """Sends a beautiful text-focused HTML email with the movie report."""
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "🍿 Weekly Movie Report - Watch vs. Skip"
        msg['From'] = self.user
        msg['To'] = recipient

        # Build HTML content
        html_body = f"""
        <html>
        <head>
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #1a1a1a; color: #f2f2f2; padding: 20px; }}
                .container {{ max-width: 600px; margin: 0 auto; background-color: #262626; padding: 20px; border-radius: 12px; }}
                .header {{ text-align: center; border-bottom: 2px solid #e50914; padding-bottom: 20px; margin-bottom: 30px; }}
                .movie-card {{ background-color: #333; margin-bottom: 25px; border-radius: 8px; padding: 25px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); border-left: 5px solid #444; }}
                .title {{ font-size: 24px; font-weight: bold; color: #fff; margin-bottom: 8px; }}
                .meta {{ font-size: 14px; color: #aaa; margin-bottom: 15px; }}
                .meta-item {{ margin-right: 15px; background: #444; padding: 3px 10px; border-radius: 4px; border: 1px solid #555; }}
                .rating {{ font-size: 18px; color: #f1c40f; margin-bottom: 15px; font-weight: bold; }}
                .summary {{ font-size: 16px; line-height: 1.6; color: #ccc; margin-bottom: 20px; }}
                .ranking-box {{ display: inline-block; padding: 10px 20px; border-radius: 6px; font-weight: bold; text-transform: uppercase; margin-bottom: 20px; border: 1px solid transparent; letter-spacing: 1px; }}
                .watch {{ background-color: rgba(46, 204, 113, 0.15); color: #2ecc71; border-color: #2ecc71; }}
                .skip {{ background-color: rgba(231, 76, 60, 0.15); color: #e74c3c; border-color: #e74c3c; }}
                .consider {{ background-color: rgba(241, 196, 15, 0.15); color: #f1c40f; border-color: #f1c40f; }}
                .trailer-link {{ display: inline-block; color: #e50914; text-decoration: none; font-weight: bold; font-size: 16px; transition: 0.3s; }}
                .trailer-link:hover {{ text-decoration: underline; }}
                .footer {{ text-align: center; margin-top: 50px; font-size: 14px; color: #666; border-top: 1px solid #333; padding-top: 20px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1 style="margin: 0; font-size: 32px;">🎬 Weekly Movie Guide</h1>
                    <p style="margin: 10px 0 0 0; color: #888;">Curated watchlist for the week ahead</p>
                </div>
        """

        for movie in movies:
            # Parse ranking and summary from AI response
            analysis_text = movie['analysis']
            summary = ""
            ranking = "CONSIDER"
            reason = ""
            
            for line in analysis_text.split('\n'):
                if line.startswith("SUMMARY:"): summary = line.replace("SUMMARY:", "").strip()
                elif line.startswith("RANKING:"): ranking = line.replace("RANKING:", "").strip()
                elif line.startswith("REASON:"): reason = line.replace("REASON:", "").strip()

            rank_class = ranking.lower() if ranking.lower() in ['watch', 'skip', 'consider'] else 'consider'
            
            html_body += f"""
                <div class="movie-card" style="border-left-color: {'#2ecc71' if rank_class=='watch' else '#e74c3c' if rank_class=='skip' else '#f1c40f'}">
                    <div class="title">{movie['title']}</div>
                    <div class="meta">
                        <span class="meta-item">📅 {movie.get('release_date', 'Next Week')}</span>
                        <span class="meta-item">📍 {movie.get('platform', 'N/A')}</span>
                    </div>
                    <div class="rating">⭐ {movie.get('rating', 'N/A')}</div>
                    <div class="summary">
                        {summary}<br><br>
                        <strong>AI Verdict:</strong> {reason}
                    </div>
                    <div class="ranking-box {rank_class}">{ranking}</div>
                    <div><a href="{movie['trailer']}" class="trailer-link">🔗 View Trailer on YouTube &rarr;</a></div>
                </div>
            """

        html_body += """
                <div class="footer">
                    <p>Designed for privacy. No external images loaded.<br>Automated weekly by your AI Movie Agent.</p>
                </div>
            </div>
        </body>
        </html>
        """

        part2 = MIMEText(html_body, 'html')
        msg.attach(part2)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(self.user, self.password)
            server.sendmail(self.user, recipient, msg.as_string())
            server.quit()
            return True
        except Exception as e:
            print(f"SMTP Error: {e}")
            return False
