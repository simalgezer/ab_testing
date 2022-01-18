# ab_testing
AB testing Facebook's two features: max bidding and average bidding.

What is AB testing: AB testing is a user experience research methodology with two variants, A and B. 

Steps used for AB testing:
1. used the shapiro test for both control and test groups to confirm the normal distribution.
2. used the levene test to test variance homogeneity.
3. confirming that control and test groups are normally distributed and their variances are homogenous, applied the two-independent sample t-test (parametric test) and two-proportion z-test for A/B testing.

Business Problem: Facebook recently introduced a new bid called “average bidding” as an alternative to the “maximum bidding” option.
bombabomba.com — Facebook’s client — has decided to test this new feature and wants to make it an A/B to see whether “average bidding” does fetch more conversions than “maximum bidding”. The dataset includes the website information of bombabomba.com. There is information such as the number of advertisements that users see and click, as well as the purchase information from the ads. There are two separate datasets: “control group” for max bidding and “test group” for average bidding.

Two datesets:
1. Control Group — The dataset formed by applying “Maximum bidding”
2. Test Group — The dataset formed by applying “Average bidding”

Variables:
1. Impression — Ad views
2. Click — Indicates the number of clicks on the displayed ad
3. Purchase — Indicates the number of products purchased after clicking the ad
4. Earning — Earnings from the purchased products
