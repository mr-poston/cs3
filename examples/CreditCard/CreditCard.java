public class CreditCard {
    // Instance variables
    private String customer;        // name of the customer
    private String bank;            // name of the bank
    private String account;         // account identifier
    private int limit;              // credit limit
    protected double balance;       // current balance

    // Constructors
    public CreditCard(String customer, String bank, String account, int limit, double initialBalance) {
        this.customer = customer;
        this.bank = bank;
        this.account = account;
        this.limit = limit;
        this.balance = initialBalance;
    }

    public CreditCard(String customer, String bank, String account, int limit) {
        this(customer, bank, account, limit, 0.0);
    }

    // Accessor methods
    public String getCustomer() {
        return customer;
    }

    public String getBank() {
        return bank;
    }

    public String getAccount() {
        return account;
    }

    public int getLimit() {
        return limit;
    }

    public double getBalance() {
        return balance;
    }

    // Update methods
    public boolean charge(double price) {           // make a charge
        if (price + balance > limit)                // if charge would surpass limit
            return false;                           // refuse the charge
        // at this point the charge is successful
        balance += price;                           // update the balance
        return true;                                // announce the good news
    }

    public void makePayment(double amount) {        // make a payment
        balance -= amount;
    }

    // Utility method to print a card's information
    public static void printSummary(CreditCard card) {
        System.out.println("Customer = " + card.customer);
        System.out.println("Bank = " + card.bank);
        System.out.println("Account = " + card.account);
        System.out.println("Balance = " + card.balance);    // implicit cast (int -> String)
        System.out.println("Limit = " + card.limit);        // implicit cast (double -> String)
    }

    // main method for testing
    public static void main(String[] args) {
        CreditCard[] wallet = new CreditCard[3];
        wallet[0] = new CreditCard("Peter Quill", "Texas Savings", "5391 0375 9387 5309", 5000);
        wallet[1] = new CreditCard("Peter Quill", "Texas Federal", "3485 0399 3395 1954", 3500);
        wallet[2] = new CreditCard("Peter Quill", "Texas Finance", "5391 0375 9387 5309", 2500, 300);

        for (int val = 1; val <= 16; val++) {
            wallet[0].charge(3 * val);
            wallet[1].charge(2 * val);
            wallet[2].charge(val);
        }

        for (CreditCard card : wallet) {
            CreditCard.printSummary(card);      // calling static method
            while (card.getBalance() > 200.0) {
                card.makePayment(200);
                System.out.println("New balance = " + card.getBalance());
            }
            System.out.println();
        }
    }
}