import cern.jet.random.Gamma;
import cern.jet.random.engine.MersenneTwister;

public class CallGamma {
  public static void main(String args[]) {
    MersenneTwister mt = new MersenneTwister();
    Gamma gamma = new Gamma(0.5, 0.5, mt);
    System.out.println(gamma.pdf(0));
    System.out.println(gamma.pdf(1));
    System.out.println(gamma.pdf(2));

    System.out.println(gamma.cdf(0));
    System.out.println(gamma.cdf(1));
    System.out.println(gamma.cdf(2));
  }
}

