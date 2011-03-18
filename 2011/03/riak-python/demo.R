data = read.csv("dexy--highs-by-month.csv",
    col.names=c("Date", "High"),
    header=FALSE)
summary(data$High)


library(zoo)
zoo.data <- zoo(data$High, order.by=data$Date, frequency=12)

png(file="dexy--monthly-highs.png", width=500, height=500)
plot(
    zoo.data,
    col="purple",
    main="Monthly Highs")
dev.off()
