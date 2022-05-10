**Draft end user instructions:**

1. For best results be as specific as possible.
2. Queries starting with "all schools..." will return full data (with latitude and longitude) to be plotted on a map
3. All other queries automatically group results by year. You may group results by one additional variable such as school level or district by adding "by school level" or similar text at the end of the query.

**Instructions for internal Fab team:**

1. This dummy app just uses a small subset of the original census data to test whether the query actually runs. 
2. Please record details of which natural language queries didn't work.
3. The model 'curie:ft-fab-data-2022-05-06-06-26-14' seems to work the best despite the it uses a less powerful engine (curie) and a smaller training dataset than the most recent model.