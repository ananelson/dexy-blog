### @export "import-library"
library(stargazer)

### @export "basic-demo"
stargazer(attitude)

### @export "basic-demo-with-sink"
sink("output-from-sink.tex")
stargazer(attitude)
sink()

### @export "create-object"
latex.snippets <- list()
latex.snippets["attitude"] <- paste(stargazer(attitude), collapse="\n")

### @export "ols-models"
## 2 OLS models
linear.1 <- lm(rating ~ complaints + privileges + learning + raises + critical, data=attitude)
linear.2 <- lm(rating ~ complaints + privileges + learning, data=attitude)
 
## create an indicator dependent variable, and run a probit model
 
attitude$high.rating <- (attitude$rating > 70)
probit.model <- glm(high.rating ~ learning + critical + advance, data=attitude, family = binomial(link = "probit"))
 
regression.results <- stargazer(linear.1, linear.2, probit.model, title="Regression Results", align=TRUE)

### @export "save-ols-models"
latex.snippets["regression"] <- paste(regression.results, collapse="\n")

### @export "save-objects"
library(rjson)
latex.snippets.file <- file("stargazer-snippets.json", "w")
writeLines(toJSON(latex.snippets), latex.snippets.file)
close(latex.snippets.file)

