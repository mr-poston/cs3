public class PredatoryCreditCard extends CreditCard {
    // Additional instance variable
    private double apr;             // annual percentage rate

    // Constructor for this class
    public PredatoryCreditCard(String customer, String bank, String account, int limit, double initialBalance, double rate) {
        super(customer, bank, account, limit, initialBalance);  // initialize superclass attributed
        apr = rate;
    }

    // A new method for assessing monthly interest charges
    public void processMonth() {
        if (balance > 0) {              // only charge interest on a positive balance
            double monthlyFactor = Math.pow(1 + apr, 1.0/12);   // compute monthly rate
            balance *= monthlyFactor;                           // assess interest
        }
    }

    // Overriding the charge method defined in the superclass
    @Override
    public boolean charge(double price) {
        boolean isSuccess = super.charge(price);    // call an inherited method
        if (!isSuccess)
            balance += 5;                           // assess a $5 penalty
        return isSuccess;
    }
}