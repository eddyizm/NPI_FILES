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
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f4;
                }

                header {
                    background-color: #333;
                    color: #fff;
                    padding: 15px;
                    text-align: center;
                }

                .container {
                    width: 80%;
                    margin: 20px auto;
                }

                .file-list {
                    list-style: none;
                    padding: 10;
                }

                .file-list li {
                    margin-bottom: 10px;
                    padding: .5em;
                }

                .download-btn {
                    padding: 8px 15px;
                    background-color: #007bff;
                    color: #fff;

                    text-decoration: none;
                    border-radius: 5px;
                }

                .download-btn:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>

        <body>
            <header>
                <h1>NPI Files</h1>
            </header>

            <div class="container">
                <ul class="file-list">
                    <li>
                        <span>NPI File</span>
                        <a href="api_v1/" class="download-btn">Download</a>
                    </li>
                    <li>
                        <span>SCC File</span>
                        <a href="api_v1/docs" class="download-btn">Download</a>
                    </li>
                    <li>
                        <span>Admin Access</span>
                        <a href="admin/" class="download-btn">GO!</a>
                    </li>
                    <!-- Add more files as needed -->
                </ul>
            </div>
        </body>
        </html>
        """)
