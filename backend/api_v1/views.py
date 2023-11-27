from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# temp home page status
def home_view(request,*args, **kwargs):
    return HttpResponse(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NPI Files</title>
        <style>
            /* Inline CSS */
            body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
            }
            header {
            background-color: #007bff;
            color: white;
            padding: 15px;
            text-align: center;
            }
            .container {
            width: 80%;
            margin: 20px auto;
            }
            .file-section {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            }
            .file {
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 20px;
            margin: 10px;
            width: 30%;
            text-align: center;
            transition: transform 0.3s ease-in-out;
            }
            .file:hover {
            transform: scale(1.05);
            }
            footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px;
            position: absolute;
            bottom: 0;
            width: 100%;
            }
        </style>
        </head>
        <body>
        <header>
            <h1>NPI Files</h1>
        </header>
        <div class="container">
            <div class="file-section">
            <!-- File links -->
            <div class="file">
                <h2>NPI Files</h2>
                <a href="api/v1/">Download</a>
            </div>
            <div class="file">
                <h2>SCC Files</h2>
                <a href="api/docs">Download</a>
            </div>
             <div class="file">
                <h2>Admin Files</h2>
                <a href="admin">Download</a>
            </div>
            </div>
        </div>
        <footer>
            <p>&copy; 2023 NPI Files. All rights reserved.</p>
        </footer>
        <script>
            // Inline JavaScript (if needed)
            // You can add scripts here for any specific functionalities
        </script>
        </body>
        </html>
        """)
