
# Recipe Time-Claim Rubric

## Question

Does the recipe’s total time fit the user’s stated time limit?

## Decision rule

Use the numeric limit in the request. For a range such as **30–60 minutes**, use its upper end (60 minutes) with no extra tolerance. For a single approximate target of **30 minutes**, this exercise allows a 5-minute tolerance, so the maximum is 35 minutes.

- **Pass:** The recipe can be ready in 35 minutes or less, including all required prep, waiting, and cooking. A shorter time can Pass if it is plausible from the stated starting ingredients.
- **Fail:** The known minimum time for required steps already exceeds the allowed maximum, or a reviewer-estimated total does.
- **Review:** The request uses a vague word like “quick,” or missing durations/pre-prepared ingredients leave the result uncertain. Missing details do not force Review when the known minimum alone proves Fail.

Do not mark a recipe Fail just because it is faster than 25 minutes. Check whether its time starts from the ingredients and preparation state the recipe actually describes.

## Time to include

Count required preparation, marinating, cooking, and waiting time. Exclude optional steps and optional sides. Treat pre-prepared ingredients as an assumption that must be stated.

## Example

`SYN018` asks for a “quick” salmon dinner but gives no numeric time limit. Label it **Review**; “quick” alone does not define a measurable limit.

`SYN069` asks for a dish in 30–60 minutes. The required lentils soak for at least 60 minutes, then pressure cook for at least 15 minutes and simmer for at least 15 minutes. The masala is prepared while the lentils cook, so those minutes overlap; even this lower bound is 90 minutes. Label it **Fail**, although the pressure-release duration is unstated.
