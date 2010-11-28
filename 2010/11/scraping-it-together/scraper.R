data <- read.table("{{ d['filenames']['scraper-data.csv|dexy'] }}", sep=",", header=TRUE)

# Convert Y-m-d strings to dates, sort by date.
data[,1] <- as.POSIXct(data[,1])
sorted.data <- data[order(data[,1]),]

# Determine overall min and max for y axis range
min.temp <- min(sorted.data$tmin, na.rm=TRUE)
max.temp <- max(sorted.data$tmax, na.rm=TRUE)

png(file="{{ a.create_input_file('max-temps', 'png') }}", width=500, height=500)
plot(
    sorted.data$Date, 
    sorted.data$tmean, 
    type="l", 
    lwd=2, 
    ylim=c(min.temp-2, max.temp+2),
    ylab=expression("Temperature"*degree~C)
)
points(sorted.data$Date, sorted.data$tmax, type="l", lty=3, col="red")
points(sorted.data$Date, sorted.data$tmin, type="l", lty=3, col="blue")
dev.off()

summary(data$tmin)
summary(data$tmax)
summary(data$tmean)
