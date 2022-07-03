# Forecasting model(s)

This service forecasts wins over 500 for each team for the next few games.

## To do (for this service)
- Add code handling the http request/response data.
- Add code for loading and saving ELO model weights from a bucket.
- Improve the model and experiment with other models.

## To do (for other services)
- data-pipeline: make request to model. Add response to json output for dashboard.
- dashboard: incorporate forecast into plot.

## To do (infrastructure)
- Create new service.
- Add github action for deployment.
- Create buckets for model weights.

# Model Descriptions

## Basic Elo model (`elo.py`)

The Elo model is essentially a logistic regression model. The output is the probability that the home team wins. In it's simplest form, the input is the data of the home team and the visiting team. Teams are represented as one-hot vectors. The relative strength of a team is given by the corresponding coefficient in the logistic regression model. I.e., the log-odds that the home team wins is roughly proportional to the difference of regression coefficients `b_home - b_visitor` ('proportional to' because the sigmoid function is scaled by a temperature parameter). 

On average, the home team in baseball wins about 53% of the time.  This advantage is represented by the y-intercept term in the logistic regression model. (thus, the log-odds is actually proportional to a shift of `b_home - b_visitor`).

Model parameters are updated in an online fashion via stochastic gradient descent. The learning rate is a hyperparameter.

## Adjusted Elo model (`adjusted_elo.py`)

The adjusted Elo model incorporates other contextual factors.

## Bayesian model (`full_bayes.py`)


## Glicko model (`approximate_bayes.py`)