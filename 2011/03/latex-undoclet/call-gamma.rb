require 'java'

include_class 'cern.jet.random.Gamma'
include_class 'cern.jet.random.engine.MersenneTwister'

mt = MersenneTwister.new()
gamma = Gamma.new(0.5, 0.5, mt)
gamma.pdf(0)
gamma.pdf(1)
gamma.pdf(2)

gamma.cdf(0)
gamma.cdf(1)
gamma.cdf(2)
