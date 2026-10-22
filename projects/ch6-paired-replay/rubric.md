
# Chapter 6 Oatmeal Rubric

## Evaluation target

Judge the final assistant response after all user constraints have been provided. Earlier incomplete suggestions do not count as a failure if the final response corrects them.

## Observable goal

The final response gives one identifiable oatmeal breakfast. This exercise checks visible recipe content only; it does not judge whether “healthy” or nutrition claims are true.

## Labels

- **Pass:** Gives a usable oatmeal idea, lists no dairy ingredients (including optional ingredients), and suggests no added sweetener. Water, unsweetened plant milk, and unsweetened fruit are allowed.
- **Fail:** Gives no oatmeal idea, lists dairy as an ingredient or option, or suggests an added sweetener. For this exercise, added sweeteners include sugar, honey, syrup, stevia, and monk-fruit extract.
- **Review:** The final response is too unclear to tell whether it meets these text-based checks.

## Scope

“No added sweetener” is our test rule for the low-sugar request. It is not a general nutrition standard. Do not assess medical or blood-sugar claims.

## Oatmeal-v3 perturbation: peanut-free and tree-nut-free

Keep all oatmeal-v2 rules. For oatmeal-003, also check the recipe ingredients and options:

- **Pass:** The recipe recommends no peanuts or tree nuts. Seeds are allowed.
- **Fail:** The recipe recommends peanuts or tree nuts, including as optional toppings, substitutions, or plant milks.
- **Review:** An ingredient is too vague to tell whether it contains peanuts or tree nuts.

This is a text-only check. Do not assess cross-contact, product brands, or medical safety.
