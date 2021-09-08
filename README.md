# Multiobjective-recommendation-for-sustainable-production-systems

We present a recommendation system to help rebuild sustainable production systems. Our multi-objective system synergizes the public and private actors of a territory. From know-how proximities in the Product Space, we suggest productive jumps for companies in a territory that consider the expectations of companies not only in terms of diversification but also in terms of the expectations of local authorities who are anxious to build sustainable production systems.
  We formalize a multi-stakeholder recommendation that is applied to the sustainability of a territorial economy and we propose the following new objectives to consider:
  - Economic growth, based on the concept of territorial economic complexity;
  - Productive resilience, defined rigorously from the theory of dynamic systems; 
  - Food security and more generally basic necessities from an original approach based on Maslow's hierarchy of needs;
  - The need to develop greener productions that respect the environment.

  The recommendation system that we propose incorporates territorial policy as a weighting of objectives. This "configuration" acts directly on the system to influence the recommended productive jumps. Each objective is defined to be computed directly from open data available for most countries without requiring external data.

# Formalization
We perform a weighted hybridization from the different objectives to re-rank the list ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cmathcal%7BA%7D). 

For each production unit u we compute the scores ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20%5C%7B%5Chat%7Bp%7D_%7Ba_1%7D%28x_i%7Cu%29%2C%20%5Chat%7Bp%7D_%7Ba_2%7D%28x_i%7Cu%29%2C%20%5Cldots%2C%20%5Chat%7Bp%7D_%7Ba_n%7D%28x_i%7Cu%29%5C%7D) of each product ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20x_i%20%5Cin%20%5Cmathcal%7BA%7D) for each algorithm ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20%5C%7Ba_1%2C%20a_2%2C%20%5Cldots%2C%20a_n%5C%7D). All scores must be normalized. Then we perform a weighted sum of each score to obtain a final score for each product: 

![equation](https://latex.codecogs.com/gif.latex?%5Chat%7Bp%7D%28x_i%20%5Cvert%20c%29%20%3D%20%5Csum_%7Bj%3D1%7D%5E%7Bn%7D%20%5Chat%7Bp%7D_%7Ba_j%7D%28x_i%20%5Cvert%20c%29%20%5Ctimes%20w_%7Ba_j%7D)

Presented at the MORS workshop held in conjunction with the 15th ACM Conference on Recommender Systems (RecSys), 2021, in Amsterdam, Netherlands.
