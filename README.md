# READ ME
## To cURL:
cURL to the [/premium](http://localhost:5000/premium) endpoint using a sample request

### Example:
`curl -H "Content-Type: application/json" --data @projects/ratingApp/samples/sample2.json http://localhost:5000/premium`

## To Run App:
### Local Install
1. Activate virtual environment

    `. venv/bin/activate`

2. Install dependencies

    `pip install -r requirements.txt`

3. Set path and run app:

    `export FLASK_APP='application.py'`

    `flask run`

4. Open [localhost:5000](http://localhost:5000) in your browser
5. cURL to [/premium](http://localhost:5000/premium) with JSON request to get the cost of a quoted premium

**Hosted Application - AWS Elastic Beanstalk**
1. To try the hosted app: [Click Here](http://ratingengine-env-1.eba-mpx2jmqg.us-east-1.elasticbeanstalk.com) to run the app
2. Or for a quick quote cURL your request to [/premium](http://ratingengine-env-1.eba-mpx2jmqg.us-east-1.elasticbeanstalk.com/premium) endpoint with JSON request to get the cost of a quoted premium
**Example:**

`curl -H "Content-Type: application/json" --data @projects/ratingApp/samples/sample2.json http://ratingengine-env-1.eba-mpx2jmqg.us-east-1.elasticbeanstalk.comµµµ/premium`