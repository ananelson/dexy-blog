library(YaleToolkit)
library(grDevices)
filename = "dexy--random-spark.pdf"
pdf(file=filename, width=2.5, height=1)
### @export "spark"
sparkline(rnorm(10), ptopts = 'first.last',
    margins=unit(c(0.2,0.2,0.2,0.6), 'inches'),
    IQR=gpar(fill="#F7ECDA", col='#F7ECDA'))
### @end
embedFonts(filename)
dev.off()
