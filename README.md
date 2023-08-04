# Weather_APP

This is a simple weather application that provides weather information based on user input.

Installation:

1.Clone this repository to your local machine using git clone https://github.com/blacknoir00/Weather_APP.git
2.Navigate to the Weather_APP directory.

Prerequisites:

Make sure you have the following installed:

Python 3.x
Flask (You can install it using pip install Flask)

Running the Application:

1.Open a terminal or command prompt.

2.Change the directory to the Weather_APP folder.

3.Run the following command to start the Flask development server:

python application.py

The server should start running
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

# Deploy the application to a cloud-based platform (Amazon Web Service).

Create Elastic Beanstalk Environment

1.Open AWS Management Console and navigate to Elastic Beanstalk service.

2.Click "Create Environment" and choose "Web server environment."

3.Select "Python" as the platform and upload your application code (zipped).

4.click on create.

5.click on Environments and select Weather-env-1,clcik upload and deploy,wait for few minutes to create instance.

6.click on the domain address to open web application.

http://weatherapp-env-1.eba-rwkevnrv.ap-south-1.elasticbeanstalk.com/
