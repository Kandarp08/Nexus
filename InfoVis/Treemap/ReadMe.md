Prerequisites Node.js and npm: Ensure Node.js and npm are installed on your system. You can download them from the official Node.js website.

http-server: A simple static file server. Install it globally using npm:

Bash npm install -g http-server

Running the Visualization Host the CSV File:

Start a local HTTP server to serve the twitch_total_views.csv file in the directory the file is present: Bash http-server -p 8080

This will make the CSV file accessible at http://localhost:8080/twitch_total_views.csv. Run the HTML File:

Start another HTTP server to serve the index.html file: Bash http-server -p 8081

This will make the visualization accessible at http://localhost:8081. Open in Browser:

Open http://localhost:8081 in your web browser to view the Twitch viewer treemap.

Start another HTTP server to serve the partner.html file: Bash http-server -p 8082

This will make the visualization accessible at http://localhost:8082/partner.html. Open in Browser:

Open http://localhost:8082/partner.html in your web browser to view the treemap

Start another HTTP server to serve the days_partner.html file: Bash http-server -p 8083

This will make the visualization accessible at http://localhost:8083/days_partner.html. Open in Browser:

Open http://localhost:8083/days_partner.html in your web browser to view the treemap

