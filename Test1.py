from lifelines.datasets import load_dd
from lifelines import KaplanMeierFitter

# Load the dataset
data = load_dd()

# Create an instance of KaplanMeierFitter
kmf = KaplanMeierFitter()

# Fit the data into the model
kmf.fit(durations = data['duration'], event_observed = data['observed'])

# Create an estimate of the survival function
kmf.plot_survival_function()

# Calculate the median survival time
median_survival_time = kmf.median_survival_time_

print("The median survival time is:", median_survival_time)