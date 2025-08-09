from flask import Flask

app = Flask(__name__)

from routes.main import *

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=False)  # Ensure debug mode is disabled for security
=======
    app.run()
>>>>>>> 231d9d82089d25fb6a1f0619468f315185121de9
