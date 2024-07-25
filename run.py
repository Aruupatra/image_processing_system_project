

import eventlet
eventlet.monkey_patch()

from app import app, celery

if __name__ == "__main__":
    app.run(debug=True)




